#include "MSaveFileImpl.h"

enum MSaveType
{
    eInt,
    eFloat,
    eString
};

struct _MSaveValue
{
    _MSaveValue(MSaveType t, const void* p, size_t s)
    {
        type = t;
        value = new char[s];
        memcpy(value, p, s);
    }

    ~_MSaveValue()
    {
        delete[] (char*)value;
    }

    MSaveType type;
    void*     value;
};

MSaveFileImpl::MSaveFileImpl(const char* filename, MSaveFileMode mode)
: m_mode(mode)
{
    m_filename = new char[strlen(filename+1)];
    sprintf(m_filename, "%s", filename);

    load();
}

MSaveFileImpl::~MSaveFileImpl()
{
    save();

    for(std::map<std::string, _MSaveValue*>::iterator iVal = m_values.begin();
        iVal != m_values.end();
        ++iVal)
        delete iVal->second;

    delete[] m_filename;
}

MSaveFile* MSaveFileImpl::getNew(const char* filename, MSaveFileMode mode)
{
    return new MSaveFileImpl(filename, mode);
}

void MSaveFileImpl::destroy()
{
    delete this;
}

void MSaveFileImpl::setInt(const char* key, const int val)
{
    if(m_values.find(key) != m_values.end())
        delete(m_values[key]);

    m_values[key] = new _MSaveValue(eInt, &val, sizeof(int));
    m_isDirty = true;
}

void MSaveFileImpl::setFloat(const char* key, const float val)
{
    if(m_values.find(key) != m_values.end())
        delete(m_values[key]);

    m_values[key] = new _MSaveValue(eFloat, &val, sizeof(float));
    m_isDirty = true;
}

void MSaveFileImpl::setString(const char* key, const char* val)
{
    if(m_values.find(key) != m_values.end())
        delete(m_values[key]);

    m_values[key] = new _MSaveValue(eString, val, strlen(val)+1);
    m_isDirty = true;
}

bool MSaveFileImpl::getInt(const char* key, int& val)
{  
    if(m_values.find(key) == m_values.end()) return false;
    if(m_values[key]->type != eInt) return false;

    val = *(int*)(m_values[key]->value);

    return true;
}

bool MSaveFileImpl::getFloat(const char* key, float& val)
{
    if(m_values.find(key) == m_values.end()) return false;
    if(m_values[key]->type != eFloat) return false;

    val = *(float*)(m_values[key]->value);

    return true;
}

bool MSaveFileImpl::getString(const char* key, char* val)
{
    if(m_values.find(key) == m_values.end()) return false;
    if(m_values[key]->type != eString) return false;

    memcpy(val, m_values[key]->value, strlen((char*)m_values[key]->value));

    return true;
}

bool MSaveFileImpl::hasKey(const char* key)
{
    return m_values.find(key) != m_values.end();
}

void MSaveFileImpl::save()
{
    if(!m_isDirty) return;

    if(m_mode == M_SAVE_FILE_MODE_TEXT)
        saveXML();
    else
        saveBinary();
}

void MSaveFileImpl::load()
{
    if(loadXML() || loadBinary())
        m_isDirty = false;
    else // failed, so make sure we save next time
        m_isDirty = true;
}

bool MSaveFileImpl::loadXML()
{
    TiXmlDocument file(m_filename);
    
    if(!file.LoadFile()) return false;

    TiXmlHandle hDoc(&file);
    TiXmlElement* rootNode;
    TiXmlHandle hRoot(0);

    rootNode = hDoc.FirstChildElement().Element();

    if(!rootNode) return false;
    if(strcmp(rootNode->Value(), "Maratis") != 0) return false;
    // todo: Add versioning in the root node

    string path = "";
    xmlAddElement(rootNode->FirstChildElement(), path);

    if(m_mode == M_SAVE_FILE_MODE_ANY)
        m_mode = M_SAVE_FILE_MODE_TEXT;
     
    return true;
}

bool MSaveFileImpl::loadBinary()
{
    return false;
}

void MSaveFileImpl::saveXML()
{
    TiXmlDocument doc;

    TiXmlElement* root = new TiXmlElement("Maratis");
    doc.LinkEndChild(root);

    for(std::map<std::string, _MSaveValue*>::iterator iVal = m_values.begin();
        iVal != m_values.end();
        ++iVal)
    {
        TiXmlElement* elem = xmlGetOrCreateElement(root, iVal->first);

        char value[256];
        switch(iVal->second->type)
        {
            case eInt:
                sprintf(value, "%d", *(int*)iVal->second->value);
                elem->SetAttribute("type", "int");
                elem->SetAttribute("value", value);
            break;
            case eFloat:
                sprintf(value, "%f", *(float*)iVal->second->value);
                elem->SetAttribute("type", "float");
                elem->SetAttribute("value", value);
            break;
            case eString:
                elem->SetAttribute("type", "string");
                elem->SetAttribute("value", (char*)iVal->second->value);
            break;
        }
    }

    doc.SaveFile(m_filename);
}

void MSaveFileImpl::saveBinary()
{

}

void MSaveFileImpl::xmlAddElement(TiXmlElement* elem, string path)
{
    if(elem == NULL) return;
    string thisPath = path + elem->Value();

    const char* attrType = elem->Attribute("type");
    if(attrType)
    {
        string type = attrType;
        if(type == "int")
            setInt(thisPath.c_str(), atoi(elem->Attribute("value")));
        else if(type == "float")
            setFloat(thisPath.c_str(), atof(elem->Attribute("value")));
        else if(type == "string")
            setString(thisPath.c_str(), elem->Attribute("value"));
    }
    
    xmlAddElement(elem->FirstChildElement(), thisPath + ".");
    xmlAddElement(elem->NextSiblingElement(), path);
}

TiXmlElement* MSaveFileImpl::xmlGetOrCreateElement(TiXmlElement* parent, string path)
{
    if(!parent) return NULL;
    if(path.length() == 0) return parent;
    size_t i = path.find_first_of(".");
    bool next = true;
    string elemName;
    if(i == string::npos) 
    {
       elemName = path;
       next = false;
    }
    else
        elemName = path.substr(0, i);
    
    TiXmlElement* elem = parent->FirstChildElement(elemName.c_str());
    if(!elem)
    {
        elem = new TiXmlElement(elemName.c_str());
        parent->LinkEndChild(elem);
    }
    if(next)
        return xmlGetOrCreateElement(elem, path.substr(i+1).c_str());
    return elem;
}
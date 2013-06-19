#ifndef _M_SAVE_FILE_IMPL_H
#define _M_SAVE_FILE_IMPL_H

//#include <MCore.h>
#include <MSaveFile.h>

#include <map>
#include <string>
#include <tinyxml.h>

using std::string;

typedef struct _MSaveValue MSaveValue;

class MSaveFileImpl : public MSaveFile
{
public:
    MSaveFileImpl(const char* filename, MSaveFileMode mode);
    ~MSaveFileImpl();

    static MSaveFile* getNew(const char* filename, MSaveFileMode mode);
    void destroy();

private:
    char* m_filename;
    std::map<std::string, _MSaveValue*> m_values;
    bool                                m_isDirty;
    MSaveFileMode                       m_mode;

public:
    void setInt(const char* key, const int val);
    void setFloat(const char* key, const float val);
    void setString(const char* key, const char* val);

    bool getInt(const char* key, int& val);
    bool getFloat(const char* key, float& val);
    bool getString(const char* key, char* val);

    bool hasKey(const char* key);

    void save();
    void load();

private:
    bool loadXML();
    bool loadBinary();

    void saveXML();
    void saveBinary();

    void xmlAddElement(TiXmlElement* elem, string path);
    TiXmlElement* xmlGetOrCreateElement(TiXmlElement* parent, string path);
};

#endif/*_M_SAVE_FILE_IMPL_H*/

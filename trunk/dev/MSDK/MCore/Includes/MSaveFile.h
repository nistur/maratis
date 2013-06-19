#ifndef _M_SAVE_FILE_H
#define _M_SAVE_FILE_H

enum MSaveFileMode
{
    M_SAVE_FILE_MODE_BINARY,
    M_SAVE_FILE_MODE_TEXT,
    M_SAVE_FILE_MODE_ANY
};

class MSaveFile
{
public:
    virtual ~MSaveFile() {}
    
    virtual void setInt(const char* key, const int val) = 0;
    virtual void setFloat(const char* key, const float val) = 0;
    virtual void setString(const char* key, const char* val) = 0;

    virtual bool getInt(const char* key, int& val) = 0;
    virtual bool getFloat(const char* key, float& val) = 0;
    virtual bool getString(const char* key, char* val) = 0;

    virtual bool hasKey(const char* key) = 0;

    virtual void save() = 0;
    virtual void load() = 0;

    virtual void destroy() = 0;
};

typedef MSaveFile*(*newSaveFileFactory)(const char* filename, MSaveFileMode mode);

#endif/*_M_SAVE_FILE_H*/

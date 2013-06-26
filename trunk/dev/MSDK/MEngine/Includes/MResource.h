#ifndef __M_RESOURCE_H__
#define __M_RESOURCE_H__


/*------------------------------------------------------------------------------
 * MResource
 * base class for all resource types, usually found in plugins
 *----------------------------------------------------------------------------*/
class M_ENGINE_EXPORT MResource
{
/*------------------------------------------------------------------------------
 * static interface
 *----------------------------------------------------------------------------*/
public:
    static MResource* getNew(const char* type);

    typedef MResource*(*resourceFactory)();
    static void registerFactory(const char* type, resourceFactory factory);
    static void unregisterFactory(const char* type, resourceFactory factory);

/*------------------------------------------------------------------------------
 * abstract interface
 *----------------------------------------------------------------------------*/
public:
    virtual void destroy() = 0;
};

#endif/*__M_RESOURCE_H__*/
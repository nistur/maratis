#include "MEngine.h"
#include "MResource.h"

#include <map>
#include <string>

using std::map;
using std::string;

// I don't want to expose this in MResource.h but I feel dirty making it a global :(
typedef map<string, MResource::resourceFactory> factoryMap;
typedef factoryMap::iterator                    factoryMapIter;

factoryMap g_factories;

MResource* MResource::getNew(const char* type)
{
    factoryMapIter iFactory = g_factories.find(type);
    if(iFactory == g_factories.end()) return NULL;

    return iFactory->second();
}

void MResource::registerFactory(const char* type, resourceFactory factory)
{
    g_factories[type] = factory;
}

void MResource::unregisterFactory(const char* type, resourceFactory factory)
{
    factoryMapIter iFactory = g_factories.find(type);
    if(iFactory == g_factories.end() ||
        iFactory->second != factory)
        return;

    g_factories.erase(iFactory);
}
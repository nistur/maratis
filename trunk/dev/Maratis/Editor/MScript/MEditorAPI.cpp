#include "MEditorAPI.h"
#include "MEngine.h"

#include "MPackageManager.h"

int Editor_IsEditor()
{
	MScriptContext* script = MEngine::getInstance()->getScriptContext();
	// this is running in the editor 
	script->pushBoolean(true);
	return 1;
}

int Editor_OpenPackage()
{
	MScriptContext* script = MEngine::getInstance()->getScriptContext();
	MSystemContext* system = MEngine::getInstance()->getSystemContext();
	MPackageManager* packager = MEngine::getInstance()->getPackageManager();

	string filename = "published/";
	filename += script->getString(0);
	char globalFilename[256];
	getGlobalFilename(globalFilename, system->getWorkingDirectory(), filename.c_str());


	MPackage package = packager->openPackage(globalFilename);
	script->pushPointer(package);
	return 1;
}

int Editor_ClosePackage()
{
	MScriptContext* script = MEngine::getInstance()->getScriptContext();
	MPackageManager* packager = MEngine::getInstance()->getPackageManager();

	MPackage package = (MPackage)script->getPointer(0);
	packager->closePackage(package);
	return 0;
}

int Editor_PackageAddFile()
{
	MScriptContext* script = MEngine::getInstance()->getScriptContext();
	MSystemContext* system = MEngine::getInstance()->getSystemContext();
	MPackageManager* packager = MEngine::getInstance()->getPackageManager();

	MPackage package = (MPackage)script->getPointer(0);
	const char* filename = script->getString(1);

	char globalFilename[256];
	getGlobalFilename(globalFilename, system->getWorkingDirectory(), filename);

	packager->addFileToPackage(globalFilename, package, filename);

	return 0;
}
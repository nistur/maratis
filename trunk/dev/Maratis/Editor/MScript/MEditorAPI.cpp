#include "MEditorAPI.h"
#include "MEngine.h"

#include "MPackageManager.h"

const char* getProjName()
{
	static char projName[256] = "";
	if(strlen(projName) > 0)
		return projName;

	MSystemContext* system = MEngine::getInstance()->getSystemContext();

	vector<string> files;
	readDirectory(system->getWorkingDirectory(), &files);
	for(vector<string>::iterator iFile = files.begin();
		iFile != files.end();
		iFile++)
	{
		int ext = iFile->find(".mproj");
		if(ext != string::npos)
		{
			sprintf(projName, "%s", iFile->substr(0, ext).c_str());
			return projName;
		}
	}
	return NULL;
}

int Editor_IsEditor()
{
	MScriptContext* script = MEngine::getInstance()->getScriptContext();
	// this is running in the editor 
	script->pushBoolean(true);
	return 1;
}

int Editor_GetProjectName()
{
	MScriptContext* script = MEngine::getInstance()->getScriptContext();

	const char* projName = getProjName();
	if(projName)
	{
		script->pushString(projName);
		return 1;
	}
	return 0;
}

int Editor_OpenPackage()
{
	MScriptContext* script = MEngine::getInstance()->getScriptContext();
	MSystemContext* system = MEngine::getInstance()->getSystemContext();
	MPackageManager* packager = MEngine::getInstance()->getPackageManager();

	string filename = "published/";

#ifdef __APPLE__
	filename += getProjName();
	filename += ".app/Contents/Resources/";
#endif

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
#include "MPlayerAPI.h"
#include "MEngine.h"

int Player_IsEditor()
{
	MScriptContext* script = MEngine::getInstance()->getScriptContext();
	// this is not running in the editor 
	script->pushBoolean(false);
	return 1;
}
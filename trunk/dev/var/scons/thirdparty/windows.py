# coding: utf-8
# define the Windows library include/obj/link flags for the various platforms
# 2011-02-06, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2012-10-25 18:46:26 +0100 (Thu, 25 Oct 2012) $
# $LastChangedBy: skaiware@gmail.com $


import sys

def getWindowsParameters():
    """get platform dependent parameters"""
    # variables
    params = dict()
    params['defines']     = []
    params['objs']        = []
    params['libs']        = []
    params['includePath'] = []
    params['libPath']     = []
    params['frameworks']  = []
    
    # fill needed params for each supported platform
    # common defs

    # platform specific
    if sys.platform=='win32' or sys.platform=='cygwin':
        # Windows settings for win32
		#   winmm : needed for all joyXXX functions...
		# 	Comdlg32 : needed for GetOpenFileName,...
		#   Gdi32 : needed for SwapBuffer,...
		#	crtdll : needed for __commit used by npk_dev
		# Seems un useful : 'glaux' 'Shell32', 'User32'...
        params['libs'] = 'User32 Shell32 Gdi32 Comdlg32 Winmm'.split()
        pass
    elif sys.platform=='darwin':
        # Windows settings for osx
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # Windows settings for linux
        pass
    
    return params


def addWindowsToEnv(env):
    """ add Windows parameters to the build environment"""
    # retrieve params
    params = getWindowsParameters()
    # append Windows specific params to the build environment
    env.AppendUnique(CPPPATH = params['includePath'])
    env.AppendUnique(LIBPATH = params['libPath'])
    env.AppendUnique(LIBS = params['libs'])
    env.AppendUnique(FRAMEWORKS = params['frameworks'])
    pass


if __name__ == '__main__':
    params = getWindowsParameters()
    print '  --- Values ---'
    print 'Windows Defines:      ' + str(params['defines'])
    print 'Windows Objs:         ' + str(params['objs'])
    print 'Windows Include Path: ' + str(params['includePath'])
    print 'Windows Lib Path:     ' + str(params['libPath'])
    print 'Windows Libs:         ' + str(params['libs'])
    print 'Windows Frameworks:   ' + str(params['frameworks'])


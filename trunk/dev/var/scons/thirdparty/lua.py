# coding: utf-8
# define the Lua library include/obj/link flags for the various platforms
# 2011-02-06, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2011-09-14 11:12:57 +0100 (Wed, 14 Sep 2011) $
# $LastChangedBy: anael.seghezzi@gmail.com $


import sys, os

def getLuaParameters():
    """get platform dependent parameters"""
    # variables
    params = dict()
    params['defines']     = []
    params['objs']        = []
    params['libs']        = []
    params['includePath'] = []
    params['libPath']     = []
    
    # fill needed params for each supported platform
    # common defs
    params['includePath'].append('lua')
    params['libPath'].append('3rdparty/lua')
    params['libs'].append('lua')

    # platform specific
    if sys.platform=='win32':
        # Lua settings for win32
        pass
    elif sys.platform=='darwin':
        # Lua settings for osx
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # Lua settings for linux
        pass
    
    return params


def addLuaToEnv(env):
    """ add Lua parameters to the build environment"""
    # retrieve params
    params = getLuaParameters()
    # convert includepath to the complete 3rdparty dir
    vincludepath = []
    for pth in params['includePath']:
        vincludepath.append(os.path.join(env['thirdpartydir'],pth))
    # convert libpath to the corresponding variant dir
    vlibpath = []
    for pth in params['libPath']:
        buildpath = os.path.join(env['builddir'],pth)
        vlibpath.append(buildpath)
    # append specific params to the build environment
    env.AppendUnique(CPPPATH = vincludepath)
    env.AppendUnique(LIBPATH = vlibpath)
    env.AppendUnique(LIBS = params['libs'])
    pass


if __name__ == '__main__':
    params = getLuaParameters()
    print '  --- Values ---'
    print 'Lua Defines:      ' + str(params['defines'])
    print 'Lua Objs:         ' + str(params['objs'])
    print 'Lua Include Path: ' + str(params['includePath'])
    print 'Lua Lib Path:     ' + str(params['libPath'])
    print 'Lua Libs:         ' + str(params['libs'])


# coding: utf-8
# define the assimp library include/obj/link flags for the various platforms


import sys, os

def getAssimpParameters():
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
    params['includePath'].append('assimp/include')
    params['includePath'].append('assimp/code/BoostWorkaround')
    params['libPath'].append('3rdparty/assimp')
    params['libs'].append('assimp')
    params['defines'].append('ASSIMP_BUILD_BOOST_WORKAROUND')
    params['defines'].append('ASSIMP_BUILD_NO_OWN_ZLIB')

    # platform specific
    if sys.platform=='win32':
        # settings for win32
        pass
    elif sys.platform=='darwin':
        # settings for osx
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # settings for linux
        pass
    
    return params


def addAssimpToEnv(env):
    """ add parameters to the build environment"""
    # retrieve params
    params = getAssimpParameters()
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
    env.AppendUnique(CPPDEFINES = params['defines'])
    env.AppendUnique(LIBS = params['libs'])

    pass


if __name__ == '__main__':
    params = getAssimpParameters()
    print '  --- Values ---'
    print 'Assimp Defines:      ' + str(params['defines'])
    print 'Assimp Objs:         ' + str(params['objs'])
    print 'Assimp Include Path: ' + str(params['includePath'])
    print 'Assimp Lib Path:     ' + str(params['libPath'])
    print 'Assimp Libs:         ' + str(params['libs'])


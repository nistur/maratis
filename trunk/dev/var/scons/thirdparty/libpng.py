# coding: utf-8
# define the LibPng library include/obj/link flags for the various platforms
# 2011-02-06, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2011-09-14 11:12:57 +0100 (Wed, 14 Sep 2011) $
# $LastChangedBy: anael.seghezzi@gmail.com $


import sys, os

def getLibPngParameters():
    """get platforma dependent parameters"""
    # variables
    params = dict()
    params['defines']     = []
    params['objs']        = []
    params['libs']        = []
    params['includePath'] = []
    params['libPath']     = []
    
    # fill needed params for each supported platform
    # common defs
    params['includePath'].append('libpng')
    params['libPath'].append('3rdparty/libpng')
    params['libs'].append('png')

    # platform specific
    if sys.platform=='win32':
        # LibPng settings for win32
        pass
    elif sys.platform=='darwin':
        # LibPng settings for osx
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # LibPng settings for linux
        pass
    
    return params


def addLibPngToEnv(env):
    """ add LibPng parameters to the build environment"""
    # retrieve params
    params = getLibPngParameters()
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
    params = getLibPngParameters()
    print '  --- Values ---'
    print 'LibPng Defines:      ' + str(params['defines'])
    print 'LibPng Objs:         ' + str(params['objs'])
    print 'LibPng Include Path: ' + str(params['includePath'])
    print 'LibPng Lib Path:     ' + str(params['libPath'])
    print 'LibPng Libs:         ' + str(params['libs'])


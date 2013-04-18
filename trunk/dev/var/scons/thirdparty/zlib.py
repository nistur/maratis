# coding: utf-8
# define the Zlib library include/obj/link flags for the various platforms
# 2011-02-11, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2011-09-14 11:12:57 +0100 (Wed, 14 Sep 2011) $
# $LastChangedBy: anael.seghezzi@gmail.com $


import sys, os

def getZlibParameters():
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
    params['includePath'].append('zlib')
    params['libPath'].append('3rdparty/zlib')
    params['libs'].append('zlib')

    # platform specific
    if sys.platform=='win32':
        # Zlib settings for win32
        pass
    elif sys.platform=='darwin':
        # Zlib settings for osx
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # Zlib settings for linux
        pass
    
    return params


def addZlibToEnv(env):
    """ add Zlib parameters to the build environment"""
    # retrieve params
    params = getZlibParameters()
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
    params = getZlibParameters()
    print '  --- Values ---'
    print 'Zlib Defines:      ' + str(params['defines'])
    print 'Zlib Objs:         ' + str(params['objs'])
    print 'Zlib Include Path: ' + str(params['includePath'])
    print 'Zlib Lib Path:     ' + str(params['libPath'])
    print 'Zlib Libs:         ' + str(params['libs'])


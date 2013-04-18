# coding: utf-8
# define the Dev-IL library include/obj/link flags for the various platforms
# 2011-02-06, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2011-09-14 11:12:57 +0100 (Wed, 14 Sep 2011) $
# $LastChangedBy: anael.seghezzi@gmail.com $


import sys, os

def getDevilParameters():
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
    params['defines'].append('IL_STATIC_LIB')
    params['includePath'].append('devil')
    params['libPath'].append('3rdparty/devil')
    params['libs'].append('il')

    # platform specific
    if sys.platform=='win32':
        # devil settings for win32
        pass
    elif sys.platform=='darwin':
        # devil settings for osx
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # devil settings for linux
        pass
    
    return params


def addDevilToEnv(env):
    """ add devil parameters to the build environment"""
    # retrieve params
    params = getDevilParameters()
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
    params = getDevilParameters()
    print '  --- Values ---'
    print 'devil Defines:      ' + str(params['defines'])
    print 'devil Objs:         ' + str(params['objs'])
    print 'devil Include Path: ' + str(params['includePath'])
    print 'devil Lib Path:     ' + str(params['libPath'])
    print 'devil Libs:         ' + str(params['libs'])


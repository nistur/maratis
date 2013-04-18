# coding: utf-8
# define the FreeType library include/obj/link flags for the various platforms
# 2011-02-06, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2011-09-14 11:12:57 +0100 (Wed, 14 Sep 2011) $
# $LastChangedBy: anael.seghezzi@gmail.com $


import sys, os

def getFreeTypeParameters():
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
    params['includePath'].append('freetype/include')
    params['includePath'].append('freetype/include/freetype')
    params['libPath'].append('3rdparty/freetype')
    params['libs'].append('freetype')

    # platform specific
    if sys.platform=='win32':
        # FreeType settings for win32
        pass
    elif sys.platform=='darwin':
        # FreeType settings for osx
        params['frameworks'] = 'Cocoa'
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # FreeType settings for linux
        pass
    
    return params


def addFreetypeToEnv(env):
    """ add FreeType parameters to the build environment"""
    # retrieve params
    params = getFreeTypeParameters()
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
    env.AppendUnique(FRAMEWORKS = params['frameworks'])
    pass


if __name__ == '__main__':
    params = getFreeTypeParameters()
    print '  --- Values ---'
    print 'FreeType Defines:      ' + str(params['defines'])
    print 'FreeType Objs:         ' + str(params['objs'])
    print 'FreeType Include Path: ' + str(params['includePath'])
    print 'FreeType Lib Path:     ' + str(params['libPath'])
    print 'FreeType Libs:         ' + str(params['libs'])


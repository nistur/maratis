# coding: utf-8
# define the NPK package library include/obj/link flags for the various platforms


import sys, os

def getNPKParameters():
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
    params['includePath'].append('npk/include')
    params['libs'].append('npk')
    params['libPath'].append('3rdparty/npk/')

    # platform specific
    if sys.platform=='win32':
        # npk settings for win32
        pass
    elif sys.platform=='darwin':
        # npk settings for osx
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # npk settings for linux
        pass
    
    return params


def addNPKToEnv(env):
    """ add npk parameters to the build environment"""
    # retrieve params
    params = getNPKParameters()
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
    params = getNPKParameters()
    print '  --- Values ---'
    print 'npk Defines:      ' + str(params['defines'])
    print 'npk Objs:         ' + str(params['objs'])
    print 'npk Include Path: ' + str(params['includePath'])
    print 'npk Lib Path:     ' + str(params['libPath'])
    print 'npk Libs:         ' + str(params['libs'])


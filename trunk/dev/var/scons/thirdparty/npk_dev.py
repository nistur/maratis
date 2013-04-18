# coding: utf-8
# define the NPK package library include/obj/link flags for the various platforms -dev lib, includes compression


import sys, os

def getNPKDevParameters():
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
    params['libPath'].append('3rdparty/npk/')
    params['defines'].append('M_PACKAGE_WRITABLE')

    # platform specific
    if sys.platform=='win32' or sys.platform=='cygwin':
        # npk settings for win32
        params['libs'].append('npk_dev')
        pass
    elif sys.platform=='darwin':
        # npk settings for osx
        params['libs'].append('libnpk_dev')
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # npk settings for linux
        params['libs'].append('libnpk_dev')
        pass
    
    return params


def addNPKDevToEnv(env):
    """ add npk parameters to the build environment"""
    # retrieve params
    params = getNPKDevParameters()
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
    params = getNPKDevParameters()
    print '  --- Values ---'
    print 'npk Defines:      ' + str(params['defines'])
    print 'npk Objs:         ' + str(params['objs'])
    print 'npk Include Path: ' + str(params['includePath'])
    print 'npk Lib Path:     ' + str(params['libPath'])
    print 'npk Libs:         ' + str(params['libs'])


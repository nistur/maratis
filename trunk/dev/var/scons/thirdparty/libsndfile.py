# coding: utf-8
# define the LibSndFile library include/obj/link flags for the various platforms
# 2011-02-06, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2012-09-05 21:17:54 +0100 (Wed, 05 Sep 2012) $
# $LastChangedBy: skaiware@gmail.com $


import sys, os

def getLibSndFileParameters():
    """get platforma dependent parameters"""
    # variables
    params = dict()
    params['defines']     = []
    params['objs']        = []
    params['libs']        = []
    params['installLibs'] = []
    params['includePath'] = []
    params['libPath']     = []
    
    # fill needed params for each supported platform
    # common defs
    params['includePath'].append('libsndfile/include')

    # platform specific
    if sys.platform=='win32':
        # settings for win32
        params['libPath'].append('libsndfile/win32')
        params['libs'].append('libsndfile-1')
        params['installLibs'].append('libsndfile-1.dll')
        pass
    elif sys.platform=='darwin':
        # settings for osx
        params['libPath'].append('libsndfile/osx')
        params['libs'].append('SndFile')
        params['installLibs'].append('libSndFile.dylib')
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # settings for linux
        params['libPath'].append('libsndfile/linux')
        params['libs'].append('sndfile')
        params['installLibs'].append('libsndfile.so')
        pass
    elif sys.platform=='cygwin':
		# settings for cygwin : very close to linux
		params['libPath'].append('libsndfile/cygwin')
		params['libs'].append('sndfile')
		# todo : add the cygwin binaries in thirdparty ?
		# perhaps not : libsndfile is available in cygwin repositories. Just install it as all usual system libs.
		#params['installLibs'].append('libsndfile.dll')
		pass
    else:
        raise Exception('Unknown platform')
    
    return params


def addLibSndFileToEnv(env):
    """ add LibSndFile parameters to the build environment"""
    # retrieve params
    params = getLibSndFileParameters()
    # convert includepath to the complete 3rdparty dir
    vincludepath = []
    for pth in params['includePath']:
        vincludepath.append(os.path.join(env['thirdpartydir'],pth))
    # convert libpath to the corresponding dir
    vlibpath = []
    for pth in params['libPath']:
        buildpath = os.path.join(env['thirdpartydir'],pth)
        vlibpath.append(buildpath)
    # append specific params to the build environment
    env.AppendUnique(CPPPATH = vincludepath)
    env.AppendUnique(LIBPATH = vlibpath)
    env.AppendUnique(LIBS = params['libs'])
    pass


def getLibSndFileLibs(env):
    """ get LibSndFile libraries with full path"""
    # retrieve params
    params = getLibSndFileParameters()
    # get full path of install libs: only the first libpath is used!!
    vlibpath = []
    for lib in params['installLibs']:
        libpath = os.path.join(env['thirdpartydir'],params['libPath'][0],lib)
        vlibpath.append(libpath)
    return vlibpath


if __name__ == '__main__':
    params = getLibSndFileParameters()
    print '  --- Values ---'
    print 'LibSndFile Defines:      ' + str(params['defines'])
    print 'LibSndFile Objs:         ' + str(params['objs'])
    print 'LibSndFile Include Path: ' + str(params['includePath'])
    print 'LibSndFile Lib Path:     ' + str(params['libPath'])
    print 'LibSndFile Libs:         ' + str(params['libs'])


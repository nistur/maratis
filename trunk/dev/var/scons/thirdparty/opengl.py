# coding: utf-8
# define the OpenGL library include/obj/link flags for the various platforms
# 2011-02-06, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2012-09-05 21:17:54 +0100 (Wed, 05 Sep 2012) $
# $LastChangedBy: skaiware@gmail.com $


import sys

def getOpenGLParameters():
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
    if sys.platform=='win32':
        # OpenGL settings for win32
        params['libs'] = 'Opengl32'
        pass
    elif sys.platform=='darwin':
        # OpenGL settings for osx
        params['frameworks'] = 'OpenGL'
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # OpenGL settings for linux
        pass
    elif sys.platform=='cygwin':
        #params['libs'] = 'GL.dll'  # cygwin real opengl GL for X11 (lib/libGL.dll.a)
        params['libs'] = 'opengl32' # cygwin WIN32 openGL (lib/w32api/libopengl32.a)
        pass

    return params


def addOpenGLToEnv(env):
    """ add OpenGL parameters to the build environment"""
    # retrieve params
    params = getOpenGLParameters()
    # append OpenGL specific params to the build environment
    env.AppendUnique(CPPPATH = params['includePath'])
    env.AppendUnique(LIBPATH = params['libPath'])
    env.AppendUnique(LIBS = params['libs'])
    env.AppendUnique(FRAMEWORKS = params['frameworks'])
    pass


if __name__ == '__main__':
    params = getOpenGLParameters()
    print '  --- Values ---'
    print 'OpenGL Defines:      ' + str(params['defines'])
    print 'OpenGL Objs:         ' + str(params['objs'])
    print 'OpenGL Include Path: ' + str(params['includePath'])
    print 'OpenGL Lib Path:     ' + str(params['libPath'])
    print 'OpenGL Libs:         ' + str(params['libs'])
    print 'OpenGL Frameworks:   ' + str(params['frameworks'])


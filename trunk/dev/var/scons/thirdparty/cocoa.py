# coding: utf-8
# define the Cocoa library include/obj/link flags for the various platforms
# 2011-02-06, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2011-09-14 11:12:57 +0100 (Wed, 14 Sep 2011) $
# $LastChangedBy: anael.seghezzi@gmail.com $


import sys

def getCocoaParameters():
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
        # Cocoa settings for win32
        pass
    elif sys.platform=='darwin':
        # Cocoa settings for osx
        params['frameworks'] = 'Cocoa'
        pass
    elif sys.platform=='linux2' or sys.platform=='linux3':
        # Cocoa settings for linux
        pass
    
    return params


def addCocoaToEnv(env):
    """ add Cocoa parameters to the build environment"""
    # retrieve params
    params = getCocoaParameters()
    # append Cocoa specific params to the build environment
    env.AppendUnique(CPPPATH = params['includePath'])
    env.AppendUnique(LIBPATH = params['libPath'])
    env.AppendUnique(LIBS = params['libs'])
    env.AppendUnique(FRAMEWORKS = params['frameworks'])
    pass


if __name__ == '__main__':
    params = getCocoaParameters()
    print '  --- Values ---'
    print 'Cocoa Defines:      ' + str(params['defines'])
    print 'Cocoa Objs:         ' + str(params['objs'])
    print 'Cocoa Include Path: ' + str(params['includePath'])
    print 'Cocoa Lib Path:     ' + str(params['libPath'])
    print 'Cocoa Libs:         ' + str(params['libs'])
    print 'Cocoa Frameworks:   ' + str(params['frameworks'])


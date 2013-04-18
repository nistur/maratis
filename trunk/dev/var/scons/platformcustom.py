# platform specific customizations
# 2011-02-13, Davide Bacchet (davide.bacchet@gmail.com)
# $LastChangedDate: 2013-02-12 11:30:35 +0000 (Tue, 12 Feb 2013) $
# $LastChangedBy: anael.seghezzi@gmail.com $


import sys

def customizeAppleLinker(env):
    env.Append(LINKFLAGS=['-arch','i386','-arch','x86_64','-mmacosx-version-min=10.6'])
    # in osx rpath refers to install_name when used in shared libs, 
    # and to runtime search path when used in executables
    # env.Append(SHLINKFLAGS=['$_SHLIBRPATH'])
    # env['SHLIBRPATHPREFIX'] = '-install_name '
    # env['SHLIBRPATHSUFFIX'] = ''
    # env['_SHLIBRPATH'] = '${_concat(SHLIBRPATHPREFIX, RPATH, SHLIBRPATHSUFFIX, __env__)}'
    env.Append(LINKFLAGS=['$__RPATH'])
    env['RPATHPREFIX'] = '-Wl,-rpath,'
    env['RPATHSUFFIX'] = ''
    env['_RPATH'] = '${_concat(RPATHPREFIX, RPATH, RPATHSUFFIX, __env__)}'
    # for shared libraries assume that the install name is always @rpath/libname.dylib
    env['SHLINKCOM']   = '$SHLINK -o $TARGET -install_name @rpath/${TARGET.file} $SHLINKFLAGS $SOURCES $_LIBDIRFLAGS $_LIBFLAGS'

def customizeMSVCLinker(env):
    env['WINDOWSEXPSUFFIX'] = '.exp'

def embedMSVCManifest(env):
    env['WINDOWS_INSERT_MANIFEST']=1
    env['LINKCOM'] = [env['LINKCOM'], 'mt.exe -nologo -manifest ${TARGET}.manifest -outputresource:$TARGET;1']
    env['SHLINKCOM'] = [env['SHLINKCOM'], 'mt.exe -nologo -manifest ${TARGET}.manifest -outputresource:$TARGET;2']
    env.AppendUnique(LINKFLAGS = '/MANIFEST')

def customizeEnvironment(env):
    """customize the build evironment"""
    if sys.platform=='darwin':
        customizeAppleLinker(env)
    elif sys.platform=='win32':
        customizeMSVCLinker(env)
        embedMSVCManifest(env)

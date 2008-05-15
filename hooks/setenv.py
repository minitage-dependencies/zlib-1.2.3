import os

from minitage.core.common import append_env_var

os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'

def getzlibenv(options,buildout):
    if uname!='Darwin':
        append_env_var('LDSHARED', ["cc -shared -Wl,-soname,libz.so.1 %s " % os_ldflags, "-Wl,-rpath -Wl,'../lib'", "-Wl,-rpath -Wl,'/lib'", "-Wl,-rpath -Wl,'/usr/lib'" ],sep=' ',before=False)
#    else:
#        append_env_var('LDSHARED', ["cc -shared  %s " % os_ldflags, "-Wl,-rpath -Wl,'../lib'", "-Wl,-rpath -Wl,'/lib'", "-Wl,-rpath -Wl,'/usr/lib'" ],sep=' ',before=False)


# vim:set ts=4 sts=4 et  :

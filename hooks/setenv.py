import os
import zc.buildout


os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'


def appendEnvVar(env,var,sep=":",before=True):
    """ append text to a environnement variable
    @param env String variable to set
    @param before append before or after the variable"""
    for path in var:
    	if before:os.environ[env] = "%s%s%s" % (path,sep,os.environ.get(env,''))
	else:os.environ[env] = "%s%s%s" % (os.environ.get(env,''),sep,path)

def getzlibenv(options,buildout):
    if uname!='Darwin':
        appendEnvVar('LDSHARED', ["cc -shared -Wl,-soname,libz.so.1 %s " % os_ldflags, "-Wl,-rpath -Wl,'../lib'", "-Wl,-rpath -Wl,'/lib'", "-Wl,-rpath -Wl,'/usr/lib'" ],sep=' ',before=False)
#    else:
#        appendEnvVar('LDSHARED', ["cc -shared  %s " % os_ldflags, "-Wl,-rpath -Wl,'../lib'", "-Wl,-rpath -Wl,'/lib'", "-Wl,-rpath -Wl,'/usr/lib'" ],sep=' ',before=False)


# vim:set ts=4 sts=4 et  :


import os


def x64(o, b):
    os.environ['OCFLAGS'] = os.environ['CFLAGS']
    del os.environ['CFLAGS']

def x64r(o, b):
    os.environ['CFLAGS'] = os.environ['OCFLAGS']



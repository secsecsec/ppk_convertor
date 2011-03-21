#!/usr/bin/env python
import sys
import chilkat
from getpass import getpass

def convert_ppk(fname):
    print "Reading: %s" %fname
    pwd = getpass()
    key = chilkat.CkSshKey()
    key.put_Password(pwd)
    key_str = key.loadText(fname)
    if key.FromPuttyPrivateKey(key_str) is not True:
        print "Conversion error"
        print key.lastErrorText()
        sys.exit(1)
    key.put_Password(pwd)
    encrd_key = key.toOpenSshPrivateKey(True)
    result = key.SaveText(encrd_key, fname.replace(".ppk",".pem"))
    if result is not True:
        print "Converted key saving error"
        print key.lastErrorText()
        sys.exit(1)
    return result

if len(sys.argv) == 1 or sys.argv[1] == "--help":
    print "Putty private key (.ppk) -> OpenSSH private key converter"
    print "    Usage: conver.py <file1.ppk> <file2.ppk> ... "
    print "    Warning! .ppk required in file name - it'll be replaced with .pem"

dummy = sys.argv.pop(0)

for fname in sys.argv:
    if convert_ppk(fname):
        print "%s conversiob complete."


#!/usr/bin/env python3

"""
Generate a skeleton source code.

Last update: 2018-06-17 (yyyy-mm-dd)
"""

import os
import sys
import shutil

CWD = os.getcwd()
# if __file__ is a link, realpath returns the path of the pointed file
TEMPLATES = os.path.abspath(os.path.dirname(os.path.realpath(__file__))) + '/' + 'templates'
EXECUTABLE = ['py', 'd']
EDITOR = 'vim'
CODE = 'code .'


def rename(fname):
    dirName, fileName = os.path.split(fname)
    fileExt = os.path.splitext(fileName)[1]
    #
    reply = input("New name of the file (without extension) [ENTER to cancel]: ").strip()
    if reply:
        to_name = dirName + '/' + reply + fileExt
        os.rename(fname, to_name)
        if os.path.isfile(to_name):
            print('# renamed to', os.path.split(to_name)[1])
            return to_name
        else:
            return None
    else:
        return fname


def copy(ext, full_name=None):
    if full_name:
        source = full_name
    else:
        source = 'alap.' + ext
    #
    if os.path.isfile(CWD + '/' + source):
        print('Warning: {} already exists in the current directory.'.format(source), file=sys.stderr)
        sys.exit(1)
    # else
    dest = CWD + '/' + source
    shutil.copyfile(TEMPLATES + '/' + source, dest)
    if os.path.isfile(dest):
        print('# {} is created'.format(source))
        if ext in EXECUTABLE:
            os.chmod(dest, 0o700)
    else:
        print("Warning: couldn't copy {}.".format(source))
        sys.exit(1)    # problem

    return rename(dest)


def edit(fname):
    ch = input("Do you want to edit the file [y/n] (default: y)? ").strip()
    if ch in ('y', ''):
        # os.system('{ed} "{f}"'.format(ed=EDITOR, f=fname))
        os.system(CODE)


def main():
    print("""---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) Go     [go]
3) Java   [java]
4) C      [c]
5) D      [d]
6) Nim    [nim]
q) quit""")
    while True:
        try:
            ch = input('> ')
        except (EOFError, KeyboardInterrupt):
            print()
            ch = 'q'
        if ch in ['1', 'py']:
            return copy('py')
            break
        elif ch in ['2', 'go']:
            return copy('go')
            break
        elif ch in ['3', 'java']:
            return copy('java', full_name='Alap.java')
            break
        elif ch in ['4', 'c']:
            return copy('c')
            break
        elif ch in ['5', 'd']:
            return copy('d')
            break
        elif ch in ['6', 'nim']:
            return copy('nim')
            break
        elif ch == 'q':
            print('bye.')
            sys.exit(0)
        else:
            print('Wat?')

#############################################################################

if __name__ == "__main__":
    fname = main()
    edit(fname)

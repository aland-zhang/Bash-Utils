#!/usr/bin/env python3

"""
py2rtf
======

Author:  Laszlo Szathmary, 2012 (jabba.laci@gmail.com)
Website: http://ubuntuincident.wordpress.com/2012/08/07/insert-syntax-highlighted-source-in-powerpoint/
GitHub:  https://github.com/jabbalaci/Bash-Utils

Transform a python source file to RTF.

What is it good for?
--------------------

You can open the RTF in Word, select it,
then paste into Powerpoint. This way you can have syntax
highlighted sources in your Powerpoint presentations.

Example:
--------

$ py2rtf hello.py       # the output is written to hello.rtf
$ py2rtf -f hello.py    # overwrite hello.rtf if exists

Last update: 2017-01-09 (yyyy-mm-dd)
"""

import os
import sys
from pathlib import Path


def process(args):
    """
    Check arguments, then call pygmentize with the
    appropriate parameters.
    """
    force = '-f' in args
    if force:
        args.remove('-f')
    if len(args) == 0:
        print("Error: the input file is missing.", file=sys.stderr)
        sys.exit(1)
    # else
    in_file = args[0]
    (dirName, fileName) = os.path.split(in_file)
    (fileBaseName, fileExt) = os.path.splitext(fileName)
    out_file = os.path.join(dirName, fileBaseName + '.rtf')
    if not force and os.path.isfile(out_file):
        print("Warning: the file {outf} exists.".format(outf=out_file), file=sys.stderr)
        print("Tip: use the -f option to force overwrite.", file=sys.stderr)
        sys.exit(1)
    # else
    cmd = 'pygmentize -f rtf -o {outf} {inf}'.format(outf=out_file, inf=in_file)
    print('#', cmd)
    #
    os.system(cmd)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: {0} [-f] input.py".format(Path(sys.argv[0]).name), file=sys.stderr)
    else:
        process(sys.argv[1:])

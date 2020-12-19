#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : exutils.py
# Author            : Amar Lakshya <amar.lakshya@protonmail.com>
# Date              : 19.12.2020
# Last Modified Date: 19.12.2020
# Last Modified By  : Amar Lakshya <amar.lakshya@protonmail.com>

import sys
import os

if len(sys.argv) < 2:
    print("USAGE: exutils.py coreutils_version")
    sys.exit(1)

SCRIPT = \
"""mkdir -p build && cd build \
&& wget https://ftp.gnu.org/gnu/coreutils/coreutils-VER.tar.gz \
&& tar -xf coreutils-VER.tar.gz \
&& cd coreutils-VER \
&& patch -p1 < ../../patches/coreutils-SPEC-on-glibc-2.28.patch \
&& ./configure \
&& make -j$(nproc)
"""
VER = float(sys.argv[1])
SCRIPT = SCRIPT.replace("VER", str(VER))
if 5.97 >= VER <= 6.9:
    VER = 5.97
elif 7.2 >= VER <= 8.3:
    VER = 7.2
elif 8.4 >= VER <= 8.12:
    VER = 8.4
elif 8.13 >= VER <= 8.16:
    VER = 8.13
elif 8.18 >= VER <= 8.23:
    VER = 8.18
elif 8.24 >= VER <= 8.29:
    VER = 8.24
elif VER >= 8.30:
    print("NO NEED TO PATCH! so no need to use me :)")
    sys.exit(0)
SCRIPT = SCRIPT.replace("SPEC", str(VER))
os.system(SCRIPT)

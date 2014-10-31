# -*- coding: utf-8 -*-
#
# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we could use relative
# imports, however those only work with the "from .x import y" syntax, meaning
# already imported modules are not detected -- hence we need to use the
# "import x" syntax.
# Our current solution is to prepend the model's directory to sys.path
# Better solutions are welcome!

import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)

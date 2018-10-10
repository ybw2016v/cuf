#!/usr/bin/env python3
from culib import *

a = decodeconf('cufig.ini')
cat=caldog(a)
cat.loadlib('')
cat.cal()

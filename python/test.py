from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import re

s = '"Cats" 1981 Original London Cast'
s = s.replace('"', '\\"')

print(s)
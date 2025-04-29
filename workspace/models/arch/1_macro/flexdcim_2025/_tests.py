import os
import sys

THIS_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MACRO_NAME = os.path.basename(THIS_SCRIPT_DIR)

sys.path.append(os.path.abspath(os.path.join(THIS_SCRIPT_DIR, '..', '..', '..', '..')))

import scripts
from scripts import utils
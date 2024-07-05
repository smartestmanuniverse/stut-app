#coding: utf-8

from copy import deepcopy
import io
import tempfile
import queue
import sys
import subprocess
import os

import sounddevice as sd
import soundfile as sf

# Make sure NumPy is loaded before it is used in the callback
# with a alias 'np' and a alias 'numpy'
import numpy as np, numpy

assert numpy  # avoid "imported but unused" message (W0611)
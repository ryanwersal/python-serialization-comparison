#!/usr/bin/env python2

from cStringIO import StringIO
from decimal import Decimal

import pickle

# ==============================================================================
def serialize(data):
	io = StringIO()
	pickle.dump(data, io)

# ==============================================================================
def deserialize(data):
	pass

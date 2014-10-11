#!/usr/bin/env python2

from cStringIO import StringIO
from decimal import Decimal

import cPickle

# ==============================================================================
def serialize(data):
	io = StringIO()
	cPickle.dump(data, io)

# ==============================================================================
def deserialize(data):
	pass

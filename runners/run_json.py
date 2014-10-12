#!/usr/bin/env python2

from cStringIO import StringIO
from decimal import Decimal

import json

# ==============================================================================
def handle_unkown_type(obj):
	if isinstance(obj, Decimal):
		return str(obj)
	raise TypeError()

# ==============================================================================
def serialize(data):
	io = StringIO()
	json.dump(data, io, default=handle_unkown_type)
	return io

# ==============================================================================
def deserialize(data):
	pass

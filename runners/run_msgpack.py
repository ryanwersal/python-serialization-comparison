#!/usr/bin/env python2

from cStringIO import StringIO
from decimal import Decimal

import msgpack

# ==============================================================================
def handle_unkown_type(obj):
	if isinstance(obj, Decimal):
		return str(obj)
	raise TypeError()

# ==============================================================================
def serialize(data):
	io = StringIO()
	result = msgpack.packb(data, default=handle_unkown_type)
	io.write(result)

# ==============================================================================
def deserialize(data):
	pass

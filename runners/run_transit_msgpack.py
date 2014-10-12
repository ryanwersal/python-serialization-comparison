#!/usr/bin/env python2

from cStringIO import StringIO
from decimal import Decimal

from transit.writer import Writer
from transit.reader import Reader

from transit_helpers import DecimalWriteHandler, DecimalReadHandler

# ==============================================================================
def serialize(data):
	io = StringIO()
	writer = Writer(io, "msgpack")
	writer.register(Decimal, DecimalWriteHandler)
	writer.write(data)
	return io

# ==============================================================================
def deserialize(data):
	pass

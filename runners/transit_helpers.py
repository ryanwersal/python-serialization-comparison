from decimal import Decimal

# ==============================================================================
class DecimalWriteHandler(object):
	@staticmethod
	def tag(d):
		return "z" if d.is_nan() or d.is_infinite() else "D"
	@staticmethod
	def rep(d):
		if d.is_nan():
			return "NaN"
		if d.is_infinite():
			return "INF"
		return str(d)
	@staticmethod
	def string_rep(d):
		return str(d)

# ==============================================================================
class DecimalReadHandler(object):
	@staticmethod
	def from_rep(v):
		return Decimal(v)

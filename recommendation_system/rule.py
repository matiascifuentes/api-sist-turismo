class Rule(object):

	def __init__(self, lhs, rhs, support, confidence, lift):
		self.lhs = lhs
		self.rhs = rhs
		self.support = support
		self.confidence = confidence
		self.lift = lift

	def json(self):
		return {
            'lhs': self.lhs,
            'rhs': self.rhs,
            'support': self.support,
            'confidence': self.confidence,
            'lift': self.lift
        }

		
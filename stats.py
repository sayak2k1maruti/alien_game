class Stats():
	"""docstring for Stats"""
	def __init__(self, setting):
		self.setting = setting
		self.ship_left = setting.ship_limit
		self.gameActive = False
		self.reset()
		self.score = 0
	def reset(self):
		self.ship_left = self.setting.ship_limit
		self.score = 0
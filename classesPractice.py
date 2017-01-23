class className:
	# Every method needs to first take the paramater 'self'	
	def createName(self, name):
		self.name = name
	
	def displayName(self):
		return self.name
		
	def saying(self):
		print "hello %s" % self.name
		
	
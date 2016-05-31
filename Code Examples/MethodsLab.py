class Kangaroo(object):
	def __init__(self,pouch_contents):
		self.pouch_contents = pouch_contents
		pouch_contents = []
	def __put_in_pouch__(self):
		pouch_contents.append(self)
	def __str__(self):
		# return str(Kangaroo)
		return str(self.pouch_contents)

kanga = Kangaroo("roo")

print kanga
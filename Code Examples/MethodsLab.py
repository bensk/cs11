class Kangaroo(object):
	def __init__(self,name,pouch_contents):
		self.name = name
		self.pouch_contents = []
	def __put_in_pouch__(self,things):
		self.pouch_contents.append(things)


    # def __put_in_pouch__(self,other):
    #     Kangaroo.pouch_contents.append(other)
    #
    # def __str__(self):
    #     # return str(Kangaroo)
    #     return str(self.pouch_contents)
justin = Kangaroo("justin","")
print justin.pouch_contents
# print kanga.pouch_contents()

justin.__put_in_pouch__("something")
justin.__put_in_pouch__("another thing")
print justin.pouch_contents

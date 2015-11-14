import ex40_mystuff

# not sure why this isn't working
class SomeStuff(object):
  def __init__(self):
		self.tangerine = "And now a thousand years between"
	def apples(self):
		print "I AM CLASSY APPLES!"

mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']

ex40_mystuff.apple()

print ex40_mystuff.tangerine

thing = SomeStuff()
thing.apple()
print thing.tangerine


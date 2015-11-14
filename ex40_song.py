class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

not_suable_version = "Happy birthday to you","I don't want to get sued","I'll stop right here."

happy_bday = Song(not_suable_version)

bulls_on_parade = Song(["They rally around tha family",
											  "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

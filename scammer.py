
#!/usr/bin/env python
import os
import random
import time


class Scammer:

	def __init__(self, scam_file, voices, init_wait, min_wait, max_wait, repeat_ct):
		'''
		 	Initializes a Scammer object according to the following arguments:

		 		@scam_file  --> A .txt file holding sayings separated by newlines.

		 		@voices     --> A Python list of voices, as strings.

		 		@init_wait  --> How long to wait before the first saying, in 
		 						minutes.

		 		@min_wait   --> After the first saying, the bottom-end of the wait 
		 						time range, in minutes.

		 		@max_wait   --> After the first saying, the top-end of the wait time
		 						range, in minutes.

		 		@repeat_ct  --> How many times to repeat a saying. Once the count 
		 						runs out, the saying is removed from the list and
		 						will not be said again.
		'''
		self.init_wait = init_wait * 60.0
		self.min_wait = min_wait * 60.0
		self.max_wait = max_wait * 60.0
		self.repeat_ct = repeat_ct

		self.voices = voices
		self.sayings = self.parse_scam_file(scam_file)
		self.sayings_dict = self.dictionaryify(self.sayings)

	def parse_scam_file(self, scam_file):
		'''
			Parsing is an exaggeration; just grabs sayings from the .txt, and
			they are all on their each line so readlines() is sufficient.
		'''	
		with open(scam_file) as f_in:
			self.sayings = f_in.readlines()
		f_in.close() 
		return self.sayings

	def dictionaryify(self, sayings):
		'''
			Convert the @sayings list to a dictionary, where:
				{key, value} == {A saying, how many times to repeat it}

			This is so the count for a saying can be decremented and 
			eventually removed from the list. 

			We'll keep the list around so we can index into with the 
			get_random_saying() method.
			'''
		return dict([(saying, self.repeat_ct) for saying in self.sayings])

	def get_random_voice(self):
		'''
			Randomly index into the 'voices' list and return a voice.
		'''
		print "length of voices: " + str(len(self.voices))
		r = random.randrange(0, len(self.voices))
		print "index: " + str(r)

		return self.voices[r]
		#s =  self.voices[random.randrange(0, len(self.voices))]

	def get_random_rate(self):
		'''
			Return a random speaking rate. 60-275 WPM is about right.
		'''
		return random.randrange(60, 250)

	def get_random_saying(self):	
		''' 
			Randomly index into the 'sayings' list and return a saying.
		'''

		print "length of sayings: " + str(len(self.sayings))
		r = random.randrange(0, len(self.sayings))
		print "index: " + str(r)

		return self.sayings[r]
	#	s = self.sayings[random.randrange(0, len(self.sayings))]

	def get_random_sleep(self):
		'''
			Return a random time that is between @min_wait and @max_wait.
		'''
		return random.randrange(self.min_wait, self.max_wait)

	def build_scam_cmd(self):
		''' 
			Builds the 'say' bash command, and returns the resulting string.
			BASH SYNTAX: say [-v voice] [-r rate] [string ...] 
		'''
		v = self.get_random_voice()
		r = self.get_random_rate()
		s = self.get_random_saying()

		print(s)

		cmd = 'say -v %s -r %s %s' % (v, r, s)
		
		# Decrement the repeat count for the saying
		self.sayings_dict[s] -= 1
		if self.sayings_dict[s] == 0:
			# And remove it from the list if it is out of repeats
			self.sayings.remove(s)

		return cmd

	def say(self):
		''' Given the command, make the Mac actually say it. Essentially a 
			python wrapper for the Bash 'say' command. 
		'''
		cmd = self.build_scam_cmd()
		os.system(cmd)

	def jack_up_volume(self):
		''' 
			Using AppleScript, turn the volume on this Mac all the way up.
			Also, unmute it, just in case.

			WARNING -- Extremely effective. 
		'''
		cmd = 'osascript -e "set volume without output muted"'
		os.system(cmd)
		cmd = 'osascript -e "set volume output volume 100"'
		os.system(cmd)

	def run_scam(self):
		''' 
			Say sayings in a loop, where there is an initial wait, and then
			all other waits between sayings are randomly picked between the 
			interval of @min_wait to @max_wait.

			This will run until all the sayings have been said @repeat_ct times,
			then the program will crash as a result of attempting to index into
			an empty list.
		'''

		exit_level = True
		first = True;

		while exit_level:
			if first:
				time.sleep(self.init_wait)
				first = False
			else:
				# jack_up_volume() 
				self.say()
				time.sleep(self.get_random_sleep())




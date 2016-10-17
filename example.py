from scammer import *

scam_file = 'sayings.txt'
voices = ["Agnes", "Vicki", "Bruce", "Fred", "Alex", "Deranged", "Junior"]	

initial_wait_time = 0.05   # 'run away time'
min_wait = 0.05       # After the initial saying, wait no less than this
max_wait = 0.1		# After the initial saying, wait no longer than this

repeat_count = 5 # How many times to repeat the saying before never saying it again

# Make a Scammer
MyScammer = Scammer(scam_file, voices, initial_wait_time, min_wait, max_wait, repeat_count)

# Get some scams
MyScammer.run_scam()

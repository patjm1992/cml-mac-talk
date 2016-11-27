cml-mac-talk
====
A practical joke taken way too far.



        												_________________
													   /                  \
												      |   I love my dad   |
						   _______________             \_________________/
						:' ,___________,  ':  `.       /
						| '             `  |    `.      
						| |             |  |      `.
  	  _________	   		| |             |  |        \
	 /		   \		| |             |  |         ]
    | lost boys |--		| |             |  |~~~~~~.  )
     \_________/		| `,___________,'  |\__O\_| ,'
						|    _______       |     \.`
						|<> [___=___](@)<> |    .'\
						':________________/__.'   )
						   (____________)        /         \  |   /
						                        /        --  jail  --
						              _________/           /  |   \
						  ___________/______
						 /....=========='(@)\___
						 |[][][][][][][][][]|   \ _______
						 |[][][][][][][][][]|    \__     \
						 |[][][][][][][][][]|    |  \..  |
						 \------------------/    | ( # ) |
						                         |  ---  |
						                         \_______/


This collection of scripts provides a simple way to configure your Mac to talk to you (more like talk *at* you, there's no trace of AI here). It's kinda fun to set this thing off in a quiet library with enough of a time interval to find a secluded spot to watch the resulting reactions.

Usage
-----

To let it run itself, i.e., the program picks sayings randomly with a time inverval based on your parameters -- as in [example.py](https://github.com/p-j-m/ssss/blob/master/example.py):

```python
# Imports and variable definitions here ...

# Make a Scammer object
MyScammer = Scammer(scam_file, voices, initial_wait_time, min_wait, max_wait, repeat_count)

# Get some scams
MyScammer.run_scam()
```

Just fill `sayings.txt` with whatever you want to/want others to hear. You'll/They'll hear it, this program jacks up the volume right before firing off a saying.


Triggering over a network
-------------------------

Partially implemented. Halted because I don't have a Mac for testing the Mac voice thing.

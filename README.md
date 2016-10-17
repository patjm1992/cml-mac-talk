SSSS
====

**S**imple **S**ocket **S**cam **S**erver.


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

To trigger sayings over a network:

```python
''' Not fully implemented yet. '''
```

TODO
----

* Variable/file renaming
* Testing triggering over network
* Remove 'scam' terminology
* PEP 8
* Add 'About'
* Web interface
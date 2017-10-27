def zad13():
    slubowanie = """
	wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
	- zdobywać wiedzę i umiejętności,
	- postępować zgodnie z prawem, tradycją i dobrymi obyczajami akademickimi,
	- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
	"""

    slubowanie[0].upper()
    print(slubowanie.count(' i '))
    print(slubowanie.count('i'))
    print('Uniwersytet' in slubowanie)
    words = slubowanie.split(' ')
    lines = slubowanie.split('\n')
	
zad13();
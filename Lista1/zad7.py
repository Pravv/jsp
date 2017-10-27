def zad7():
    # strip
    str = "___string___"
    print(str.strip('_'))  # string

    # isnumeric
    str = u"this2009"
    print(str.isnumeric())  # false

    str = u"23443434"
    print(str.isnumeric())  # true

    # rjust
    str = 'test'.rjust(25, 'X')  # XXXXXXXXXXXXXXXXXXXXXtest
	
zad7()
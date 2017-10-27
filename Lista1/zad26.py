def funkcja(*args, **kwargs):
	counter = 0
	for arg in args:
		print(counter, " -> ", arg)
		counter += 1
		
	for key, value in kwargs.items():
		print (key, " -> ", value)
   
funkcja(1,2,3, "3244", kotek = "mruczek", piesek = "reksio")

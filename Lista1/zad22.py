def avg(dict):
	return sum(dict.values()) / len(dict)
	
	
dict = {'Mleko': 7, 'Woda': 10, 'Cukier': 12, 'Gruszki': 3, 'Mak': 9}
print(dict)

print("avg", avg(dict))

dict["NowyProdukt"] = 33
print(dict)

print("avg", avg(dict))

del dict["Mleko"]
print(dict)

print("avg", avg(dict))
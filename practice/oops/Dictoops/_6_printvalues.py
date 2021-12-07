#Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
class Dict:
	def printDict(self):
		d=dict()
		for i in range(1,15+1):
			d[i]=i**2
		return d

dict_new = Dict()
print(dict_new.printDict())
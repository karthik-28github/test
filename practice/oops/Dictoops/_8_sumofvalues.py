#Sum all the items in a dictionary
class Dict:
    def returnSum(self):
        sum = 0
        for i in dict:
            sum = sum + dict[i]
        return sum


new_dict = Dict()
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", new_dict.returnSum())
class Demo:
    def __init__(self):
        pass
    def match(self,dict1,dict2):
        for i in dict1.keys():
            if i in dict2.keys():
                print(i,"is available in both the dictionaries")
        print(dict1)
        print(dict2)



d=Demo()
d1={1:100,3:200,5:300,7:400}
d2={1:500,7:1000}
d.match(d1,d2)
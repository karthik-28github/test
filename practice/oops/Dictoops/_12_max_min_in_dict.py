class Dictmaxmin:
    def __init__(self):
        pass
    def dict_max_min(self,a_dict):
        keymax = max(a_dict, key= lambda x: a_dict[x])
        print(f'key is :{keymax}')
        print(f'value is :{a_dict[keymax]}')
        keymin = min(a_dict, key= lambda x: a_dict[x])
        print(keymin)
        print(f'key is :{keymin}')
        print(f'value is :{a_dict[keymin]}')

a_dict = {"a":1, "b":2, "c": 3}
d1=Dictmaxmin()
d1.dict_max_min(a_dict)
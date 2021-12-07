class Dictsum:
    def __init__(self):
        pass
    def sum_key(self,dictA,dictB):
        # dictC=dict
        for key in dictB:
            if key in dictA:
                dictB[key] = dictB[key] + dictA[key]
            else:
                pass
        dictA.update(dictB)
        print(dictA)

dictA = {'Mon': 23, 'Tue': 11, 'Sun': 6}
dictB = {'Wed': 10, 'Mon': 12, 'Sun': 4}

d1=Dictsum()
d1.sum_key(dictA,dictB)
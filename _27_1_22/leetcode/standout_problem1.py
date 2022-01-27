class standout:
    def __init__(self):
        pass
    def chck(self,str1,p1,p2):
        d1=dict()
        # for i in str1:
        #     if i not in d1:
        #         d1[i]=1
        #     else:
        #         d1[i] += 1
        # for i,j in d1.items():
        #     if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
        #         p1.append(i)
        #     else:
        #         p2.append(i)
        print(d1)

        for i in str1:
            print(i)
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i, j in d1.items():
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                p1.append(i)
            else:
                p2.append(i)


        print("player1",p1)
        print("player2",p2)




s=standout()
e=input("Enter the String ")
player1=[]
player2=[]
s.chck(e,player1,player2)
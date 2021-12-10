from abc import ABC, abstractmethod


class Party:
    def arrive_time(self,str1):
        self.str1=str1
        print(f'Arrive at time {str1}')

    @abstractmethod
    def arrange(self,str1):
        pass


class Team1:
    def arrange(self,str1):
        print(f'{str1} arrange food')


class Team2:
    def arrange(self,str1):
        print(f'{str1}arrange drincks')


class Team3:
    def arrange(self,str1):
        print(f'{str1}welcome all')


str1='friends'
p1=Party()
p1.arrive_time(str1)

s1 = Team1()
s1.arrange(str1)
s2 = Team2()
s2.arrange(str1)
s3 = Team3()
s3.arrange(str1)



print("-----------------------------------------------------------")



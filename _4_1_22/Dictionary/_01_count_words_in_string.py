class Word:
   def __init__(self):
      pass
   def Count_words(self,test_string):
      print(test_string)
      word_count = 0
      for i in range(len(test_string)):
         if (test_string[i] == ' ' or test_string[i] == '\n' or test_string[i] == '\t' or test_string[i] == ','):
            word_count += 1
      return word_count

a = input("Enter string here:")
# print(a)
test_string = a
w1=Word()
total = w1.Count_words(test_string)
print("Total Number of Words in our input string is: ", total)


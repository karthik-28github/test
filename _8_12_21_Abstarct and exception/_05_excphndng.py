class ErrorNode(Exception):
    def __init__(self,data):
        self.data=data
    def abc(self):
        print(self.data)

try:
    raise ErrorNode(100)
except:
    print()
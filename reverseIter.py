class ReverseIter:
    def __init__(self,listvalues):
        self.list1 = listvalues
    def reverseList(self):
        length=len(self.list1)-1
        l1=[]
        while length >= 0:
            l1.append(self.list1[length])
            length=length-1
        return l1
    def hello(self):
        return "hi"

if __name__ == '__main__':
    list1=[1,2,3,4,5]
    r1=ReverseIter(list1)
    print(r1.reverseList())
    r1.hello()
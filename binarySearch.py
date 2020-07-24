
def binarySe (list1,l,h,element):
    while l <=h:
        mid = (l+h)//2
        if list1[mid] == element:
            return mid
        elif list1[mid]>element:
            return binarySe(list1,l,mid-1,element)
        elif list1[mid]<element:
            return binarySe(list1,mid+1,h,element)
    if l>h:
         return -1



list1=[1,2,3,4,5,6]
l,h=0,len(list1)-1
element = 4
index = binarySe(list1,l,h,element)
if index == -1:
    print("Element not found")
else:
    print(index)







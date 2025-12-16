import lessons
hero=lessons.Hero('kami', 32,31)
from random import randint
print(lessons.randint(1,100))


def find_element(my_list,target):
    for i,j in enumerate(my_list):
        if target == i:
            return j


my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target=15
def binary_search(arr,target):
    left,right = 0 , len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = (mid+1)
        else:
            right = (mid-1)
    return print('нету чо искали')
binary_search(my_list,target)
my_list_2=[1,2,3444,4,5,6,7,4448,9,10,11,1352,13,14,15]
print(my_list_2,target)
print(sorted(my_list_2))
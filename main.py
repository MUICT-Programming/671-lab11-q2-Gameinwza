# YOUR CODE HERE
def summation(list1, list2):
    total=[]
    for i in range(len(list1)):
        total.append(list1[i]+list2[i])
    return total
def find_min_max(lst):
    mins=min(lst)
    maxs=max(lst)
    return mins,maxs

n = int(input())
list1=[]
for i in range(n):
    l1=int(input())
    list1.append(l1)
list2=[]
for i in range(n):
    l2=int(input())
    list2.append(l2)
sum_list=summation(list1,list2)
print(sum_list)
maxs,mins=find_min_max(sum_list)
print(f'({maxs}, {mins})')

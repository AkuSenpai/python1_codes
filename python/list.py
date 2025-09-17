# num=[1,2,3,4,5]
# print("original list:",num)

# num.append(7)
# print(num)
# print("after append:",num)

# num.insert(3,6)
# print("after insert:",num)

# num.remove(2)
# print("after remove:",num)

# num.sort()
# print("sort:",num)

# num.reverse()
# print("reversed:",num)

# num.extend([8,9])
# print("extend:",num)

# num.insert(2,10)
# print('insert',num)

# print(sum(num))

# print(num.count(4))

# print(len(num))


# print(num.index(3))

# print(min(num))

# print(max(num))

# print("copy:",num)


# print(num.pop())
# print(num)

# print(num.pop(4))
# print(num)

# del num[3]
# print("del:",num)

# num.remove(3)
# print(num)

# x=[]
# print(x)
# x2=[1,2,3]
# print(x2)
# x3=[1,2,5.6,9.8]
# print(x3)
# x4=[1,"one",3.4]
# print(x4)

# l1=['mother','father','daughter',10,23]
# print(l1[0])
# print(l1[2])
# print(l1[4])

# print(l1[-1])
# print(l1[-2])
# print(l1[-6])






#changing elements in list

# l1=['mother','father','daughter',10,23]
# l1[-1]="daughter"
# print(l1)





#concatenation of list


# l1=[1,2,3]
# l2=[3,4,5]
# l3=l1+l2
# print(l3)



#repeating/replicating list

# l1=[1,2,10,23]
# print(l1*4)

# li=[3,8,7,4,5]
# x=len(li)
# print(x)
# for a in range (x):
#      print(li[a])

# for a in range(5):
#     print(a)

# for a in range(5,10,1):
#     print(a)

# for a in range(5,20,2):
#     print(a)

# for a in range(1,x,2):
#     print(a)

# for a in range(1,x,2):
#     print(li[a])

# x=[]
# print(x)
# x=[1,2,3]
# print(x)
# x3=[1,2,5.6,9.8]
# print(x3)
# x4=[1,"one",3.4]
# print(x4)




#tuple bracket

# x=()
# print(x)
# x=(1,2,3)
# print(x)
# x3=(1,2,5.6,9.8)
# print(x3)
# x4=(1,"one",3.4)
# print(x4)



# li=(3,8,7,4,5)
# x=len(li)
# # print(x)
# for a in range (x):
#      print(li[a])


# l1=('mother','father','daughter',10,23)
# print(l1)


# l1=(1,2,3)
# l2=(3,4,5)
# l3=l1+l2
# print(l3)


# l1=('mother','father','daughter',10,23)
# l1(-1)="daughter"
# print(l1)

#tuple is inmutable


# l1=(1,2,10,23)
# print(l1*4)

# li=(3,8,7,4,5)
# x=len(li)
# print(x)
# for a in range (x):
#      print(li[a])

# for a in range(5):
#     print(a)

# for a in range(5,10,1):
#     print(a)

# for a in range(5,20,2):
#     print(a)

# for a in range(1,x,2):
#     print(a)

# for a in range(1,x,2):
#     print(li[a])

# l1=[]
# N=int(input('Enter the name:'))
# for i in range(N):
#      n=input("input enter value:")
#      l1.append(n)
# print(l1)

# a=input("Enter the value:").split()
# print(a)

#Using List Comprehension

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[]
# for x in fruits:
#      if "a" in x:
#           newlist.append(x)
# print(newlist)

# inputlist=[int(x) for x in input().split()]
# print(inputlist)

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if 'a' in  x]
# print(newlist)

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if x != 'apple']
# print(newlist)

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x if x!= 'banana' else 'orange' for x in fruits]
# print(newlist)

# l1=[]
# for i in range(10):
#      l1.append(i**2)
# print("without comprehension:",l1)

# l2=[i**2 for i in range(10)]
# print("comprehension:",l2)

# lst=[-10,-20,10,20,50]
# print(lst)

#multiplying by 2

# new_lst=[i*2 for i in lst]
# print(new_lst)

#finding positive elements

# new_pos_lst=[i for i in lst if i>=0]
# print(new_pos_lst)

# thislist=["orange","mango","kiwi","pineapple","banana"]
# thislist.sort()
# print(thislist)

# thislist=[100,50,65,82,23]
# thislist.sort()
# print(thislist)

# list1=[1,2,3,2,3,4,5,4]
# unique_list=list(set(list1))
# print("list without duplicates:",unique_list)

# thislist=["orange","mango","kiwi","pineappple","banana"]
# thislist.sort(reverse=True)
# print(thislist)


# thislist=[100,50,65,82,23]
# thislist.sort(reverse=True)
# print(thislist)


# num=[2,3,5,3,2,7]
# unique_sum=sum(set(num))
# print("sum of unique number:",unique_sum)

# list1=(1,2,3,['akshaya','kaushik'])
# list2=(2,3,4,(4,'om',5.6))
# print("tuPLES with list:",list1)
# print('Nested tuples:',list2)


# li=(3,4,5,(6,7,8))
# print(li[3][0])

# l1=(1,2,3,['akshaya','kaushik'])
# l1[3][0]='sir'
# print(l1)


# l1=(1,2,3,['akshaya','kaushik',5,7])
# print(l1[3][0:2:])

tuple1=(1,2,3,4,5,6)
tuple2=('aalo','toori','mooli','tamatar')
concat1=tuple1+tuple2
print(concat1)
concat2=tuple1*4
print(concat2)
concat3=tuple2*4
print(concat3)


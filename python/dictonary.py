# student={"name":"kshitij","age":"20","course","python"}

# mydict={}
# print(mydict)

# mydict={1:"one",2:"two"}
# print(mydict)

# mydict={"one":"namit",1:["cse","fet"],2:(2,"gkv"),3:[("A1","ML","DL"),("PYTHON","R")]}
# print(mydict[3][1][0][4])

# mydict=dict()
# print(mydict)

# mydict=dict([(1,"abc"),(2,"pqr")])
# print(mydict)

# b=mydict.copy()
# print(b)

# mydict=dict.fromkeys([1,2,"one"])
# print(mydict)

# mydict=dict.fromkeys([1,2,"one"],10)
# print(mydict)

# mydict={1:2,3:4,"list":[1,23],"dict":{1:2}}
# print(mydict)

# mydict={1:2,3:4,"list":[1,23],"dict":{1:2}}
# print(mydict[1])
# print(mydict.get(3))
# print(mydict(4))
# print(mydict.get(4))
# print(mydict.get(4,0))
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

# mydict={1:2,3:4,"list":[1,23],"dict":{1:2}}
# b={3:5,"the":4,2:1000}
# print(mydict[5])
# print(mydict.popitem())
# print(mydict.pop(1))
# del mydict[1]
# print("after delete [1]:",mydict)
# print(mydict.clear())
# mydict.update(b)
# print("using update() function",mydict)


# square_dict=dict()
# for num in range(1,11):
#     square_dict[num]=num*num
# print(square_dict)

# square_dict={num:num*num for num in range(1,11)}
# print(square_dict)

# dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
# double_dict1={k:v*2 for (k,v) in dict1.items()}
# print(double_dict1)

# dict1_keys={k:v*2 for (k,v) in dict1.items()}
# print(dict1_keys)

# num=range(10)
# new_dict_for={}
# for n in num:
#     if n%2==0: new_dict_for[n]=n**2
# print(new_dict_for)

# new_dict_comp={n:n**2 for n in num if n%2==0}
# print(new_dict_comp)

# old_price={"milk":1.02,"coffee":2.5,"bread":2.5}
# dollar_to_pound=0.76
# new_price={items:value*dollar_to_pound for(items,value)in old_price.items()}
# print(new_price)

# original_dict={"jack":38,'michael':48,'guido':57,'john':33}
# even_dict={k: v for (k,v) in original_dict.items() if v% 2 == 0}
# print(even_dict)

# new_dict={k: v for (k,v) in original_dict.items() if v% 2 == 0 if v<40}
# print(new_dict)

# new_dict_1={k:("bhudda" if v>40 else "javan") for(k,v) in original_dict.items()}
# print(new_dict_1)

# dict1={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
# dict1_triplecond={k:v for (k,v) in dict1.items() if v>2 if v%2==0 if v%3==0}
# print(dict1_triplecond)


# dict1={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
# dict1_triplecond={k:("even"if v%2==0 else "odd") for(k,v)in dict1.items()}
# print(dict1_triplecond)


# a={1:"d",2:"z",5:"b",4:"a"}
# print(sorted(a))
# print(sorted(a.keys()))
# print(sorted(a.values()))
# print(sorted(a.items(),reverse=True))
# print(sorted(a,key=a.get))

# a={1:"d",2:"z",5:"b",4:"a"}
# print(sorted(a.keys()))


# a={1:"d",2:"z",5:"b",4:"a"}
# d={k:a.get(k,0) for k in sorted (a)}
# print(d)


# a={1:"d",2:"z",5:"b",4:"a"}
# print(sorted(a.items(),reverse=True))
# print(sorted(a.keys(),reverse=True))

# a={1:"d",2:"z",5:"b",4:"a"}
# d={k:a.get(k,0)for k in sorted (a,reverse=True)}
# print(d)


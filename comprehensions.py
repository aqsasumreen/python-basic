# list
lis = [4, 45, 9, 81, 3]
print("the Divisible of 3" , [item for item in lis if item%3 ==0])
print([item **3 for item in lis if item%3!=0])

# dictionay
# dict_1  ={'a':3 , 'b':9 , 'A' :8 , 'B':10}
# print({k.upper():dict_1.get(k.lower() , 0)+ dict_1.get(k.upper() , 0)   for k in dict_1.keys()})

# set
# sqd = {x**2 for x in [4,6,3, 4]}
# print(sqd)
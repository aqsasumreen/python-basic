# iterable--aik python obj hy js me __iter ya __getitem fun use hta ,,jo k hmy iterator deta.
# iterators--aisa obj js me next method define hta ,,mean hmy agla se agla element deta.
# iteration--kisi b chz ko iterate krna aur uske next elements ko fetch krna called iteration.
# generators--python obj jn k oper hm sirf aik br iterate kr skty hain aur wo on the fly values generate krty...
def gen(n):
    for i in range(n):
        yield i

print(gen(10000))
for i in gen(10):
    print(i)

num = "344"
# INT OBJECTS ARE NOT ITERABLE...
for i in  num:
    print(i)

var = "aqsa"
iter1 = iter(var)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
import time
initial = time.time()
k =0
while k<10:
    print("This is Aqsa..")
    time.sleep(3)
    k+=1
print("While loop Ran in " ,time.time()-initial , "seconds")
initial2  = time.time()

for i in range(10):
    print("This is Mawo..")

print("For loop ran in", time.time() -initial2, "seconds")
try:
    open("this.txt")
except:
    print("no such file or directory")

else:
    print("no Exception caught")
finally:
    print("code in this block must run.")


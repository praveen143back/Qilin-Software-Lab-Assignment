new=(input("enter numbers"))
new1=new.split(',')
print(new)
swap1=int(input("enter index of 1st number to be swapped"))
swap2=int(input("enter index of 2nd number to be swapped"))
print(new1,swap1,",",swap2)
new1[swap1],new1[swap2]=new1[swap2],new1[swap1]
print(new1)
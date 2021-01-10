num = int(input("Please Enter The Number :- "))
# Used dictionary  comprehension method
d = {i: i*i for i in range(1, num+1)}
print(d)

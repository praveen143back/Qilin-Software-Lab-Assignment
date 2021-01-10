num = input("Please Enter The Numbers : ")

# used split method to split string into list
# and type casted string to integer in list
list_odds = [i for i in num.split(',') if (int(i) % 2 != 0)]

# used join method to join them into one string.
print((",".join(list_odds)))

line = input("Enter string: ")
word=line[0:line.index(" ")]
words=[word.lower() for word in line.split()]
words.sort()
if(words.count(word)>1):
      words.remove(word)
for word in words:
  print(word,end=" ")

  if(words.count(word)>1):
      words.remove(word)
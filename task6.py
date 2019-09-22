my_file= open('words.txt')
for line in my_file: 
    sentence=my_file.readline()
word=sentence.strip()
a=0
index=0
for letter in word:
    if ord(letter)<ord(word[index+1]):
        a=a+1
        index=index+1
if a==len(word):
    print(word)

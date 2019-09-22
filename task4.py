goal = 'acefhlo'
y=open('words.txt', 'r')
word_list = y.read().splitlines()
def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True
words = [word for word in word_list if uses_only(word, goal)]
print(There are {} words that use only '{}', here's a sample: {}".format(len(words), target, words[:10]))


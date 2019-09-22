def do_some(word):
    for i in range(len(word) - 5):
            if word[i] == word[i + 1]:
                if word[i + 2] == word[i + 3]:
                    if word[i + 4] == word[i + 5]:
                        return True
    return False
y = open("item.txt")
def find_do_some():
    for line in wordlist:
        word = line.strip()
        if do_some(word):
            print(word)
find_do_some()

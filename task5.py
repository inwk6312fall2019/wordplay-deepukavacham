x=open('file.txt', 'r')
my_list = x.read().split()
def user_all(word, string):
    count = 0
    for letter in string:
        if letter in word:
            count += 1
    if count == len(string):
        return True
    return False
def find_all_vowels(list):
    count = 0
    string = 'aeiou'
    for word in list:
        if user_all(word, string):
            count += 1
    return count

print(find_all_vowels(word_list))


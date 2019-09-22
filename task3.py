def items_entered(word,forbidden_string):
    for char in word:
        if char.lower() in forbidden_string.lower():
            return False
    return True
def avoid(string, forbidden_string):
    words = string.split()
    correct_words = []
    for word in words:
        if items_entered(word, forbidden_string):
            right_words.append(word)
    print('\n'," ".join(right_words))
avoid()


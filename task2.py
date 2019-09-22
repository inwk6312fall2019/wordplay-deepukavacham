y=open('file.txt', 'r')
item_list = y.read().split()
def no_e(word):
    return word.find('e') == -1
total = len(item_list)
no_e = [word for word in item_list if no_e(word)]
percentage = float(len(no_e)) / total
print'{:.2%}'.format(percentage)


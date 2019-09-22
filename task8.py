def palindrome(num):
    return str(num) == str(num)[::-1]
def puzzler_8():
    for num in range(100000, 1000000):
        if palindrome(str(num)[2:6]):
            if palindrome(str(num + 1)[1:6]):
                if palindrome(str(num + 2)[1:5]):
                    if palindrome(str(num +3)):
                        print(num)
    return False
puzzler_8()

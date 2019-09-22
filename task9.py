def palindrome_age(motherAge, daughterAge):
    Age_mother = str(motherAge)
    Age_daughter = str(daughterAge)
    diff= len(Age_mother) - len(Age_daughter)
    Age_daughter = Age_daughter.zfill(len(motherAge))
    age_mother = age_mother[::-1]
    if Age_mother == Age_daughter:
        return True
    else:
        return False
count = 0
previousDiffAge = 0
for Age_mother in range (15, 120):
    for Age_daughter in range(1, 100):
        diffAge = Age_mother - Age_daughter
        if palindrome(Age_mother, Age_daughter) and diffAge == previousDiffAge:
            count = count + 1
            if count == 6:
                print(Age_mother)
                print(Age_daughter)
    previousDiffAge = diffAge

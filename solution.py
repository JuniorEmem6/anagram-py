# write the function is_anagram
def is_anagram(test, original):
    fword = test.lower()
    sword = original.lower()

    if(len(fword) != len(sword)
       return False

    new_fword = sorted(fword)
    new_sword = sorted(sword)

    for count in range(original):
        if new_fword[count] in new_word:
            continue
        else:
            return False

    return True

solution = is_anagram("foefet", "toffee")
print(solution)

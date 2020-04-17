'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


count = 0


def split(string):
    print(string)
    to_list = list(string)
    del(to_list[0])
    new_string = "".join(to_list)
    return new_string


def count_th(word):
    global count
    if len(word) <= 1:
        print(count)
        return count
    elif word[0] == "t" and word[1] == "h":
        count += 1
    return count_th(split(word))


count_th("abcthefthghith")

# tests fail because global counter isn't resetting between function calls. If you test all cases individually, they all return the expected result

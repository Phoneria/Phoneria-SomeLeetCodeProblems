def convert(string):
    letter = {}

    for i in string:
        if not i in letter:
            letter[i] = len(letter)


    number_list = []

    for i in string:
        number_list.append(letter[i])



def is_isomorphic(s,t):
    if convert(s) == convert(t):
        return True


print(is_isomorphic("egg","add"))
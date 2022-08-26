import itertools

s = "ADOBECODEBANC"
t = "ABC"

def is_in(s,t):
    """words = []

    group = ""

    temp_t = t
    let= False
    for letter in s:
        if letter in temp_t:
            let=True
            temp_t.replace(letter, '')

        if let:
            group+=letter

        if temp_t == '':
            let = False
            words.append(group)
            group=""

    return(words)"""

    words = []

    group = ""
    let = False
    for letter in s:
        if letter in t[0]:
            group = ""
            let = True

        if let:
            group += letter

        if let and letter == t[len(t) - 1]:
            words.append(group)
            group = ""
            let = False

    for i in words:
        for j in t:
            if not j in i:
                words.remove(i)
    return (words)




def mix_letter(t):
    each_letter = []
    for i in t:
        each_letter.append(i)

    temp_words  = list(itertools.permutations(each_letter, len(t)))

    mixed_words = []
    group = ""
    for j in temp_words:
        for h in j:
            group+=h
        mixed_words.append(group)
        group=""

    return mixed_words

all_true_words = []
for i in (mix_letter(t)):
    if len(is_in(s, i)) != 0:
        all_true_words.append(is_in(s, i))


shortest = all_true_words[0][0]
for i in all_true_words:
    if len(i[0]) < len(shortest):
        shortest = i[0]


print(shortest)
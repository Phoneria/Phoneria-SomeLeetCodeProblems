s = "ADOBECODEBANC"
t = "ABC"

words = []

group = ""
let = False
for letter in s :
    if letter in t[0]:
        group = ""
        let = True

    if let:
        group+=letter

    if let and letter == t[len(t)-1]:
        words.append(group)
        group=""
        let = False


for i in words:
    for j in t :
        if not j in i:
            words.remove(i)

print(min(words,key=len))



#Course Schedule III

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]

courses.sort(key=lambda i:i[0])
for i in courses:
    if i[0] > i[1]:
        courses.remove(i)

print(courses)
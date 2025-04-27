marks = [12, 44, 52, 62, 90]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print('%d번 학생 축하합니다. 합격입니다.' % number)


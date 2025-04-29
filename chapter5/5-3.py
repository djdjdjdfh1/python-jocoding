import datetime

try:
    f = open('나없는파일', 'r')
except:
    print('에러 발생')

day1 = datetime.date(2025, 4, 29)
print(day1)
year = int(input("연도 입력: "))

if (year % 4 ==0 and year % 100 == 0 and year % 400 == 0):
    print("윤년")

elif (year % 4 == 0 and year % 100 == 0):
    print("윤년x")

elif (year % 4 ==0):
    print("윤년")

else:
    print("윤년이 아니다")

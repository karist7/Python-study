score_list = [95,80,99,93,78,72,83,35,59,66]
grade_list = []


def getGrade():
    if score >= 95:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 75:
        return "C+"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D+"
    elif score >= 60:
        return "D"
    else:
        return "F"
    

for i in range (score_list):
    grade_list.append(i)
index = -1
while (index < len(score_list)):
    index += 1
    print("",grade)

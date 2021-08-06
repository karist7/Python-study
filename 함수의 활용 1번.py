counter = 0


def flatten(data):
    out = []
    for i in data:
        if type(i) == list:

            out += flatten(i)

        else:
            out.append(i)
    return out

example = [[1,2,3],[4,[5,6],7, [8, 9]]]
print("원본:", example)
print("변환:", flatten(example))

#append활용 빈리스트 생성은 맞췄지만 리스트 활용에 대한 생각이 부족했다.
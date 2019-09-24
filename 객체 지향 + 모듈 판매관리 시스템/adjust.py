infile = open("fruits.txt","r") #fruits.txt를 read모드로 연다
fruits = eval(infile.read()) #fruits의 딕셔너리를 읽는다
infile.close()#파일을 닫는다


def adjust(): 
    while True: #무한 반복
        cmds = int(input("재설정 1.수량변경, 2.추가, 3.삭제, 4.종료: ")) 
        if cmds == 1:
            a = input("과일 선택:")
            b = int(input("개수 입력:"))
            key = a #key값에 a할당
            fruits[key][1] = b #fruits 딕셔너리의 2번째 인덱스인
                                #재고량에 b값 할당
        elif cmds == 2:
            fruit = input("상품: ")
            if fruit not in fruits.keys(): #fruits의 key값에 상품이 없을경우
                price = int(input("가격: ")) #가격을 price에 할당
                store = int(input("재고량: ")) #재고량을 store에 할당
                fruits[fruit] = [price,store] #fruit딕셔너리에 할당한 값들을
                            #딕셔너리로 추가(fruit = key, price,sotre = value)
        elif cmds == 3:
            key = input("삭제할 물품은? ") #삭제할 물품 입력받아 key에 할당
            if key in fruits.keys(): #fruits의 key값에 key가 있다면
                del fruits[key] # key값에 해당하는 딕셔너리 삭제
        
        elif cmds == 4:
            outfile = open("fruits.txt","w") #fruits.txt를 write모드로 연다
            outfile.write(str(fruits)) #fruits를 문자열 형태로 쓴다
            outfile.close() #파일을 닫는다
            print("저장후 종료합니다.") #저장후 종료합니다 출력
            break #작동중지

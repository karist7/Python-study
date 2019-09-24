from adjust import * #save모듈을 import한다

import sqlite3 #sqlite3모듈을 import한다

infile = open("fruits.txt","r") #fruits.txt를 read모드로 연다
fruits = eval(infile.read()) #fruits의 딕셔너리를 읽는다
infile.close()#파일을 닫는다



def info(): #info함수 정의
    for key in fruits.keys(): #key값 반복
        printfruit(key) #결과 출력
        
def printfruit(key): #printfruit(key)함수 정의
    print(key, "\t가격=", fruits[key][0], "\t재고=", fruits[key][1]) #목록 출력
    
con = sqlite3.connect('판매.db') #판매.db 데이터베이스 파일을 연결한다
cur = con.cursor() #커서 객체를 받아온다
#cur.execute("create table test (product text, price int, store int)")
#테이블을 생성한다 계속 반복될 시 오류가 나므로 한 번 만들어둔 후 빼야한다 처음 설명이니 추가함


while True: #무한 반복
    cmd = input("명령을 입력하시오(출력,판매,수정,종료):") #명령어 입력
    if cmd == "출력":
       info() #전체목록 출력
       
    elif cmd == "판매": #명령어가 판매일 경우
        a = input("과일 선택:")
        b = int(input("개수 입력:")) 
        key = a #key값을 선택한 과일로 한다.
        c = fruits[key][0] #a의 0번쨰 인덱스인 가격을 c에 할당한다
        e = b * c #총 가격을 e에 할당한다
        if b > fruits[key][1]: #남은 재고보다 더 많이 입력한 경우
            print("재고가 부족합니다.")
        else: #재고가 충분할 경우
    
            if input("할인카드가 있습니까? ") == 'y': 
                e = discount(e) #discount모듈의 discount함수 호출하여 할인된 가격을 e에 저장한다.
       
                cur.execute("insert into test values (:fruit, :price, :store)",
                    {'fruit':a,'price':e,'store':b}) #입력한 정보를 레코드에 저장한다.
                con.commit() #정보를 저장
            else:
                cur.execute("insert into test values (:fruit, :price, :store)",
                    {'fruit':a,'price':e,'store':b}) #입력한 정보를 레코드에 저장한다.
                con.commit() #정보를 저장
               
            fruits[key][1] -= b #fruits 딕셔너리에 인덱스 첫번째 값인 재고량에 구매한 개수만큼 감소시킨다.
    elif cmd == "수정": 
        adjust() #adjust모듈의 adjust함수 호출
    elif cmd == "종료": 
        break #프로그램 종료
        con.close() #데이터 베이스 종료


import sqlite3
from adjust import *

infile = open("fruits.txt","r")
fruits = eval(infile.read())
infile.close()
con = sqlite3.connect('판매.db')
cur = con.cursor()

#부모 클래스
class Management():
    # 속성
    fruit = 0
    price = 0
    sell = 0
    # 생성자
    def __init__(self,fruit,price,sell):
        self.fruit = fruit
        self.price = price
        self.sell = sell
        
    # 매서드
    def save(self):
        cur.execute("insert into test values (:fruit, :price, :store)",
                    {'fruit':a,'price':e,'store':b}) #입력한 정보를 레코드에 저장한다.
        con.commit() #정보를 저장
#자식 클래스
class Discount_management(Management):
    # 생성자
    def __init__(self,fruit,price,sell):
        Management.__init__(self,fruit,price,sell)
    #오버라이드 매서드
    def save(self):
        cur.execute("insert into test values (:fruit, :price, :store)",
                    {'fruit':a,'price':0.9 * e,'store':b}) #입력한 정보를 레코드에 저장한다.
        con.commit() #정보를 저장

#cur.execute("create table test (product text, price int, store int)")
#테이블을 생성한다 계속 반복될 시 오류가 나므로
#한 번 만들어둔 후 빼야한다 처음 설명이니 추가함
def printfruit(key): #printfruit(key)함수 정의
    print(key, "\t가격=", fruits[key][0], "\t재고=", fruits[key][1]) #목록 출력


while True:
    for key in fruits.keys(): #key값 반복
        printfruit(key) #결과 출력
    cmd = int(input("명령을 입력하시오(1.판매,2.재설정,3.초기화,4.종료):"))
    if cmd == 1:
        a = input("과일 선택:")
        b = int(input("개수 입력:")) 
        key = a #key값을 선택한 과일로 한다.
        c = fruits[key][0] #a의 0번쨰 인덱스인 가격을 c에 할당한다
        e = b * c #총 가격을 e에 할당한다
        if b > fruits[key][1]: #남은 재고보다 더 많이 입력한 경우
            print("재고가 부족합니다.")
        else: #재고가 충분할 경우
    
            if input("할인카드가 있습니까? ") == 'y':
                #자식 클래스 이용
                manage = Discount_management(a,e,b)
                manage.save()
            else:
                #부모 클래스 이용
                manage = Management(a,e,b)
                manage.save()
            fruits[key][1] -= b
            #fruits 딕셔너리에 인덱스 첫번째 값인
            #재고량에 구매한 개수만큼 감소시킨다.
    elif cmd == 2:
        adjust()
        infile = open("fruits.txt","r") #fruits.txt를 read모드로 연다
        fruits = eval(infile.read()) #fruits의 딕셔너리를 읽는다
        infile.close()#파일을 닫는다
    elif cmd == 3:
        #데이터 베이스의 데이터를 모두 지운다.
        cur.execute("delete from test")
        con.commit()
        1
    elif cmd == 4:
        #file = open("fruits.txt","w") #fruits.txt를 write모드로 연다
        #file.write(str(fruits)) #fruits를 문자열 형태로 쓴다
        #file.close() #파일을 닫는다
        print("프로그램 종료.")
        con.close()#데이터 베이스 종료
        break

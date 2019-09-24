from transaction import *# transactions모듈 import
import promotion #promotion 모듈 import
import starbuzz #starbuzz 모듈 import

items = ["DONUT","LATTE","FILTER","MUFFIN"] #items 리스트 목록
prices = [1.50,2.20,1.80,1.20] #price 리스트 목록
running = True #running일 경우 동

while running: #running이 True이므로 무한 반복
    option = 1 #option에 1할당
    for choice in items: #items를 choice만큼 반복
        print(str(option) + "." + choice) #option을 문자열로 변환,
        #option과 ".", choice를 결합하여 출력
        option += 1 #반복할 때 마다 option 1증가
    print(str(option) + ".Quit") #문자열로 변환한option에 .Quit결하바여 출력
    choice = int(input("Choose an option: ")) 
    if choice == option: #choice와 option이 같을 경우
        running = False #반복 중지
    else: #아닐 경우
        credit_card=input("Credit card number: ") 
        price = promotion.discount(prices[choice-1])
        #promotion 모듈의 discount함수에 price리스트의 choice-1인덱스값 price에 할당
        if input("Starbuzz card? ") == "Y": #Starbuzz card가 있을 경우
            price = starbuzz.discount(price)
            #Starbuzz모듈의 discount함수에 price를 넣어 계산
        save_transaction(price,credit_card,items[choice-1])
        #save_transaction함수에 입력한 정보값을 전달하여 메모장에 저장

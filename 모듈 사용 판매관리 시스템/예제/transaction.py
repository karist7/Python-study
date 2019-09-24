def save_transaction(price,credit_card,description):
    #save_transaction함수에 매개변수price,credit_card,description포함하여 정의
    file = open("transaction.txt","a") #transaction.txt를 append모드로 연다
    file.write("%07d%16s%16s\n" % (price * 100,credit_card,description))
    #transaction.txt에 입력된 정보값을 저장한다.
    file.close() #파일을 종료한다.

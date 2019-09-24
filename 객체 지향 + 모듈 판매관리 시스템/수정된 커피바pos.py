# 부모 클래스
class Transactions(): 
    # 속성
    price = 0.0 
    credit_card = 0 
    item = 0
    # 생성자
    def __init__(self, cost, card, item):
        self.price = cost
        self.credit_card = card
        self.item = item
    # 메서드
    def save(self):
        #transactions. txt파일을 append모드로 연다
        file = open("transactions.txt", "a")
        #파일에 7,16,16글자씩 입력받은 것을 쓴다.(글자수 부족하면 빈공간)
        file.write("%07d%16s%16s\n" % (self.price * 100,
                                       self.credit_card, self.item))
        file.close()
# 자식 클래스
class Discount_trans(Transactions):
    # 생성자
    def __init__(self, cost, card, item):
        Transactions.__init__(self, cost, card, item)
    # 오버라이드 메서드
    def save(self):
         #transactions. txt파일을 append모드로 연다
        file = open("transactions.txt", "a")
        #파일에 7,16,16글자씩 입력받은 것을 쓴다.(글자수 부족하면 빈공간)
        #price에 10% 할인된 가격을 저장한다.
        file.write("%07d%16s%16s\n" % (self.price * 100 * 0.9,
                               self.credit_card, self.item))
        file.close()
items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
running = True
#while문의 running이 True이므로 무한 반복
while running:
    option = 1
    #for문을 이용하여 choice를 items(4번)만큼 반복
    for choice in items:
        print(str(option) + ". " + choice)
        #반복할 때마다 option1증가
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False #작동 중지
    else:
        card = input("Credit card number: ")
        if input("Starbuzz card? ") == "Y":
            #자식 클래스 이용
            trans = Discount_trans(prices[choice-1], card, items[choice - 1])
            trans.save()
        else:
            #부모 클래스 이용
            trans = Transactions(prices[choice-1], card, items[choice - 1])
            trans.save()

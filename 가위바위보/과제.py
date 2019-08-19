import turtle
import random #random 라이브러리의 choice 를 사용하기 위해 import 수행

screen = turtle.Screen()
image1 = "rock.gif" #image1 변수에 rock.gif 를 할당합니다.
image2 = "scissors.gif"
image3 = "paper.gif"
screen.addshape(image1)
screen.addshape(image2)
screen.addshape(image3)

TempDict = {"바위":"rock.gif","가위":"scissors.gif","보":"paper.gif"}

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
user = turtle.textinput("","가위,바위,보 중 하나를 선택하시오.")
computer = random.choice(["가위","바위","보"])
t1.up()
t1.goto(-200,0)
t2.up()
t2.goto(200,0)
t3.penup()
t3.goto(-150,300)
t1.shape(TempDict[user])
t1.stamp()
t1.write("당신의 선택")
t2.shape(TempDict[computer])
t2.stamp()
t2.write("컴퓨터의 선택")
if user == "가위":
   # t1.shape(image2)
    #t1.stamp()
    #t1.write("당신의 선택")
    if computer == "바위":
       
        #t2.shape(image1)
        #t2.stamp()
       # t2.write("컴퓨터의 선택")
        t3.write("당신이 졌습니다.",font = ("None",50,"normal"))
        
        print("컴퓨터가 이겼습니다.")
    elif computer == "가위":
        
       # t2.shape(image2)
       # t2.stamp()
       # t2.write("컴퓨터의 선택")
        t3.write("비겼습니다.",font = ("None",50,"normal"))
        print("비겼습니다.")
    else:
        #t2.shape(image3)
        #t2.stamp()
        #t2.write("컴퓨터의 선택")
        print("당신이 이겼습니다.")
        t3.write("이겼습니다.",font = ("None",50,"normal"))
elif user == "바위":
 
  #  t1.shape(image1)
   # t1.stamp()
  #  t1.write("당신의 선택")
    if computer == "보":
        
        #t2.shape(image3)
        #t2.stamp()
        #t2.write("컴퓨터의 선택")
        t3.write("당신이 졌습니다.",font = ("None",50,"normal"))
    elif computer == "바위":
        #t2.shape(image1)
        #t2.stamp()
        #t2.write("컴퓨터의 선택")
        t3.write("비겼습니다.",font = ("None",50,"normal"))
    else:
        #t2.shape(image2)
        #t2.stamp()
        #t2.write("컴퓨터의 선택")
        print("당신이 이겼습니다.")
        t3.write("이겼습니다.",font = ("None",50,"normal"))
else:
   # t1.shape(image3)
    # t1.stamp()
  #  t1.write("당신의 선택")
    if computer == "가위":
       # t2.shape(image2)
       # t2.stamp()
       # t2.write("컴퓨터의 선택")
        t3.write("당신이 졌습니다.",font = ("None",50,"normal"))
        
    elif computer == "바위":
        #t2.shape(image1)
        #t2.stamp()
        #t2.write("컴퓨터의 선택")
        print("당신이 이겼습니다.")
        t3.write("이겼습니다.",font = ("None",50,"normal"))
    else:
       # t2.shape(image3)
       # t2.stamp()
       # t2.write("컴퓨터의 선택")
        print("비겼습니다.")
        
        t3.write("비겼습니다.",font = ("None",50,"normal"))
    

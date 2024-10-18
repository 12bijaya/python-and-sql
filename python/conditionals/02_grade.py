# creating the program that will find the grade of the student 

score = float(input("what is your score "))
tscore = float(input("what is the total score of the exam "))
y = 100*score/tscore
print(f"the percentage you have got is {y:.2f} ", end="%\n")
print("Congralutation", end=" ")
if y<100 and y>=90:
    print("you have got A+")
elif y<90 and y>=80:
    print('you have got A')
elif y<80 and y>=70:
    print("you have got B+")
elif y<70 and y>=60:
    print("you hsve got B")
elif y<60 and y>=50:
    print("you have got C+")
elif y<50 and y>=40:
    print("YOu have got C")
elif y<40 and y>=35:
     print("you have got D")
else :
    print("You have got NG")

# the better way than this is given

print("Congralutation", end=" ")
if  100>y>=90:
    print("you have got A+")
elif  90>y>=80:
    print('you have got A')
elif 80>y>=70:
    print("you have got B+")
elif 70>y>=60:
    print("you hsve got B")
elif 60>y>=50:
    print("you have got C+")
elif  50>y>=40:
    print("YOu have got C")
elif  40>y>=35:
     print("you have got D")
else :
    print("You have got NG")

#more better than that is 
print("Congralutation", end=" ")
if y>=90:
    print("you have got A+")
elif y>=80:
    print('you have got A')
elif y>=70:
    print("you have got B+")
elif y>=60:
    print("you hsve got B")
elif y>=50:
    print("you have got C+")
elif y>=40:
    print("YOu have got C")
elif y>=35:
     print("you have got D")
else :
    print("You have got NG")
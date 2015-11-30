

import random

number1=random.randint(1,10)
number2=random.randint(1,10)
number3=random.randint(1,10)
count=0
count_1=0
ball=0
strlike=0
no_match=3
manu_num=1;

print "=============manu============="
print "1.Explanation or interface ==="
print "2.Start======================="
print "3.exit========================"
print "Enter the manu_number?========"

manu_num=int(raw_input())

if manu_num==1:
   print "======base ball game========"
   print "Three number match success=="
   print "Thank you==================="
   print "Three number use or not zero"
   print "input Three number not zero="
   print "Find bug send e-mail->======"
   print "rnjsxoqkf@naver.com GoGo===="
   print "Thank you go baseball start="
   print ""
   manu_num+=1
  
if manu_num==2:
   print "welcome visit start"
   while number1==number2 and number3==number3 and number2==number3:
     if number1==number2:
        number1=random.randint(1,10)
     elif number2==number3:
        number2=random.randint(1,10)
     elif number3==number1:
        number3=random.randint(1,10)
     
   baseball=[number1,number2,number3]

   while strlike<3:
     count=0
     strlike=0
     ball=0
     print "input number ex_) number 1,number 2,number 3"
     a_num1=int(raw_input())
     a_num2=int(raw_input())
     a_num3=int(raw_input())
     if a_num1==0 and a_num2==0 and a_num3==0:
       break
     for count in xrange(3):
       if a_num1==baseball[count]:
         if a_num1==baseball[0]:
           strlike+=1
         else:
           ball+=1
       elif a_num2==baseball[count]:
          if a_num2==baseball[1]:
            strlike+=1
          else:
            ball+=1
       elif a_num3==baseball[count]:
          if a_num3==baseball[2]:
            strlike+=1
          else:
            ball+=1
       no_mathch=no_match-strlike-ball
     print "ball:",ball,"stlike:",strlike,"--"
     count_1+=1
print "Your count:",count_1,"Thank you"      

if manu_num==3:
  print "Thank you"
et=raw_input()



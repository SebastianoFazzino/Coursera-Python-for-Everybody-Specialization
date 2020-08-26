#Calculating the score

score = input("Enter Score: ")

try:
   score = float(score)
    
   if score > 0.0 and score < 0.6:
        print ("F")
   elif score >= 0.6 and score <= 0.69:
        print("D")
   elif score >= 0.7 and score <= 0.79:
        print ("C")
   elif score >= 0.8 and score <= 0.89:
        print("B")
   elif score >=0.9 and score <=1.0:
        print("A")
   else:
        print("Score value must be between 0.0 and 1.0")
        
        
except:
   print("wrong input!")
    

      

#calculating the pay


hrs = input("Enter Hours:")
hr_rate = input("Enter Pay Rate:")


try:
   hrs = float(hrs)
   hr_rate = float(hr_rate)
except:
    print("Please enter numeric input!")
    quit()


extratime = hrs - 40

if hrs > 40:
   pay = 40 * hr_rate + extratime * 15.75
elif hrs > 1 and hrs <= 40:
   pay = hrs * hr_rate
print(pay)




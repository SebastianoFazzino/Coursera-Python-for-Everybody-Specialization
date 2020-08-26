#Example of function:


hrs = input("Enter Hours:")
hr_rate = input("Enter Pay Rate:")

try:
   hrs = float(hrs)
   hr_rate = float(hr_rate)
except:
    print("Please enter numeric input!")
    quit()

extratime = hrs - 40

def computepay(hrs, hr_rate):
 
   
    if hrs > 40:
        pay = 40 * hr_rate + extratime * hr_rate * 1.5
    else:
        pay = hrs * hr_rate
        
    return pay
 
pay =  computepay(hrs, hr_rate)
print("Pay",pay)
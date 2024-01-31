def compute_wage(days, gender, age):
   if 18<= age <= 29:
       if gender == "male":
        wage_per_day = 15000
       elif gender == "female":
        wage_per_day = 20000
       else:
        return -1
   elif 30<= age <= 49:
       if gender == "male":
        wage_per_day = 25000
       elif gender == "female":
        wage_per_day = 30000  
       else:
        return -1
   else:
    return  -2
   total_wage = wage_per_day * days
   return total_wage
name = str(input("Please enter your name\n"))  
age = int(input("Please enter your age\n"))
gender = str(input("Please enter your gender (male or female)\n"))
days = int(input("Please enter number of days worked\n"))
wage = compute_wage(days, gender, age)
if wage == -1:
  print("Sorry, the gender you entered is invalid.")
elif wage == -2:
  print("Sorry, the age you entered is invalid.")  
else:
  print(f"Hlo, {name}. You are {age}years old and you worked for {days}days.")
  print(f"Your total wage is {wage} shs")



    
        
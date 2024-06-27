age = int( input("Age :"))

if age < 18 :  
    print("You are young!")

elif age > 18 and age < 30 : 
    print ("You are normal.")

else : 
    print("You are old.")



# input with if conditon

user_status = input("Are you tired? 'Y/N'")

if(user_status) == "Y" :
    print("Take a rest well, Please!")

elif(user_status) == "N" :
    print("Go back to proceed your work.")

else : 
    print("Please enter your status only with Y or N ! Please.")


user_info = input("Login with email: example@gamil.com")
user_pass = input("Password with strong: #*kKiw12")

if(user_info) == "khun@gamil.com" :
    print("You are successful login!")
elif(user_pass) == "khun" :
    print("correct password")
elif(user_info and user_pass): 
    print("You are email and pass not match.")
else : 
 print("You are not authenticate person.")

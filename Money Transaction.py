
## Money Transaction program, you can send, pay things, and receive money, check the balance left in your account as the mobile payment process

prints ("....................IF YOU ARE NEW TO THIS SERVICE WE OFFER YOU A FREE SERVICE OF YOUR CHOICE BUT WE SPECIFICALLY ACCEPT THE FOLLOWING SERVICES: \n1. LUMICASH if you enter *163# \n2. CLIENTEL SERVICE if you enter *131# \n3. DEBT REQUEST if you enter *800*7# \n4. INSTRUCTION ABOUT THESE 3 SERVICES if you enter *100#..........!!!!\n")

amount_possessed = 1000000 ## amount of money possessed in the account.
code = input("Enter the code of a service you want to request:")
name = input("What is your name sir : ")

if code == "*163#":
  print("**************** WELCOME TO LUMICASH SERVICES ", name, "****************\n Here are the Services we offer:\n0. send money\n1. withdraw money\n2. Buy airtimes\n3. Pay the seller\n4. Pay bill\n5. Buy tickets\n6.check account balance\n7.cancel\n")
  choice = int(input("Enter the number of the service you want to request:"))
  if choice == 0:
    def send_money():
      phone_number = int(input("Enter the phone number of the person you want to send money to:"))
      amount = int(input("Enter the amount you want to send:"))
      if len(str(phone_number)) == 8 and amount < amount_possessed:
        print("You have successfully sent >>" + str(amount) + "to this number :"+ str(phone_number))
        amount_left = amount_possessed - amount
        print(" You have now " + str(amount_left) + "in your Lumicash account!")
    send_money()
  elif choice == 1:
    def withdraw_money():
      amount = int(input("Enter the amount you want to withdraw:"))
      print("You have successfully withdrawn " + str(amount) + " from your Lumicash account! ")
      amount_left = amount_possessed - amount
      print(" You have now " + str(amount_left) + "in your Lumicash account!")
      
    withdraw_money()
    
  elif choice == 2:
    def buy_airtime():
      amount_of_airtime = int(input("Enter the amount of airtime you want to buy:"))
      if amount_of_airtime < amount_possessed:
        print("You have successfully bought " + str(amount_of_airtime) + " airtime! ")
        amount_left = amount_possessed - amount_of_airtime
        print(" You have now" + str(amount_of_airtime) + "in your airtime savings and " + str(amount_left) + "in your Lumicash account!")
      else:
        print(" Sorry! You are not eligible to get the airtime unless you diminish your wanted airtime!")
        second_chance = input("Do you want to try again? (yes/no) >>>>>")
        if second_chance == "yes":
          buy_airtime()
          exit()
        else:
          print("Thanks for trying out!\n")
          exit()
    buy_airtime()
  elif choice == 3:
        def pay_the_seller():
          amount_to_pay = int(input("Enter the amount of the money you want to pay the seller:>>>>"))
          seller_phone_number = int(input("Enter the phone number of the seller:>>>>"))
          if len(str(seller_phone_number)) != 8:
            print("Sorry! The seller's phone number must be 8 digits long! Try again >>")
            pay_the_seller()
          if amount_to_pay < amount_possessed:
              amount_in_possession = amount_possessed - amount_to_pay
              print("You have successfully sent",amount_to_pay,"to the seller and you have now", amount_in_possession)
          else:
              second_chance = input("Sorry, you don't have such amount of money in your Lumicash account!Do you want to try again? yes or no>>>")
              if second_chance == "yes":
                  pay_the_seller()
                  exit()
              else:
                  exit()

        pay_the_seller()

  elif choice == 4:
        def pay_bill():
          amount_bill = int(input("Enter the amount of money to pay the bill:"))
          phone_number = int(input(" Enter the phone number to which you want to pay the bill:"))
          your_password = int(input("Enter your password:"))
          if len(str(phone_number)) != 8 and your_password < 10 and amount_bill > amount_possessed:
              print(" Check!!!!! There is a number missing! The phone number must be 8 digits long and the password 10 digits long or more! and the balance in your account!:")
              pay_bill()
              exit()
          else:
            amount_left = amount_possessed - amount_bill
            print("You have successfully paid", amount_bill, "to", phone_number, "and you have now", amount_left)

        pay_bill()
  
  elif choice == 5:
    def pay_ticket():
      amount_ticket = int(input("Enter the amount of money to spend for the ticket:"))
      your_password = input("Enter your password but remember the long password!:")
      if len(str(your_password)) == 8 and amount_ticket > amount_possessed:
        print("Please you are not eligible. Check the password or the amount of money you have in your account!\n")
      else:
        amount_left = amount_possessed - amount_ticket
        print("You have successfully spent", amount_ticket, "for the ticket and you have now", amount_left, " in your Lumicash account")
      print("You have " + str(amount_left) + " in your Lumicash account!")
    
    pay_ticket()
  
  elif choice == 6:
    def balance():
      full_password = str(input("Enter your password but letter or symbols only:"))
      full_password1 = int(input("Enter your password but digits only:"))
      your_password = full_password + str(full_password1)
      if len(your_password) < 10:
        print("Please you are not eligible. Check the password or the amount of money you have in your account! Try again!\n")
        balance()
        exit()
      else:
        print("Your password is ", your_password)
        choice = input(" Do you want to log in to see your balance/ money? [yes/no] ?>>>")
        if choice == "yes":
          print("You have successfully loged in!\n")
          print("You have ", amount_possessed, "in your Lumicash account!")  
        elif choice == "no":
          exit()
        else:
          print(">>>>>>>>>>>>You choose the wrong input! Try to spell well!\n")

    balance()

  elif choice == 7:
    def cancel():
      print("You have successfully cancelled the transaction!\n")
      choice = input("Do you really want to cancel this transaction? [yes/no]?>>>")
      if choice == "yes":
        exit()
      elif choice == "no":
        print(" Choose the Services :\n0. send money\n1. withdraw money\n2. Buy airtimes\n3. Pay the seller\n4. Pay bill\n5. Buy tickets\n6.check account balance\n")
        choice = input("Enter your choice: >>>>")
        if choice == 0:
          send_money()
          exit()
        
          
        elif choice == 1:
          withdraw_money()
          exit()
          
        elif choice == 2:
          buy_airtime()
          exit()
          
        elif choice == 3:
          pay_the_seller()
          exit()
          
        elif choice == 4:
          pay_bill()
          exit()
          
        elif choice == 5:
          pay_ticket()
          exit()
          
        elif choice == 6:
          balance()
          exit()
          
        else:
          print("Wrong input! Try again!\n")
          cancel()
          
    cancel()
  else:
    print("Please the choice you made does correspond to the services offered buy us!")
elif code == "*131#":
  print("************************** Welcome to clientel services", name, "******************!\n")
  print("You have :>>>>", amount_possessed,"in your airtime savings account!")
elif code == "*800*7#":
  print("************************** Welcome to debt service", name, "******************!\n")
  print("You are eligible to get a debt\n: \n1.50 \n2.100 \n3.200!")
  choice = int(input("Enter the number of debt you need: >>>>"))
  if choice <= 200:
    print("You have successfully got a debt of", choice, "and you have now", choice)
    exit()
  else:
    print("You have not enough money to get a debt of", choice)
    exit()
    print("THANK YOU FOR TRYING OUR SERVICES!!!!!!!")
elif code == "*100#":
  print("Welcome to the service of the money transaction company!\n \n >>>>>>I am here to guide you in this process as you have chosen *100# to get information about this act of transaction!\n\n1. First step is to enter *163# whenever you want to use mobile cash/ payment as you will be guided by other person at this case\n2. second is whenever you enter the code *131#, you will get the service of your airtime in your phone to make sure you have enough airtime to send or use to call someone! \n3. The last one is the code *800*7#, because we know that always you can't get the airtime, we put this service here to make sure you don't miss any opportunity or you don't talk to your friends because you have run aout airtimes and you are not near our agents!\n")
  ask_user = input(" Are you satisfied with this information so that we can improve it? [yes/no]\n:")
  if ask_user == "yes":
    print("\033[1;32m Thank you for your appreciation of our services, now you can continue as you have enough information of how our services work!")
  else:
    print("\033[1;33m Thank you for your review we are going to improve it, come back tomorrow to get clarification to our office!\n")
  



 
  
    

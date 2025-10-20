#we need rent,food expense,electricity bill from user
#by using number of people in house we will calculate expense
House_Rent = int(input("enter ur monthly house rent  "  ))
food_expense = int(input("enter your monthly food expense " ))
electricity = int(input("enter ur electricity usage  "  ))
charge_perunit = int(input("charge of electricity in ur area  "  ))
total_bill = electricity * charge_perunit
Tenants = int(input("enter the number of people in house "))

Rent_perperson = ( total_bill + House_Rent + food_expense) // Tenants
print("Rent per person : " , Rent_perperson
  )
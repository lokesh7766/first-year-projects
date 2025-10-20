hotel_Menu = {
  'Gobi' : 30,
  'Masala puri ' : 40,
  'pani puri ' :30,
  'Egg rice ' :30,
  'coffe' : 10,
  'Tea' : 10,
}

print("WELCOME TO LOKESH CHATS")
print("Gobi:30\nmasalapuri:40\npanipuri:30\neggrice:30\ncoffe:10\ntea:10")
order_total = 0
item_1 = input("plz enter ur order =  ")
if item_1 in hotel_Menu:
  order_total += hotel_Menu[item_1]
  print(f"ur item {item_1 } has been added to your order")

else:
  print(f"ur ordered {item_1} is not available in our menu")

another_order = input("do you want to add another item? (yes/no) ")
if another_order.lower() == "yes":
    item_2 = input("plz add ur second item = ")
if item_2 in hotel_Menu:
  order_total += hotel_Menu[item_2]
  print(f" ur item {item_2 } has been added to ur order")

else:
     print("it is not available")

print(f" total amount u need to pay is {order_total} ")     


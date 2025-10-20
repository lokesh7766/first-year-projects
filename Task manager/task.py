""" task management app consists of tasks with features like add,delete,view like tha t """
def task():
   tasks = []
   print("welcome to task manager")
   
   total_task = int(input("enter the number of tasks u need:  "))
   for i in range(1,total_task + 1):
      task_name = input(f" enter task {i} =  ")
      tasks.append(task_name)
  
   print(f'todays task are\n {tasks} ')
   while True:
        operation = int(input("Enter 1.add\n2.update\n3.delete\n4.view\n5.exit"))
        if operation == "1":
           add = input("enter task u want to add   =   ")
           tasks.append(add)
           print("task {add} has been successfully added")
        elif operation == "2":
            update_val = ("enter u want to update =  ")
            if update_val in tasks:
               up = input("enter ur new task =  ")
               ind  = tasks.index(update_val)
               tasks[ind] = up
        elif operation == "3":
            del_value = input("enter the deleting task : ")
            if del_value in tasks:
               ind = tasks.index(del_value)
               del tasks[ind]
               print(f"ur task{del_value} has been deleted ")
        elif operation == "4":
            print(f'total tasks = {tasks}')
        elif operation == "5":
            print("closing task manager")
            break
        else:
             print("invalid choice ") 
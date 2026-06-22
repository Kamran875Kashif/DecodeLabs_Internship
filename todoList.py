# Make a todolist with a menu to select if want to add a
# task or want to display a task and use list to store
# data while use dict to define a task


input_value=None
tasks_list=[]
print("..................TodoList................")
print("1. Enter a task")
print("2. Print the tasks\n")
while input_value!=0:

  input_value= int(input("Enter index to input value or enter 0 to exit!!\n"))
  if input_value==0:
    break
  match input_value:
   case 1:
    task = None
    while task !="end":
     task=input("Add a task or input 'end' to exit adding more tasks:\n")
     if task == "end":
      break
     else:
      tasks_list.append({"id":len(tasks_list)+1,"Task":task})
   case 2:
    print("...........Tasks..........\n")
    for task in tasks_list:
      print("ID: ",task["id"])
      print("Task: ", task["Task"],"\n")      
   case _:
      print("Invalid Input")   
      

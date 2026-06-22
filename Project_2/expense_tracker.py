# An expense tracker that adds up expenses and displays total spent.


print("------------Expense Tracker-----------")
print(" ")
item=None
items_track={}
total_expenses=0
while item != "No more items":
  print("Enter the item brought with it's corresponding price and to end entering item enter 'No more items': \n")
  item = input("Enter product name:")
  if item =="No more items":
    break
  price = int(input("Enter the price for item: "))
  items_track[item]=price
  total_expenses+=price

print("----------Expenses list---------\n")
for key, value in items_track.items():
  print("Item: ", key, " Price: ",value)
print("")
print("Total expenses: ", total_expenses)  
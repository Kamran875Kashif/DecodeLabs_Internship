# Create a game that asks three questions and on each correct answer adds a point

print("-----------Guess the Correct Answer---------------\n")
print("Every correct answer gives you 1 score!!\n")
counter=0

input_value = int(input("To start playing game press '1' or to end simply press '0'.\n"))
if input_value ==1:
  
 first_question = input("Which is capital of Belgium?\n")
 if first_question == "Brussels":
  counter+=1
 second_question= input("Which is the deepest point on Earth?\n")
 if second_question == "Mariana Trench":
  counter+=1
 third_question = int(input("Guess the number of colors in a rainbow!!\n"))
 if third_question == 7:
  counter+=1

 if counter == 1:
  print("You guessed one correct answer and your score is: 1")
 elif counter ==2:
  print("You were good, you guessed two correct answers and your score is: 2")
 elif counter==3:
  print("Congratulations!! You guessed all the questions right and scored: 3")
 else:
  print("OOPS!! You Failed.")      

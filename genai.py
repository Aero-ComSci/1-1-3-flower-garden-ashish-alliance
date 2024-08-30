
#user input at the very top 

#import turtle as trtl
#painter = trtl.Turtle()

userinput = input("I draw flowers. What flower and how many would you like me to draw?").strip()

#use a list to split the user input into 2 elemts 

#elemt one is the number 

flower_choice= userinput.split(" ")
i = 0
while i < len(flower_choice):
    if flower_choice[i].isdigit():
        if flower_choice[i] > 30:
            print("Our max on one run is 30. Sorry for this and thank you for understanding")
            num = 30
        else:
            num = flower_choice[i]
            break

        break
    i += 1
#element two is the flower type 

flowers = ["roses", "tulips", "violets", "lilies", "sunflower"]

w = 0
while w < len(flower_choice):
    if flower_choice[w].lower() in flowers:
        flowerType = flower_choice[w]
        break
    
    w += 1

# print(num, flowerType)

# def rose(num, type):
#     painter.forward
    

# wn = trtl.Screen()
# wn.mainloop()

# first we make mae a function to draw flower 
#this funciton will have 5 if and elif statements and will change the colors of the petals only base don the case 

# flower funciton has 3 parts 
#circle 
#stem
#pettles, these are the hardest which we keep till end 


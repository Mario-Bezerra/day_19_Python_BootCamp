from turtle import Turtle , Screen
import random

screen = Screen()
screen.setup(width=600 , height= 400)

game_on = False

user_guess = screen.textinput(title= "Faca sua aposta" ,prompt="Qual tartaruga irá ganhar?" )
color = ["red","orange","green","purple","yellow","blue"]
y_positions = [125,75,25,-25,-75,-125]
all_turtles = []

for turtle_number in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(color[turtle_number])
    turtle.penup()
    turtle.goto(x=-280,y=(y_positions[turtle_number]))
    all_turtles.append(turtle)

if user_guess:
    game_on = True

while game_on:
    for turtle in all_turtles:
        random_number = random.randint(0,10)
        turtle.forward(random_number)
        if turtle.xcor()>280:
            winner = turtle.pencolor()
            game_on = False

if winner == user_guess:
    print(f"You win the {winner} wins")
else:
    print(f"You lose, the winner was {winner}")


screen.exitonclick()

from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")

game_continue = True

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
turtles = []
y_cor = -120

def turtle_line(y):

    for i in colors:
        t = Turtle()
        t.shape("turtle")
        t.color(i)
        turtles.append(t)
        t.penup()
        t.goto(x=-230, y=y)
        y += 50

def clear_screen(turtle_list, y):
    for turtle in turtle_list :
        turtle.penup()
        turtle.goto(x=-230, y=y)
        y += 50

turtle_line(y_cor)

while game_continue:

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?"
                                               " Enter a color:\n(purple, blue, green, yellow, orange, red) ")

    if user_bet in colors:
        is_race_on = True


    while is_race_on:

        for turtle in turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            bet_result = "no"

            if int(turtle.xcor()) >= 230:
                is_race_on = False

                if user_bet == turtle.pencolor():
                    bet_result = screen.textinput(title="Bet Result", prompt=f"You win the bet! {user_bet.title()} turtle wins.\nDo you want to try again? yes/no")
                    # print(f"You win the bet! {user_bet.title()} turtle wins. ")

                else:
                    bet_result = screen.textinput(title="Bet Result",
                                              prompt=f"You lost! {turtle.pencolor().title()} turtle wins.\nDo you want to try again? yes/no")
                # print(f"You lost! {turtle.pencolor().title()} turtle wins.")

                if bet_result == "yes":
                    clear_screen(turtles, y_cor)
                    game_continue = True
                    break
                else:
                    game_continue = False
                    is_race_on = False
                    break

screen.exitonclick()
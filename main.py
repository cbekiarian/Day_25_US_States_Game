import turtle
import pandas
screen = turtle.Screen()
screen.screensize(100,100)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
Bob = turtle.Turtle()
Bob.hideturtle()
Bob.penup()

score = 0
answers = []
while len(answers) <50 :
    answer_state = screen.textinput(title = f"{score}/50Guess the State", prompt= "What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    data = pandas.read_csv("50_states.csv")
    ans = data[data["state"] == answer_state]
    if ans.empty or answer_state in answers:
        print("ok")
        continue

    Bob.goto(int(ans.x.iloc[0]), int(ans.y.iloc[0]))
    Bob.write(answer_state)
    score +=1
    answers.append(answer_state)

res = data[~data.state.isin(answers)]
res.to_csv("States_to_learn.csv")
screen.exitonclick()


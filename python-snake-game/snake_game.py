import turtle
import time
import random

# --- Game Setup ---
# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.setup(width=600, height=600)
wn.bgcolor("darkblue")
wn.tracer(0) # Turns off screen updates

# Game variables
delay = 0.1
score = 0
high_score = 0

# --- Snake Head ---
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkgreen")
head.penup() # Prevents drawing as it moves
head.goto(0, 0)
head.direction = "stop"

# --- Snake Food ---
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red", "darkred")
food.penup()
food.goto(0, 100)

segments = [] # List to store the snake's body segments

# --- Scoreboard ---
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# --- Functions ---
def go_up():
    if head.direction != "s":
        head.direction = "w"

def go_down():
    if head.direction != "w":
        head.direction = "s"

def go_left():
    if head.direction != "d":
        head.direction = "a"

def go_right():
    if head.direction != "a":
        head.direction = "d"

def move():
    if head.direction == "w":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "s":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "a":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "d":
        x = head.xcor()
        head.setx(x + 20)

# --- Keyboard Bindings ---
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# --- Main Game Loop ---
while True:
    wn.update()

    if score < 50:
        delay = 0.1
    elif score < 100:
        delay = 0.08
    elif score < 150:
        delay = 0.05
    else:
        delay = 0.001

    # Check for boundary collisions
    if head.xcor() > 287 or head.xcor() < -287 or head.ycor() > 287 or head.ycor() < -287:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear() # Clear the segments list
        score = 0
        delay = 0.1 # Reset speed
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for food collision
    if head.distance(food) < 20:
        # Move the food to a new random location
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        food.goto(x, y)

        # Add a new segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.shapesize(stretch_wid=0.8, stretch_len=1.0)
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10

        # Update the scoreboard
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
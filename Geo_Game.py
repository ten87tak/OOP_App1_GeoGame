from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.f_point.x < self.x < rectangle.s_point.x \
                and rectangle.f_point.y < self.y < rectangle.s_point.y:
            return True
        else:
            return False


class Rectangle:
    # Each parameter contains a tuple of coordinate:
    def __init__(self, f_point, s_point):
        self.f_point = f_point
        self.s_point = s_point

    def get_area(self):
        # Accessing each value of a tuple using a dot notation:
        area = (self.s_point.x - self.f_point.x) \
               * (self.s_point.y - self.f_point.y)
        return area


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        # Go to a certain coordinate.
        canvas.penup()
        canvas.goto(self.f_point.x, self.f_point.y)

        canvas.pendown()
        canvas.forward(self.s_point.x - self.f_point.x)
        canvas.left(90)
        canvas.forward(self.s_point.y - self.f_point.y)
        canvas.left(90)
        canvas.forward(self.s_point.x - self.f_point.x)
        canvas.left(90)
        canvas.forward(self.s_point.y - self.f_point.y)

        # turtle.done()


class GuiPoint(Point):

    def draw(self, canvas, size=30, color="pink"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

        # turtle.done()


# Get a GUI rectangle:
rectangle = GuiRectangle(Point(randint(0, 100), randint(0, 100)),
                         Point(randint(101, 200), randint(101, 200)))

# Print the rectangle's coordinates:
print("Rectangle Coordinates: ",
      rectangle.f_point.x, ", ",
      rectangle.f_point.y, " and ",
      rectangle.s_point.x, ", ",
      rectangle.s_point.y)

# Get a point coordinate and an area from a user:
user_guess_point = GuiPoint(int(input("Guess X: ")), int(input("Guess Y: ")))
user_guess_area = float(input("Guess the area: "))

# Get a result of the game:
print("Your point was inside the rectangle: ",
      user_guess_point.falls_in_rectangle(rectangle))

if user_guess_area == rectangle.get_area():
    print(f"Your guessed right! The area of this rectangle is {user_guess_area}")

else:
    print(f"Your area is off by {rectangle.get_area() - user_guess_area}")


my_turtle = turtle.Turtle()
rectangle.draw(canvas=my_turtle)
user_guess_point.draw(canvas=my_turtle)
turtle.done()


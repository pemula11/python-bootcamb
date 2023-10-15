from turtle import Turtle, Screen
from prettytable import PrettyTable


# Timmy = Turtle()
# Timmy.shape('turtle')
# Timmy.color("#ff0000")
# my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "water", "fire"])
table.align = "l"
print(table)
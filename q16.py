'''
Imagine you are creating a Super Mario game. You need to define a
class to represent Mario. What would it look like? If you aren't familiar
with SuperMario, use your own favorite video or board game to model
a player.
'''

class SuperMario():

    def __init__(self):
        self.name = "SuperMario"
        self.color = "Red"
        self.position = 0
        self.left = int(input("Enter a number to go left"))
        self.right = int(input("Enter a number to go right"))

    def display_position(self):
        print(f"Your name is {self.name}")
        print(f"Your color is {self.color}")
        return f"Your default postion is in {self.position} "

    def left_movement(self):
        left = self.position - self.left 
        return f"You move {left} to left"

    def right_movement(self):
        right = self.position + self.right
        return f"You move {right} to right"    


mario = SuperMario()
print(mario.display_position())
print(mario.left_movement())
print(mario.right_movement())
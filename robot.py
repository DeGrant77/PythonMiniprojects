class Robot:

    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100

    def move_up(self):
        if self.fuel >= 5:
            self.y -= 1
            self.fuel -= 5
        else:
            print("Insufficient to perform action")

    def move_down(self):
        if self.fuel >= 5:
            self.y += 1
            self.fuel -= 5
        else:
            print("Insufficient to perform action")

    def move_left(self):
        if self.fuel >= 5:
            self.x -= 1
            self.fuel -= 5
        else:
            print("Insufficient to perform action")

    def move_right(self):
        if self.fuel >= 5:
            self.x += 1
            self.fuel -= 5
        else:
            print("Insufficient to perform action")

    def laser(self):
        if self.fuel >= 15:
            self.fuel -= 15
            print("Pew! Pew!")
        else:
            print("Insufficient to perform action")

    def display_status(self):
        print("({},{}) - Fuel: {}".format(self.x, self.y, self.fuel))

    def prompt(self):
        print("Robot Game")
        print("Available Commands: up, down, left, right, fire, status and quit")
        self.prompt = input("Enter a command: ").lower()
        if self.prompt == "up":
            self.move_up()
        elif self.prompt == "down":
            self.move_down()
        elif self.prompt == "left":
            self.move_left()
        elif self.prompt == "right":
            self.move_right()
        elif self.prompt == "fire":
            self.laser()
        elif self.prompt == "status":
            self.display_status()
        elif self.prompt == "quit":
            print("Goodbye")
        return self.prompt


def main():
    zod = Robot()
    while zod:
        if Robot.prompt(zod) == "quit":
            break


if __name__ == "__main__":
    main()

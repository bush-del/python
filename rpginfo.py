class RPGInfo():

    author = "Anonymous"
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print("Welcome to " + self.title)


    @staticmethod
    def info():
        print("Made using the OOP RPG game creator (c) me")
        print("You will have to collect 3 items- a pair of glasses,a bone and a book. But remember you are not going to be alone. Make sure to use the commands- {talk/speak/directions(east,west,north and south)/fight/hug/take} to procede. /n Pshh..your backpack has a gun, sword, cookies and water")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)


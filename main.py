from room import Room
from character import Enemy, Friend
from rpginfo import RPGInfo
from item import Item

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "Raspberry Pi Foundation"

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

bedroom=Room("Bedroom")
bedroom.set_description("A cozy but spooky place to rest with skeletons on the bed")

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(bedroom, "east")
ballroom.link_room(dining_hall, "east")
bedroom.link_room(dining_hall,"west")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("gun")
dining_hall.set_character(dave)

davi = Enemy("Davi", "Another smelly zombie")
davi.set_conversation("Brrlgrh...urgghh..wanna dance?..")
davi.set_weakness("water")
bedroom.set_character(davi)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
ballroom.set_character(catrina)

glasses = Item("glasses")
glasses.set_description("A pair of old glasses")
ballroom.set_item(glasses)

book = Item("book")
book.set_description("The book entitled 'History of Spooky Castle'")
dining_hall.set_item(book)

bone=Item("bone")
bone.set_description("Replica chew bone of the dead King's dog Emperio")
bedroom.set_item(bone)

current_room = kitchen
backpack = ["gun","sword","cookies","water"]

dead = False
while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command in ["talk","speak"]:
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            inhabitant.talk()

    elif command == "fight":
        # You can check whether an object is an instance of a particular
        # class with isinstance() - useful! This code means
        # "If the character is an Enemy"
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)

RPGInfo.credits()

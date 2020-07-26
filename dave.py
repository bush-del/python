from character import Enemy
dave=Enemy("dave","a smelly zombie")
davi=Enemy("davi","another smelly zombie")
dave.describe()
davi.describe()
dave.set_conversation("hey")
davi.set_conversation("what weapon have you got?")
dave.talk()
davi.talk()

dave.set_weakness("sword")
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)

davi.set_weakness("gun")
print("okay, but what will you fight me with?")
fight_with = input()
davi.fight(fight_with)

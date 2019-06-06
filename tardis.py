from sys import exit
from textwrap import dedent
from time import sleep

def cls():
    print("\n" * 100)
    
class Room(object):
    
    def __init__(self):
        self.visited = False
        self.objects = []
        
    def title(self):
        cls()
        print("This room has no title yet")
    
    def v_description(self):
        print("Room has no verbose description yet")
        
    def north(self):
        print("\nYou can't go that way.\n")
        
    def south(self):
        print("\nYou can't go that way.\n")
        
    def west(self):
        print("\nYou can't go that way.\n")
        
    def east(self):
        print("\nYou can't go that way.\n") 

    def up(self):
        print("\nYou can't go that way.\n")
        
    def down(self):
        print("\nYou can't go that way.\n")

    def enter(self):
        if not self.visited:
            self.v_description()
            self.visited = True
        else:
            self.s_description()


class TardisControlRoom(Room):
    
    def title(self):
        cls()
        print("\nThe TARDIS Control Room")
        
    def v_description(self):
        print(dedent("""
        You are standing in the control room of a type 40 TARDIS. It has
        six white walls covered with glowing white round panels in a
        hexagonal pattern. On one wall there is a viewing monitor that is
        currently closed.
        Filling the center of the room is a large control console with six
        large trapazoidal control panels filled with many flashing lights,
        dials, readouts, buttons, switches and levers. In the center is the
        clear cylindrical time roter currently stopped.
        To the west are the large doors that are open to the outside, to
        the east a smaller door leading to the inner corridors of the TARDIS.
        The Doctor is here fiddling with some controls on the console and
        looking perplexed."""))
    
    def s_description(self):
        print(dedent("""
        The Doctor is here fiddling with some controls on the console and
        looking perplexed."""))

    def east(self):
        return(tardis_interior_corridorA)


class TardisInteriorCorridorA(Room):
    
    def title(self):
        cls()
        print("\nTARDIS Interior Corridor")
        
    def v_description(self):
        print(dedent("""
        You come to an intersection of the corridors, from here you can go
        north, south, west, or east. All of the corridors look the same to you."""))

    def s_description(self):
        print(dedent("""
        You come to an intersection of the corridors, from here you can go
        north, south, west, or east. All of the corridors look the same to you."""))



class Hero(object):

    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.pockets = []

    def inventory(self):
        print("\nYou are carrying:")
        if self.pockets:
            for i in self.pockets:
                print(f"a {i}")
            print()
        else:
            print("nothing\n")


def main ():

    tardis_control_room = TardisControlRoom()
    tardis_interior_corridorA = TardisInteriorCorridorA()
    u_name = input("What is your name?\n> ")
    companion = Hero(u_name, tardis_control_room)
    tardis_control_room.enter()
    while True:
        action = input("> ").lower().strip()
        if action == "e" or "east" or "go e" or "go east":
            next_room = companion.current_room.east()
            if next_room != companion.current_room:
                companion.current_room = next_room
                companion.current_room.enter()

main()

#print(companion.name)
#print(companion.current_room)
#companion.inventory()
#
#companion.pockets.append("sonic screwdriver")
#companion.pockets.append("key card")
#
#companion.inventory()


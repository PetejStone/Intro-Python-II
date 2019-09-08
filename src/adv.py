from room import Room
from player import Player
# Declare all the rooms
# class Room:
#     def __init__(self, name, desc):
#         self.name = name
#         self.items = []
#         self.desc = desc
      

#     def __str__(self):
#         return f"{self.name}: {self.items}"
   
#     def __repr__(self):
#         return f"Rooms({repr(self.name)})"


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#print(Room("outside", "it's cold"))
## Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

print(room['foyer'].e_to)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# outside = Room('outside', 'you are outside')
# print(outside.name)
#player = Player('player 1', room['outside'])
current_room = room['outside']

quit = False
while not quit:

    command = input(f"\n(S)elect a Direction: You are now - {current_room}\n(Q)uit\n\nCommand: ")

    command = command.lower().strip()  # normalize input
    
    if command == '':
        continue

    command = command[0]

    if command == 'q':  # quit
        quit = True

    elif command == 's': # select
        direction = input("Enter direction (n,s,e,w): ").strip()
        direction = direction.lower().strip()  # normalize input
        direction = direction[0]

        # room[f"{current_room}"]
        if direction == "n":
            if f"{current_room.name}" == f"{current_room.n_to}":
                print('>>>>>>>You cannot go this way')
            else:
                current_room = current_room.n_to
                print(f"You have entered: {current_room}")
        
        elif direction == "e":
            if f"{current_room.name}" == f"{current_room.e_to}":
                print('>>>>>>>You cannot go this way')
            else:
                current_room = current_room.e_to
                print(f"You have entered: {current_room}")
        elif direction == "s":
            if f"{current_room.name}" == f"{current_room.s_to}":
                print('>>>>>>>You cannot go this way')
            else:
                current_room = current_room.s_to
                print(f"You have entered: {current_room}")
        elif direction == "w":
            if f"{current_room.name}" == f"{current_room.w_to}":
                print('>>>>>>>You cannot go this way')
            else:
                current_room = current_room.w_to
                print(f"You have entered: {current_room}")
            
       
        
       

    
      

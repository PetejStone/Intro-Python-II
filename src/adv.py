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

    'foyer':    Room("Foyer", """Dim light filters in from the South. Dusty
passages run North and East."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the North, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from West
to North. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the South."""),
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
current_room = room['outside'] #current room they are in
message = '' #message displayed to user if they can't go a direction or enter invalid command
quit = False
while not quit:

    command = input(f"\nSelect a Direction:\n\n>>> You are now - {current_room}\n>>> {current_room.description}\n{message}\n(Q)uit\n\nCommand: ").strip() # strips all trailing letters and leaves the first

    command = command.lower().strip()  # normalize input to always be lowercase and strip any trailing letters
    
    if command == '':  #if input is empty do nothing
        continue

    command = command[0]

    if command == 'q':  # quit
        quit = True

  

        # room[f"{current_room}"]
    if command == "n":
        if f"{current_room.name}" == f"{current_room.n_to}": #if the direction the user put in is the same room (this happens when a room isn't available in that dir. Entering it again would result in an error)
            message = '>>>>>>> You cannot go this way'
        else:
            current_room = current_room.n_to
            message = ''
    
    elif command == "e":
        if f"{current_room.name}" == f"{current_room.e_to}":
            message = '>>>>>>> You cannot go this way'
        else:
            current_room = current_room.e_to
            message = ''
    elif command == "s":
        if f"{current_room.name}" == f"{current_room.s_to}":
            message = '>>>>>>> You cannot go this way'
        else:
            current_room = current_room.s_to
            message = ''
    elif command == "w":
        if f"{current_room.name}" == f"{current_room.w_to}":
            message = '>>>>>>> You cannot go this way'
        else:
            current_room = current_room.w_to
            message = ''
    else:
        message = '>>>>>> Please enter a valid command'
            
       
        
       

    
      

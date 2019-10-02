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
                     "North of you, the cave mount beckons", ['rock']),

    'foyer':    Room("Foyer", """Dim light filters in from the South. Dusty
passages run North and East.""", ['quiver', 'knife']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the North, a light flickers in
the distance, but there is no way across the chasm.""", ['drinking pouch', 'map', 'meat']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from West
to North. The smell of gold permeates the air.""", ['arrows', 'cloak', 'tent']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the South.""", ['bow', 'potion', 'arrowhead']),
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

#print(room['outside'].items)
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
browsing = False
signed_in = False
name = ''
player = Player(name,current_room)
satchel_open = False
quit = False
while not quit:
    if signed_in == False:
        name = input(f"Please enter your name to start: ") #
        signed_in = True
    else:
        pass

    if browsing == True:
        command = input(f"\nSelect a Direction:\n\n>>> {name}, you are at - {current_room}\n>>> {current_room.description}\n{message}\n(I)tems holding\n(B)rowse room\n(R)eturn to previous menu\n(Q)uit\n\nPick up item (type name of item): ").lower() # strips all trailing letters and leaves the first
    elif satchel_open == True:
        command = input(f"\nSelect a Direction:\n\n>>> {name}, you are at - {current_room}\n>>> {current_room.description}\n{message}\n(I)tems holding\n(D)rop item\n(R)eturn to previous menu\n(Q)uit\n\nCommand: ").lower() # strips all trailing letters and leaves the first
    else:
        command = input(f"\nSelect a Direction:\n\n>>> {name}, you are at - {current_room}\n>>> {current_room.description}\n{message}\n(I)tems holding\n(B)rowse room\n(Q)uit\n\nCommand: ").strip() # strips all trailing letters and leaves the first
        command = command.lower().strip()  # normalize input to always be lowercase and strip any trailing letters
        command = command[0]
    
    if command == '':  #if input is empty do nothing
        continue


    if command == 'q':  # quit
        quit = True
        signed_in = False


    
   
        


    if command == "n":
        browsing = False
        satchel_open = False
        if f"{current_room.name}" == f"{current_room.n_to}": #if the direction the user put in is the same room (this happens when a room isn't available in that dir. Entering it again would result in an error)
            message = '>>>>>>> You cannot go this way'
        else:
            current_room = current_room.n_to
            message = ''
    
    elif command == "e":
        browsing = False
        satchel_open = False
        if f"{current_room.name}" == f"{current_room.e_to}":
            message = '>>>>>>> You cannot go this way'
        else:
            current_room = current_room.e_to
            message = ''
    elif command == "s":
        browsing = False
        satchel_open = False
        if f"{current_room.name}" == f"{current_room.s_to}":
            message = '>>>>>>> You cannot go this way'
        else:
            current_room = current_room.s_to
            message = ''
    elif command == "w":
        browsing = False
        satchel_open = False
        if f"{current_room.name}" == f"{current_room.w_to}":
            message = '>>>>>>> You cannot go this way'
        else:
            current_room = current_room.w_to
            message = ''
    elif command == "b":
        browsing = True
        satchel_open = False
        if current_room.items == []:
            message = '>>> No items to be found'
        else:
            message = f'>>> While browing, you find these items:\n    {current_room.items}\n'
    elif command == "i":
        browsing = False
        satchel_open = True
        if player.items == []:
            message = '>>> You are not holding any items'
        else:
            message = f'>>> You are currently holding: {player.items}\n'
    elif command == "d":
        browsing = False
        satchel_open = True
        prompt = input(f"Enter name of item you want to drop: ").lower() # strips all trailing letters and leaves the first
        if prompt in f"{player.items}":
            player.drop_item(prompt)
            current_room.get_item(prompt)
            message = f">>> You have dropped {prompt}"
        else:
            message = ">>> You do not have an item by that name"
    elif command == "r":
        browsing = False
        satchel_open = False
    elif command in f"{current_room.items}":
        if len(player.items) < 5:
            message = f'>>> You have picked up {command}\n'
            player.get_item(command)
            current_room.drop_item(command)
            browsing = False
            print(player.items)
        else:
            message = '>>> You are holding the max number of items. You must drop something to pick this up.'

    else:
        browsing = False
        message = '>>>>>> Please enter a valid command'
            
       
        
       

    
      

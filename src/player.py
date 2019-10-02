# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,player, current_room, items=[]):
        self.player = player
        self.current_room = current_room
        self.items = items
        print(f"Room:{self.current_room}")
        print(f"Player:{self.player}")
    
    def __repr__(self):
        return f"Room: {repr(self.current_room)}\nPlayer: {repr(self.player)}"

    def get_item(self, item):
        self.items.append(item)


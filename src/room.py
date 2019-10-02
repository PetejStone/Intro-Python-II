# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = self.name
        self.s_to = self.name
        self.n_to = self.name
        self.e_to = self.name
        self.s_to = self.name
        self.w_to = self.name
        self.n_to = self.name
        self.s_to = self.name
    def __repr__(self):
        return f"{repr(self.name)}"

    def get_item(self, item):
        self.items.append(item)
        
    def drop_item(self, item):
        self.items.remove(item)

    def rooms(self):
        pass
        # if self.name == 'foyer':
        #     self.n_to == 'overlook'
        #     self.s_to == 'outside'
        #     self.e_to == 'narrow'
        # elif self.name == 'outside':
        #     self.n_to == 'foyer'
        # elif self.name == 'overlook':
        #     self.s_to == 'foyer'
        # elif self.name == 'narrow':
        #     self.w_to == 'foyer'
        #     self.n_to == 'teasure'
        # elif self.name == 'treasure':
        #     self.s_to == 'narrow'

         




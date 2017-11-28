#This file stores all the different types of room
class Room():
    """The generic base class for all tiles"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        """The text shown to the user when you enter a room"""
        raise NotImplementedError()


class Corridor(Room):
    def intro_text(self):
        return """You are in a corridor. Dark shapes flicker on the wall"""

class DeadEnd(Room):
    def intro_text(self):
        return """You have reached the end of the corridor"""

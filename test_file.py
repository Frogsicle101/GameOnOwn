#This is a test file
print("Hello World")
import tiles

room = tiles.Corridor(0, 0)
room2 = tiles.DeadEnd(1, 0)
rooms = [room, room2]
x = 0
while x != 5:
    x = int(input("X\n"))
    print(rooms[x].intro_text())

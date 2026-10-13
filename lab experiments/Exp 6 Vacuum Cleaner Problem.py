
rooms = {'A': 'Dirty', 'B': 'Dirty'}
position = 'A'

while 'Dirty' in rooms.values():
    print("Vacuum is in room", position)

    if rooms[position] == 'Dirty':
        print("Cleaning room", position)
        rooms[position] = 'Clean'

    position = 'B' if position == 'A' else 'A'

print("All rooms are clean!")
print(rooms)

# There are 100 rooms in a row, each containing a light. The light in every room is turned off.
# 100 wolves walk through the rooms, in order, one at a time flipping switches. Wolf 1 flips
# every switch. Wolf 2 flips every other. Wolf 3 flips every third. Etc.
# After all 100 wolves have walked through, how many lights are left on?

rooms = []

roomPointer = 100
wolfPointer = 1

def printRooms(rooms):
	i = 0
	print('|', end='')
	while i < len(rooms):
		if rooms[i]:
			print('1', end='')
		else:
			print(' ', end='')
		i += 1
	print('|')

while roomPointer > 0:
	rooms.append(False)
	roomPointer -= 1

print('rooms:', str(len(rooms)), sep=' ')
printRooms(rooms)

while wolfPointer <= 100:
	print('Wolf', str(wolfPointer), sep='#')
	roomPointer = 0;
	while roomPointer < 100:
		if (roomPointer + 1) % wolfPointer == 0:
			rooms[roomPointer] = not rooms[roomPointer]
		roomPointer += 1
	printRooms(rooms)
	wolfPointer += 1
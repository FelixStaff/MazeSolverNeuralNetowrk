import random
import time
import Maze_solver as ms
import numpy as np
## Functions
List_mazes = [[],[]]
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 32
width = 32
def printMaze(maze):
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(str(maze[i][j]), end="")
			elif (maze[i][j] == 'c'):
				print(str(maze[i][j]), end="")
			else:
				print(str(maze[i][j]), end="")
			
		print()

# Find number of surrounding cells
def surroundingCells(rand_wall, nmaze):
	s_cells = 0
	if (nmaze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (nmaze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (nmaze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (nmaze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1

	return s_cells
cant_maces = 1000
def create_maze(nmaze):
	## Main code
	# Init variables
	# Denote all cells as unvisited
	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited)
		nmaze.append(line)

	# Randomize starting point and set it a cell
	starting_height = int(random.random()*height)
	starting_width = int(random.random()*width)
	if (starting_height == 0):
		starting_height += 1
	if (starting_height == height-1):
		starting_height -= 1
	if (starting_width == 0):
		starting_width += 1
	if (starting_width == width-1):
		starting_width -= 1

	# Mark it as cell and add surrounding walls to the list
	nmaze[starting_height][starting_width] = cell
	walls = []
	walls.append([starting_height - 1, starting_width])
	walls.append([starting_height, starting_width - 1])
	walls.append([starting_height, starting_width + 1])
	walls.append([starting_height + 1, starting_width])

	# Denote walls in maze
	nmaze[starting_height-1][starting_width] = 'w'
	nmaze[starting_height][starting_width - 1] = 'w'
	nmaze[starting_height][starting_width + 1] = 'w'
	nmaze[starting_height + 1][starting_width] = 'w'

	while (walls):
		# Pick a random wall
		rand_wall = walls[int(random.random()*len(walls))-1]

		# Check if it is a left wall
		if (rand_wall[1] != 0):
			if (nmaze[rand_wall[0]][rand_wall[1]-1] == 'u' and nmaze[rand_wall[0]][rand_wall[1]+1] == 'c'):
				# Find the number of surrounding cells
				s_cells = surroundingCells(rand_wall, nmaze=nmaze)

				if (s_cells < 2):
					# Denote the new path
					nmaze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (nmaze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							nmaze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])


					# Bottom cell
					if (rand_wall[0] != height-1):
						if (nmaze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							nmaze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):	
						if (nmaze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							nmaze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
				

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check if it is an upper wall
		if (rand_wall[0] != 0):
			if (nmaze[rand_wall[0]-1][rand_wall[1]] == 'u' and nmaze[rand_wall[0]+1][rand_wall[1]] == 'c'):

				s_cells = surroundingCells(rand_wall, nmaze=nmaze)
				if (s_cells < 2):
					# Denote the new path
					nmaze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (nmaze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							nmaze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):
						if (nmaze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							nmaze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])

					# Rightmost cell
					if (rand_wall[1] != width-1):
						if (nmaze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							nmaze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check the bottom wall
		if (rand_wall[0] != height-1):
			if (nmaze[rand_wall[0]+1][rand_wall[1]] == 'u' and nmaze[rand_wall[0]-1][rand_wall[1]] == 'c'):

				s_cells = surroundingCells(rand_wall,nmaze=nmaze)
				if (s_cells < 2):
					# Denote the new path
					nmaze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					if (rand_wall[0] != height-1):
						if (nmaze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							nmaze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[1] != 0):
						if (nmaze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							nmaze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
					if (rand_wall[1] != width-1):
						if (nmaze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							nmaze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)


				continue

		# Check the right wall
		if (rand_wall[1] != width-1):
			if (nmaze[rand_wall[0]][rand_wall[1]+1] == 'u' and nmaze[rand_wall[0]][rand_wall[1]-1] == 'c'):

				s_cells = surroundingCells(rand_wall, nmaze=nmaze)
				if (s_cells < 2):
					# Denote the new path
					nmaze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					if (rand_wall[1] != width-1):
						if (nmaze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							nmaze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])
					if (rand_wall[0] != height-1):
						if (nmaze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							nmaze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[0] != 0):	
						if (nmaze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							nmaze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Delete the wall from the list anyway
		for wall in walls:
			if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
				walls.remove(wall)
	#function that convert the maze in numpy array
	for i in range(0, height):
		for j in range(0, width):
			if (nmaze[i][j] == 'u'):
				nmaze[i][j] = 'w'
	for i in range(0, width):
		if (nmaze[1][i] == 'c'):
			nmaze[0][i] = 'c'
			break
	for i in range(width-1, 0, -1):
		if (nmaze[height-2][i] == 'c'):
			nmaze[height-1][i] = 'c'
			break
def numpy_maze(maze):
	n_maze = np.array(maze)
	return n_maze
	#turn the maze into a 0 and 1 array
def maze_to_array(maze):
	maze_array = np.zeros((32,32))
	for i in range(height):
		for j in range(width):
			if maze[i][j] == 'w':
				maze_array[i][j] = 1
			elif maze[i][j] == 'c':
				maze_array[i][j] = 0
	return maze_array
	#function that convert a number matrix into a string matrix
def convert_string(maze):
	maze_string = np.zeros((height,width),dtype=str)
	for i in range(height):
		for j in range(width):
			if maze[i][j] == 1:
				maze_string[i][j] = '#'
			else:
				maze_string[i][j] = '.'
	return maze_string
	#function that convert a string matrix into a number matrix


def saveCSV(array, filename):
    path = "./" + filename
    np.save(path, array)

def main():
	counted = 0
	# Mark the remaining unvisited cells as walls
	for epoch in range(10000):
		mmaze = []
		create_maze(nmaze=mmaze)
		#selct a random start and end point
		#print("\n")
		for i in range(0, height):
			for j in range(0, width):
				if (mmaze[i][j] == 'u'):
					mmaze[i][j] = 'w'
		start = [random.randint(0,height-1),random.randint(0,width-1)]
		end = [random.randint(0,height-1),random.randint(0,width-1)]
		Smaze = ms.Maze(32,32,start,end,maze = convert_string(maze_to_array(mmaze)))
		#printMaze(Smaze.maze)
		m = Smaze.make_new_maze_with_path()	
		#printMaze(m)
		if Smaze.posible == True:
			counted += 1
			List_mazes[1].append(m)
			List_mazes[0].append(Smaze.maze)
		# Print final maze
		if epoch % 1000 == 0:
			print("Saving:[", epoch/10000*100 ,"%", "] and [", counted, "]")
			printMaze(m)
	#print(".", end="")
	#generate the maze
	#save the maze in a csv file
	print("Generating mazes...")
	saveCSV(List_mazes, "ListMaze.npy")
if __name__ == "__main__":
	main()


import copy
import random
from node import Node
from timer import Timer


def main():
	# val = input("Enter your value: ")
	val = '((6; 1; 2); (7; 8; 3); (5; 4; 9))'
	# val = '((3; 2); (4; 1))'
	input_list = get_list(parse_input(val))
	
	node = Node(input_list, [], 0, 0)
	start_dfs(node)

def start_dfs(start_node):
	solution_node = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	# solution_node = [[1, 2], [3, 4]
	open_stack = []
	closed_stack = []
	max_depth = 10
	t = Timer()
	t.start()

	open_stack.append(start_node)

	while(len(open_stack) > 0):

		if t.getTime() >= 60:
			t.maxTime()
			return False

		if len(closed_stack) == 0:
			current_node = open_stack.pop()
			closed_stack.append(current_node)
		else:
			#print(current_node.state)
			closed_stack.append(current_node)
			current_node = open_stack.pop()

		if(current_node.state == solution_node):
			print("*************************************************")
			print("Solution State Reached: " + str(current_node.state))
			print("Parent State: " + str(current_node.parent.state))
			print("*************************************************")
			output_solution_path(current_node)
			output_search_path(closed_stack)
			elapsed_time = t.getTime()
			t.stop()
			return True, elapsed_time, len(closed_stack), current_node.depth+1, len(closed_stack)

		while(current_node.depth < max_depth):
			if t.getTime() >= 60:
				t.maxTime()
				return False

			#print(current_node.state)
			if(current_node.state == solution_node):
				print("*************************************************")
				print("Solution State Reached: " + str(current_node.state))
				print("Parent State: " + str(current_node.parent.state))
				print("*************************************************")
				output_solution_path(current_node)
				output_search_path(closed_stack)
				elapsed_time = t.getTime()
				t.stop()
				return True, elapsed_time, len(closed_stack), current_node.depth+1, len(closed_stack)

			children = generateChildren(current_node)

			for state in children:
				if t.getTime() >= 60:
					t.maxTime()
					return False
				if current_node.depth == 0:
					open_stack.append(state)
				elif not is_in_stack(state.state, closed_stack):
					open_stack.append(state)
			
			closed_stack.append(current_node)

			#Ensures that the function doesnt throw an error
			#when trying to pop at the end of the search
			if(len(open_stack) == 0):
				print("No Solution Found..")
				return False

			current_node = open_stack.pop()

			if(current_node.state == solution_node):
				print("*************************************************")
				print("Solution State Reached: " + str(current_node.state))
				print("Parent State: " + str(current_node.parent.state))
				print("*************************************************")
				output_solution_path(current_node)
				output_search_path(closed_stack)
				elapsed_time = t.getTime()
				t.stop()
				return True, elapsed_time, len(closed_stack), current_node.depth+1, len(closed_stack)

def output_solution_path(node):
	new_file = open("output_files/dfs/solution_path.txt","w+")
	dimension = len(node.state)
	solution_path = node.get_solution_path()
	ctr = 0

	for state in solution_path:
		while(ctr < dimension):
			new_file.write(str(state.state[ctr]) + "\n")
			ctr +=1

		new_file.write("\n")
		ctr = 0

def output_search_path(closed_stack):
	new_file = open("output_files/dfs/search_path.txt","w+")
	dimension = len(closed_stack[0].state)
	ctr = 0

	for i in reversed(closed_stack):
		while(ctr < dimension):
			new_file.write(str(i.state[ctr]) + "\n")
			ctr +=1

		new_file.write("\n")
		ctr = 0
			
def is_in_stack(state, stack):
	for i in range(len(stack)):
		if state == stack[i].state:
			return True
	return False

# convert input string to a tuple
def parse_input(inputStr):
	inputStr = eval(inputStr.replace(';', ','))
	return inputStr

# converts tuple to a list, since tuples are immutable
def get_list(tup):
	return list(map(get_list, tup)) if isinstance(tup, (list, tuple)) else tup

# returns index of a number in a nested list as a list of size 2
def get_index(input_list, num):
	for sub_list in input_list:
		if num in sub_list:
			return (input_list.index(sub_list), sub_list.index(num))
	raise ValueError("'{num}' is not in list".format(num=num))

# -----------------------SWAPING METHODS-----------------------
def swap_left(input_list, current_index):
	list_copy = copy.deepcopy(input_list)
	num_temp = list_copy[current_index[0]][current_index[1]+1]
	list_copy[current_index[0]][current_index[1] +
								1] = list_copy[current_index[0]][current_index[1]]
	list_copy[current_index[0]][current_index[1]] = num_temp
	return list_copy


def swap_right(input_list, current_index):
	list_copy = copy.deepcopy(input_list)
	num_temp = list_copy[current_index[0]][current_index[1]-1]
	list_copy[current_index[0]][current_index[1] -
								1] = list_copy[current_index[0]][current_index[1]]
	list_copy[current_index[0]][current_index[1]] = num_temp
	return list_copy

def swap_up(input_list, current_index):
	list_copy = copy.deepcopy(input_list)
	num_temp = list_copy[current_index[0]-1][current_index[1]]
	list_copy[current_index[0]-1][current_index[1]
								  ] = list_copy[current_index[0]][current_index[1]]
	list_copy[current_index[0]][current_index[1]] = num_temp
	return list_copy


def swap_down(input_list, current_index):
	list_copy = copy.deepcopy(input_list)
	num_temp = list_copy[current_index[0]+1][current_index[1]]
	list_copy[current_index[0]+1][current_index[1]
								  ] = list_copy[current_index[0]][current_index[1]]
	list_copy[current_index[0]][current_index[1]] = num_temp
	return list_copy

# -------------SWAP CHECKING METHODS-------------

def can_swap_left(current_index, dimension):
	if(current_index[1] == dimension - 1):
		return False
	else:
		return True


def can_swap_right(current_index):
	if(current_index[1] == 0):
		return False
	else:
		return True

def can_swap_up(current_index):
	if(current_index[0] == 0):
		return False
	else:
		return True

def can_swap_down(current_index, dimension):
	if(current_index[0] == dimension - 1):
		return False
	else:
		return True

# Generate all 12 child nodes for given parent node

def generateChildren(parent_node):
	input_list = parent_node.state
	possible_moves = []
	dimension = len(input_list)
	for row in input_list:
		for j in row:
			index = get_index(input_list, j)
			if(can_swap_left(index, dimension)):
				move = swap_left(input_list, index)
				if move not in possible_moves:
					possible_moves.append(move)
			if(can_swap_right(index)):
				move = swap_right(input_list, index)
				if move not in possible_moves:
					possible_moves.append(move)
			if(can_swap_up(index)):
				move = swap_up(input_list, index)
				if move not in possible_moves:
					possible_moves.append(move)
			if(can_swap_down(index, dimension)):
				move = swap_down(input_list, index)
				if move not in possible_moves:
					possible_moves.append(move)

	nodes = create_nodes(possible_moves, parent_node)
	random.shuffle(nodes)
	return nodes


def create_nodes(states_list, parent_node):
	nodes = []
	for state in states_list:
		node = Node(state, parent_node, parent_node.depth+1,0)
		nodes.append(node)

	return nodes


if __name__ == '__main__':
	main()

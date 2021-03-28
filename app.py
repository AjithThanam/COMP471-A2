from dfs import start_dfs
from id import start_id
from astar1 import start_a1
from astar2 import start_a2
from node import Node

def main():
	list = generate_inputs()
	new_file = open("output_files/analysis.txt","w+")
	no_solution_counter = 0
	execution_time = 0
	total_cost = 0
	solution_len = 0
	search_len = 0
	success = False

	for input in list:
		node = Node(input, [], 0, 0)
		success, temp_time, temp_search, temp_soln, temp_cost = start_dfs(node)
		if success:
			execution_time += temp_time
			search_len += temp_search
			solution_len += temp_soln
			total_cost += temp_cost
		else:
			no_solution_counter += 1

	write_analysis(no_solution_counter, execution_time, total_cost, solution_len, search_len, "Depth-First Search")

	no_solution_counter = 0
	execution_time = 0
	total_cost = 0
	solution_len = 0
	search_len = 0
	success = False

	for input in list:
		node = Node(input, [], 0, 0)
		success, temp_time, temp_search, temp_soln, temp_cost = start_id(node)
		if success:
			execution_time += temp_time
			search_len += temp_search
			solution_len += temp_soln
			total_cost += temp_cost
		else:
			no_solution_counter += 1
	
			
	write_analysis(no_solution_counter, execution_time, total_cost, solution_len, search_len, "Iterative-Deepening Search")

	no_solution_counter = 0
	execution_time = 0
	total_cost = 0
	solution_len = 0
	search_len = 0
	success = False

	for input in list:
		node = Node(input, [], 0, 0)
		success, temp_time, temp_search, temp_soln, temp_cost = start_a1(node)
		if success:
			execution_time += temp_time
			search_len += temp_search
			solution_len += temp_soln
			total_cost += temp_cost
		else:
			no_solution_counter += 1
	
			
	write_analysis(no_solution_counter, execution_time, total_cost, solution_len, search_len, "A star 1 - Manhattan")

	no_solution_counter = 0
	execution_time = 0
	total_cost = 0
	solution_len = 0
	search_len = 0
	success = False

	for input in list:
		node = Node(input, [], 0, 0)
		success, temp_time, temp_search, temp_soln, temp_cost = start_a2(node)
		if success:
			execution_time += temp_time
			search_len += temp_search
			solution_len += temp_soln
			total_cost += temp_cost
		else:
			no_solution_counter += 1
	
			
	write_analysis(no_solution_counter, execution_time, total_cost, solution_len, search_len, "A star 2 - Hamming")

def generate_inputs():
	input_file = open("input_files/inputs.txt", "r")
	list_of_inputs = []

	for input in input_file:
		list_of_inputs.append(get_list(parse_input(input)))
	
	return list_of_inputs

def write_analysis(no_solution_counter, execution_time, total_cost, solution_len, search_len, algorithm_name):

	new_file = open("output_files/analysis.txt","a+")

	new_file.write("Algorithm name: " + algorithm_name + "\n\n")
	new_file.write("Total Search Path: " + str(search_len) + "\n")
	new_file.write("Average Search Path: " + str(search_len/(20-no_solution_counter))+ "\n")
	new_file.write("Total Solution Path: " + str(solution_len) + "\n")
	new_file.write("Average Solution Path: " + str(solution_len/(20-no_solution_counter))+ "\n")
	new_file.write("Total 'No Solution': " + str(no_solution_counter)+ "\n")
	new_file.write("Average 'No Solution': " + str(no_solution_counter/20)+ "\n")
	new_file.write("Total cost: " + str(total_cost)+ "\n")
	new_file.write("Average cost: " + str(total_cost/(20-no_solution_counter))+ "\n")
	new_file.write("Total execution time: " + str(execution_time) + "\n")
	new_file.write("Average execution time: " + str(execution_time/(20-no_solution_counter))+ "\n")
	new_file.write("Total execution time (including 'No Solution'): " + str(execution_time + no_solution_counter*60) + "\n")
	new_file.write("Average execution time (including 'No Solution'): " + str((execution_time + no_solution_counter*60)/(20))+ "\n")
	new_file.write("***********************************************************************" + "\n")

# convert input string to a tuple
def parse_input(inputStr):
	inputStr = eval(inputStr.replace(';', ','))
	return inputStr

# converts tuple to a list, since tuples are immutable
def get_list(tup):
	return list(map(get_list, tup)) if isinstance(tup, (list, tuple)) else tup

if __name__ == '__main__':
	main()
	 
import copy
from node import Node

def main():
    # val = input("Enter your value: ")
    val = '((6; 1; 2); (7; 8; 3); (5; 4; 9))'
    input_list = parse_input(val)
    print(input_list)
    input_list = get_list(input_list)
    print(input_list)
    generateChildren(input_list)
    #------TEST CODE FOR THE SWAPING METHODS------
    # print(input_list)
    # swap_left(input_list,get_index(input_list, 6))
    # print(input_list)
    # swap_right(input_list,get_index(input_list, 6))
    # print(input_list)
    # swap_down(input_list,get_index(input_list, 6))
    # print(input_list)
    # swap_up(input_list,get_index(input_list, 6))
    # print(input_list)

    #--------TEST CODE FOR THE SWAP CHECKING--------
    # print(can_swap_left(get_index(input_list, 6),3))
    # print(can_swap_right(get_index(input_list, 6)))
    # print(can_swap_up(get_index(input_list, 6)))
    # print(can_swap_down(get_index(input_list, 6),3))

#convert input string to a tuple
def parse_input(inputStr):
    inputStr = eval(inputStr.replace(';',','))
    return inputStr
    
#converts tuple to a list, since tuples are immutable
def get_list(tup):
    return list(map(get_list, tup)) if isinstance(tup, (list, tuple)) else tup

#returns index of a number in a nested list as a list of size 2
def get_index(input_list, num):
    for sub_list in input_list:
        if num in sub_list:
            return (input_list.index(sub_list), sub_list.index(num))
    raise ValueError("'{num}' is not in list".format(num = num))


#-----------------------SWAPING METHODS-----------------------
def swap_left(input_list,current_index):
    list_copy = copy.deepcopy(input_list)
    num_temp = list_copy[current_index[0]][current_index[1]+1]
    list_copy[current_index[0]][current_index[1]+1] = list_copy[current_index[0]][current_index[1]]
    list_copy[current_index[0]][current_index[1]] = num_temp
    return list_copy

def swap_right(input_list,current_index):
    list_copy = copy.deepcopy(input_list)
    num_temp = list_copy[current_index[0]][current_index[1]-1]
    list_copy[current_index[0]][current_index[1]-1] = list_copy[current_index[0]][current_index[1]]
    list_copy[current_index[0]][current_index[1]] = num_temp
    return list_copy
    
def swap_up(input_list,current_index):
    list_copy = copy.deepcopy(input_list)
    num_temp = list_copy[current_index[0]-1][current_index[1]]
    list_copy[current_index[0]-1][current_index[1]] = list_copy[current_index[0]][current_index[1]]
    list_copy[current_index[0]][current_index[1]] = num_temp
    return list_copy

def swap_down(input_list,current_index):
    list_copy = copy.deepcopy(input_list)
    num_temp = list_copy[current_index[0]+1][current_index[1]]
    list_copy[current_index[0]+1][current_index[1]] = list_copy[current_index[0]][current_index[1]]
    list_copy[current_index[0]][current_index[1]] = num_temp
    return list_copy

#-------------SWAP CHECKING METHODS-------------
def can_swap_left(current_index,dimension):
    if(current_index[1] == dimension -1):
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

def can_swap_down(current_index,dimension):
    if(current_index[0] == dimension -1):
        return False
    else:
        return True

#Generate all 12 child nodes for given parent node    
def generateChildren(input_list):
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

    nodes = create_nodes(possible_moves, input_list)
    return nodes      

def create_nodes(states_list, parent_state):
    nodes = []
    for state in states_list:
        node = Node(state, parent_state)
        nodes.append(node)

    return nodes

if __name__ == '__main__':
    main()
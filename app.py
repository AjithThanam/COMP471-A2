
def main():
    list = generate_inputs()

    for input in list:
        print(str(input))
   

def generate_inputs():
    input_file = open("input_files/inputs.txt", "r")
    list_of_inputs = []

    for input in input_file:
        list_of_inputs.append(get_list(parse_input(input)))
    
    return list_of_inputs


# convert input string to a tuple
def parse_input(inputStr):
	inputStr = eval(inputStr.replace(';', ','))
	return inputStr

# converts tuple to a list, since tuples are immutable
def get_list(tup):
	return list(map(get_list, tup)) if isinstance(tup, (list, tuple)) else tup

if __name__ == '__main__':
    main()
     
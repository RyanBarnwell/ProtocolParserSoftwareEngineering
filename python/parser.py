from exceptions import IncompleteProtocolException
from exceptions import IndexOutOfBoundsException
from exceptions import InvalidCommandException
from exceptions import InvalidModeException
from exceptions import EmptyStackException
from exceptions import NonExistentStackException

import re # For regex matching

#indexOutOfBounds method
def indexOutOfBounds(input_array, index):
    if isinstance(index, int):
        if(index < 0 or index >= len(input_array)):
            raise IndexOutOfBoundsException()

def parse(input_values, parser_output):
    input_array = input_values.split()
    for x in range(len(input_array)):
        if input_array[x].isdigit():
            input_array[x] = int(input_array[x])
    index = 0
    stack_dict = {} # dictionary of stacks
    refMode = False
    logMode = False 
    logCounter = 0
    #incomplete protocol flag
    incompleteProt = 0

    if input_array[0] == 40:    # Turning on mode flags
        #check invalid mode
        if(not bool(re.match('^[LR]+$', input_array[1]))):
            raise InvalidModeException
        if 'R' in input_array[1]:
            refMode = True
        if 'L' in input_array[1]:
            logMode = True
        index = 2

    while index < len(input_array):
        if input_array[index] == 20: # Add function
            if refMode: # Reference mode functionality
                indexOutOfBounds(input_array, input_array[index+1])
                indexOutOfBounds(input_array, input_array[index+2])
                indexOutOfBounds(input_array, input_array[index+3])
                indexOutOfBounds(input_array, input_array[input_array[index+3]])
                paramVals = [input_array[input_array[index+1]], input_array[input_array[index+2]], 
                             input_array[input_array[index+3]]]
            else:
                indexOutOfBounds(input_array, input_array[index+3])
                paramVals = [input_array[index+1], input_array[index+2], input_array[index+3]]
            
            if logMode: # Log mode functionality
                logCounter += 1
                out = str(logCounter) + ": ADD " + str(input_array[index+1]) + " " + str(input_array[index+2]) + " " + str(input_array[index+3])
                parser_output.print(out)
            sum = 0

            if isinstance(paramVals[0], int):
                sum = paramVals[0]
            else:
                sum = stack_dict[paramVals[0]].pop()
            if isinstance(paramVals[1], int):
                sum += paramVals[1]
            else:
                sum += stack_dict[paramVals[1]].pop()
            input_array[paramVals[2]] = sum
            index += 4

        elif input_array[index] == 21: # Subtract function
            if refMode:
                indexOutOfBounds(input_array, input_array[index+1])
                indexOutOfBounds(input_array, input_array[index+2])
                indexOutOfBounds(input_array, input_array[index+3])
                indexOutOfBounds(input_array, input_array[input_array[index+3]])
                paramVals = [input_array[input_array[index+1]], input_array[input_array[index+2]], 
                             input_array[input_array[index+3]]]
            else:
                indexOutOfBounds(input_array, input_array[index+3])
                paramVals = [input_array[index+1], input_array[index+2], input_array[index+3]]
            
            if logMode: # Log mode functionality
                logCounter += 1
                out = str(logCounter) + ": SUB " + str(input_array[index+1]) + " " + str(input_array[index+2]) + " " + str(input_array[index+3])
                parser_output.print(out)

            diff = 0
            if isinstance(paramVals[0], int):
                diff = paramVals[0]
            else:
                diff = stack_dict[paramVals[0]].pop()
            if isinstance(paramVals[1], int):
                diff -= paramVals[1]
            else:
                diff -= stack_dict[paramVals[1]].pop()
            input_array[paramVals[2]] = diff            
            index += 4

        elif input_array[index] == 11: # Out function
            if refMode:
                indexOutOfBounds(input_array, input_array[index+1])
                indexOutOfBounds(input_array, input_array[input_array[index+1]])
                paramVal = input_array[input_array[index+1]]
            else:
                indexOutOfBounds(input_array, input_array[index+1])
                paramVal = input_array[index+1]
            out = ""
            if logMode: # Log mode functionality
                logCounter += 1
                out = str(logCounter) + ": OUT " + str(input_array[index+1])
                parser_output.print(out)
            out = ""
            if isinstance(paramVal, int):
                out = input_array[paramVal]
            else:
                for i in reversed(stack_dict[paramVal]):
                    out += (str(i) + " ")
                out = out[:-1] # delete trailing space at end
            parser_output.print(out)
            index += 2

        elif input_array[index] == 19: # End function
            if logMode: # Log mode functionality
                logCounter += 1
                out = str(logCounter) + ": END"
                parser_output.print(out)
            incompleteProt = 1
            break

        elif input_array[index] == 30: #push function
            #push a val to stack stored at index
            if refMode:
                indexOutOfBounds(input_array, input_array[index+2])
                paramVals = [input_array[input_array[index+1]], input_array[input_array[index+2]]]
            else:
                paramVals = [input_array[index+1], input_array[index+2]]
            if logMode: # Log mode functionality
                logCounter += 1
                out = str(logCounter) + ": PUSH " + str(input_array[index+1]) + " " + str(input_array[index+2])
                parser_output.print(out)
            if paramVals[0] in stack_dict:
                stack_dict[paramVals[0]].append(paramVals[1])
            else:
                stack_dict[paramVals[0]] = [paramVals[1]]
            index += 3

        elif input_array[index] == 31: #pop function
            #store popVal, then input in proper index
            if refMode:
                indexOutOfBounds(input_array, input_array[index+2])
                indexOutOfBounds(input_array, input_array[input_array[index+2]])
                paramVals = [input_array[input_array[index+1]], input_array[input_array[index+2]]]
            else:
                indexOutOfBounds(input_array, input_array[index+2])
                paramVals = [input_array[index+1], input_array[index+2]]
            if logMode: # Log mode functionality
                logCounter += 1
                out = str(logCounter) + ": POP " + str(input_array[index+1]) + " " + str(input_array[index+2])
                parser_output.print(out)
            if paramVals[0] not in stack_dict: # Checking if the stack exists
                raise NonExistentStackException()
            if len(stack_dict[paramVals[0]]) == 0: # Checking if stack is empty
                raise EmptyStackException()
            popVal = stack_dict[paramVals[0]].pop()
            input_array[paramVals[1]] = popVal
            index += 3

        elif input_array[index] == 32: #clear function
            #loop through stack to clear vals
            if refMode:
                indexOutOfBounds(input_array, input_array[index+1])
                paramVal = input_array[input_array[index+1]]
            else:
                paramVal = input_array[index+1]
            if logMode: # Log mode functionality
                logCounter += 1
                out = str(logCounter) + ": CLEAR " + str(input_array[index+1])
                parser_output.print(out)
            for x in range(len(stack_dict[paramVal])):
                stack_dict[paramVal].pop()
            index += 2

        elif input_array[index] == 33: # dump function
            if logMode: # Log mode functionality
                logCounter += 1
                out = str(logCounter) + ": DUMP"
                parser_output.print(out)

            for key in stack_dict.keys():
                output = key + ": "
                for i in reversed(stack_dict[key]):
                    output += (str(i) + " ")
                output = output[:-1]
                parser_output.print(output)
            index += 1
        else: # Any other value - now an Invalid command
            raise InvalidCommandException()
    if(incompleteProt == 0):
        raise IncompleteProtocolException()
    pass
# type: ignore


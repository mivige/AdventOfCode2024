def read_input_from_file(filename):
    corrupted_memory = ""
    
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace
            this = line.strip()
            
            # Append to complete string
            corrupted_memory += this
    
    return corrupted_memory

def validate_memory(corrupted_memory):
    statements_characters = ["d", "o", "n", "'", "t", "("]
    valid_characters = ["m", "u", "l", "(", ",", ")"]
    instruction = ""
    validated_memory = ""
    disabled = False

    for i in range(len(corrupted_memory)):
        c = corrupted_memory[i]

        # If the instructions are disabled ignore everything else until theres a 'do()'
        if disabled:
            if len(instruction) == 0:
                if c == "d":
                    instruction += c
            elif (instruction[-1] == "d" and c == "o") or (instruction[-1] == "o" and c == "("):
                instruction += c
            elif instruction[-1] == "(" and c == ")":
                instruction = ""
                disabled = False
            else: 
                instruction = ""

        # If the instructions are not disabled
        else:
            # First, check if the instruction could be a statement
            if c in statements_characters:
                if len(instruction) == 0:
                    if c == "d":
                        instruction += c
                        continue
                elif c == "(":
                    if instruction[-1] == "o" or instruction[-1] == "t":
                        instruction += c
                        continue
                elif instruction[-1] != statements_characters[statements_characters.index(c)-1]:
                    if instruction[-1] != "l":
                        instruction = ""
                else:
                    instruction += c
                    continue
                
            # If the character is not any of the valid ones
            if (c not in valid_characters) and (not c.isnumeric()):
                instruction = ""
            # If the character could be the ending of an instruction
            elif c == ")":
                if len(instruction) > 0:
                    if instruction[-1].isnumeric():
                        validated_memory += instruction + ")"
                    if instruction == "don't(":
                        disabled = True
                instruction = ""
            # If the character could be in the middle of two numbers
            elif c == ",":
                if len(instruction) > 0:
                    if instruction[-1].isnumeric():
                        instruction += ","
                else: 
                    instruction = ""
            else:
                # If the character could be in the start of an instruction
                if c in valid_characters[:4]:
                    if len(instruction) == 0:
                        if c == "m":
                            instruction += c
                    # If it's not in the correct position discard instruction
                    elif instruction[-1] != valid_characters[valid_characters.index(c)-1]:
                        instruction = ""
                    else:
                        instruction += c
                # If it's a number
                elif c.isnumeric():
                    if len(instruction) == 0:
                        pass
                    # Check that is in the correct position
                    elif (instruction[-1] != "(") and (instruction[-1] != ",") and (not (instruction[-1].isnumeric())):
                        instruction = ""
                    else: 
                        instruction += c
                else:
                    instruction += c

    return validated_memory

def analyze(instructions):
    result = 0

    # Divide the instructions into singular operations
    operations = instructions.replace("mul(", "").split(")")

    # Evaluate each operation
    for o in operations:
        # Get the datas of the operation
        datas = o.split(",")
        # Double check to be sure that the operation is valid
        if len(datas) == 2:
            # Add the multiplication to the result
            result += int(datas[0]) * int(datas[1])
    return result

if __name__ == "__main__":
    filename = 'day3/input.txt'
    corrupted_memory = read_input_from_file(filename)
    # print("Corrupted memory:", corrupted_memory)
    instructions = validate_memory(corrupted_memory)
    # print("Validated memory:", instructions)
    result = analyze(instructions)
    print("Result:", result)

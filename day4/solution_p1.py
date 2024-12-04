def read_input_from_file(filename):
    puzzle = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and create a list of each line
            this = list(line.strip())
            
            # Append to create a matrix
            puzzle.append(this)
    
    return puzzle

def check_horizontals(puzzle):
    return

def check_verticals(puzzle):
    return

def check_lr_diagonals(puzzle):
    return

def check_rl_diagonals(puzzle):
    return

def analyze(puzzle):
    result = 0

    # Check horizontal (including backwards)
    result += check_horizontals(puzzle)
    # Check vertical (including backwards)
    result += check_verticals(puzzle)
    # Check left to right diagonals (both top-down and bottom-up)
    result += check_lr_diagonals(puzzle)
    # Check right to left diagonals (both top-down and bottom-up)
    result += check_rl_diagonals(puzzle)

    return result

if __name__ == "__main__":
    filename = 'day4/input.txt'
    puzzle = read_input_from_file(filename)
    print("Puzzle input:", puzzle)
    result = analyze(puzzle)
    print("Result:", result)

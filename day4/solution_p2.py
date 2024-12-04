def read_input_from_file(filename):
    puzzle = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and create a list of each line
            this = list(line.strip())
            
            # Append to create a matrix
            puzzle.append(this)
    
    return puzzle

def check_xmas(puzzle, sequence):
    result = 0
    
    # For this case we can check starting from all the 'A' character assuming they are a center
    for i in range(1, len(puzzle) - 1):
        for j in range (1, len(puzzle[0]) - 1):
            # If this character is 'A'
            if puzzle[i][j] == sequence[1]:
                # Create and evaluate the left-to-right diagonal
                lr = []
                lr.append(puzzle[i][j])
                lr.append(puzzle[i - 1][j - 1])
                lr.append(puzzle[i + 1][j + 1])
                if sorted(lr) == sorted(sequence):
                    # Create and evaluate the right-to-left diagonal
                    rl = []
                    rl.append(puzzle[i][j])
                    rl.append(puzzle[i - 1][j + 1])
                    rl.append(puzzle[i + 1][j - 1])
                    if sorted(rl) == sorted(sequence):
                        # If it was a center increment the result
                        result += 1
    return result

def analyze(puzzle):
    result = 0
    # Removed 'X' from the complete sequence
    sequence = ['M', 'A', 'S']

    # Check diagonals
    result = check_xmas(puzzle, sequence)

    return result

if __name__ == "__main__":
    filename = 'day4/input.txt'
    puzzle = read_input_from_file(filename)
    # print("Puzzle input:", puzzle)
    result = analyze(puzzle)
    print("Result:", result)

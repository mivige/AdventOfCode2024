def read_input_from_file(filename):
    puzzle = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and create a list of each line
            this = list(line.strip())
            
            # Append to create a matrix
            puzzle.append(this)
    
    return puzzle

def check_horizontals(puzzle, sequence):
    partial = 0

    # For horizontal checks we can evaluate each line separately
    for l in puzzle:
        # Check forward
        current_sequence = 0
        for i in range (len(l)):
            # If the next needed character is found implement the current sequence
            if l[i] == sequence[current_sequence]:
                current_sequence += 1
            else:
                # Check for the case if the character is the first of the sequence, otherwise you could miss some cases (e.g. 'XXMAS')
                if l[i] == sequence[0]:
                    current_sequence = 1
                else:
                    current_sequence = 0
            # If the current sequence is completed implement the partial count
            if current_sequence == 4:
                partial += 1
                # Reset to 0 to start a new sequence, we don't need special checks since we're checking separately forward and backwards, so the end of a sequence can't be the start of a new one ('S' != 'X')
                current_sequence = 0
        
        # Check backwards
        current_sequence = 0
        for i in range (1, len(l)+1):
            if l[-i] == sequence[current_sequence]:
                current_sequence += 1
            else:
                if l[-i] == sequence[0]:
                    current_sequence = 1
                else:
                    current_sequence = 0
            if current_sequence == 4:
                partial += 1
                current_sequence = 0

    return partial

def check_verticals(puzzle, sequence):
    partial = 0

    for i in range (len(puzzle)):
        # Check forward
        current_sequence = 0
        for j in range (len(puzzle[0])):
            # If the next needed character is found implement the current sequence
            if puzzle[j][i] == sequence[current_sequence]:
                current_sequence += 1
            else:
                # Check for the case if the character is the first of the sequence, otherwise you could miss some cases (e.g. 'XXMAS')
                if puzzle[j][i] == sequence[0]:
                    current_sequence = 1
                else:
                    current_sequence = 0
            # If the current sequence is completed implement the partial count
            if current_sequence == 4:
                partial += 1
                # Reset to 0 to start a new sequence, we don't need special checks since we're checking separately forward and backwards, so the end of a sequence can't be the start of a new one ('S' != 'X')
                current_sequence = 0
        
        # Check backwards
        current_sequence = 0
        for j in range (1, len(puzzle[0])+1):
            # If the next needed character is found implement the current sequence
            if puzzle[-j][i] == sequence[current_sequence]:
                current_sequence += 1
            else:
                # Check for the case if the character is the first of the sequence, otherwise you could miss some cases (e.g. 'XXMAS')
                if puzzle[-j][i] == sequence[0]:
                    current_sequence = 1
                else:
                    current_sequence = 0
            # If the current sequence is completed implement the partial count
            if current_sequence == 4:
                partial += 1
                # Reset to 0 to start a new sequence, we don't need special checks since we're checking separately forward and backwards, so the end of a sequence can't be the start of a new one ('S' != 'X')
                current_sequence = 0

    return partial

def check_lr_diagonals(puzzle, sequence):
    partial = 0

    return partial

def check_rl_diagonals(puzzle, sequence):
    partial = 0

    return partial

def analyze(puzzle):
    result = 0
    sequence = ['X', 'M', 'A', 'S']

    # Check horizontal (including backwards)
    result += check_horizontals(puzzle, sequence)
    # Check vertical (including backwards)
    result += check_verticals(puzzle, sequence)
    # Check left to right diagonals (both top-down and bottom-up)
    result += check_lr_diagonals(puzzle, sequence)
    # Check right to left diagonals (both top-down and bottom-up)
    result += check_rl_diagonals(puzzle, sequence)

    return result

if __name__ == "__main__":
    filename = 'day4/input.txt'
    puzzle = read_input_from_file(filename)
    # print("Puzzle input:", puzzle)
    result = analyze(puzzle)
    print("Result:", result)

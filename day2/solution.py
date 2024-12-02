def read_numbers_from_file(filename):
    lines = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and split the line
            this = line.strip().split()
            
            # Convert to integers and append to respective lists
            lines.append(this)
    
    return lines

def convert_to_int(lines):
    for x in lines:
        l = len(x)

        for i in range(l):
            # Converts each element to an integer
            x[i] = int(x[i])

    return lines

    
def analyze(lines):
    safes = 0

    for x in lines:
        # Check if all levels are increasing or decreasing
        is_increasing = all(x[i] <= x[i + 1] for i in range(len(x) - 1))
        is_decreasing = all(x[i] >= x[i + 1] for i in range(len(x) - 1))
        
        # Check if differences between adjacent levels are between 1 and 3
        valid_differences = all(1 <= abs(x[i] - x[i + 1]) <= 3 for i in range(len(x) - 1))
        
        # A report is safe if it's either increasing or decreasing AND has valid differences
        if (is_increasing or is_decreasing) and valid_differences:
            safes += 1

    return safes

if __name__ == "__main__":
    filename = 'day2/input.txt'
    lines = read_numbers_from_file(filename)
    # print("Lines:", lines)
    lines = convert_to_int(lines)
    # print("Lines:", lines)
    safes = analyze(lines)
    print(safes)

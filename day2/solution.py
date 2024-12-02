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

def is_safe_report(report):
    # Check if the report is safe without removing any levels
    is_increasing = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] >= report[i + 1] for i in range(len(report) - 1))
    valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    return (is_increasing or is_decreasing) and valid_differences

def check_with_problem_dampener(report):
    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        # Create a new report with the i-th level removed
        modified_report = report[:i] + report[i+1:]
        
        # Check if the modified report is safe
        if is_safe_report(modified_report):
            return True
    
    return False

def analyze(lines):
    safes = 0

    for x in lines:
         # First, check if the report is safe without removing any levels
        if is_safe_report(x):
            safes += 1
        # If not, check if removing a single level makes it safe
        elif check_with_problem_dampener(x):
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

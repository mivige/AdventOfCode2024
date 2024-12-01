def read_numbers_from_file(filename):
    left_numbers = []
    right_numbers = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and split the line
            left, right = line.strip().split()
            
            # Convert to integers and append to respective lists
            left_numbers.append(int(left))
            right_numbers.append(int(right))
    
    return left_numbers, right_numbers

def analyze(left, right):
    l = len(left)
    total = 0
    similarity = 0
    
    # Sort both lists to ensure correct pairing
    sorted_left = sorted(left)
    sorted_right = sorted(right)

    for i in range(l):
        total += abs(sorted_left[i] - sorted_right[i])
        similarity += sorted_left[i] * sorted_right.count(sorted_left[i])
    
    return total, similarity

if __name__ == "__main__":
    filename = 'day1/input.txt'
    left, right = read_numbers_from_file(filename)
    # print("Left numbers:", left)
    # print("Right numbers:", right)
    total, similarity = analyze(left, right)
    print(total)
    print(similarity)

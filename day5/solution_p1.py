def read_input_from_file(filename):
    rules = []
    updates = []
    reading_rules = True
    
    with open(filename, 'r') as file:
        for line in file:
            # When we find the empty line the rules are finished
            if line == '\n':
                reading_rules = False
            elif reading_rules:
                # Strip whitespace and create a list of each rule
                this = list(map(int, line.strip().split('|')))
                
                rules.append(this)
            else:
                # Strip whitespace and create a list of each update
                this = list(map(int, line.strip().split(',')))
                
                updates.append(this)
        
    return rules, updates

def find_corrects(updates, rules):
    correct_updates = []

    # Check all updates
    for l in updates:
        correct = True

        # Assuming that the uppdate is correct check from the second one if a rule has been broken before
        for i in range(1, len(l)):
            if not correct:
                break;
            
            # Check find rules about the current page being before another one
            for r in rules:
                if not correct:
                    break;
                elif r[0] == l[i]:

                    # If such rule is found check all characters before the current to see if they break such rule
                    for j in range(i):
                        if r[1] == l[j]:
                            correct = False
                            break;
        if correct:
            correct_updates.append(l)
                
    return correct_updates

def analyze(updates, rules):
    result = 0
    
    correct_updates = find_corrects(updates, rules)

    # Sum the values of the centers of the correct updates
    for l in correct_updates:
        result += l[len(l) // 2]

    return result

if __name__ == "__main__":
    filename = 'day5/input.txt'
    rules, updates = read_input_from_file(filename)
    # print("Rules:", rules)
    # print("Updates:", updates)
    result = analyze(updates, rules)
    print("Result:", result)

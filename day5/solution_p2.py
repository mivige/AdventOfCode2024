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

def correct_update(update, rules):
    correct = True

    # Assuming that the uppdate is correct check from the second page if a rule has been broken before
    for i in range(1, len(update)):

        # Stop after one movement
        if not correct:
            break;
        
        # Check to find rules about the current page being before another one
        for r in rules:
            if not correct:
                break;
            elif r[0] == update[i]:

                # If such rule is found check all characters before the current to see if they break such rule
                for j in range(i):

                    # If a page break such rule invert them
                    if r[1] == update[j]:
                        correct = False
                        move = update[i]
                        update[i] = update[j]
                        update[j] = move
                        break;
    
    # If the update had a movement reiterate on it (maybe new rules still need to be checked)
    if not correct:
        return correct_update(update, rules)

    # If it was correct from the start return it
    return update

def make_corrects(updates, rules):
    to_be_corrected_updates = []

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
        
        # If is not correct add it to the list
        if not correct:
            to_be_corrected_updates.append(l)
                
    corrected_updates = []
    
    # Correct all uncorrect updates
    for u in to_be_corrected_updates:
        corrected_updates.append(correct_update(u, rules))

    return corrected_updates

def analyze(updates, rules):
    result = 0
    
    corrected_updates = make_corrects(updates, rules)

    # Sum the values of the centers of the corrected updates
    for l in corrected_updates:
        result += l[len(l) // 2]

    return result

if __name__ == "__main__":
    filename = 'day5/input.txt'
    rules, updates = read_input_from_file(filename)
    # print("Rules:", rules)
    # print("Updates:", updates)
    result = analyze(updates, rules)
    print("Result:", result)

import csv

def run_intcode(data):
    position = 0
    while position < len(data) and data[position] != 99:        
        if data[position] == 1:
            data[data[position + 3]] = data[data[position + 1]] + data[data[position + 2]]
        elif data[position] == 2:
            data[data[position + 3]] = data[data[position + 1]] * data[data[position + 2]]
        position += 4
    return data[0]

def noun_verb_combo(data):
    for noun in range(0, 100):
        for verb in range (0, 100): 
            copy = data.copy()
            copy[1] = noun
            copy[2] = verb
            output = run_intcode(copy)
            if output == 19690720:
                return noun * 100 + verb

if __name__ == "__main__":
    with open('day-2-input.csv', newline='') as csvfile:
        data = [list(map(int,rec)) for rec in csv.reader(csvfile, delimiter=',')][0]
        print(noun_verb_combo(data))
        
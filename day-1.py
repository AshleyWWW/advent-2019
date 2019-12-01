def amt_fuel(mass):
    if mass <= 0:
        return 0
    fuel = max((mass // 3) - 2, 0)
    return fuel + amt_fuel(fuel)

def total_fuel():
    total = 0
    input_file = open("day-1-input.txt", "r")
    lines = input_file.readlines()
    
    for line in lines: 
        total += amt_fuel(int(line))
    
    print(total)

if __name__ == "__main__":
    total_fuel()
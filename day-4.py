def meets_criteria(n):
    exp = 5
    digit = n // 10**exp
    n = n % 10**exp
    # has_double = False
    has_double = [0] * 10
    while exp > 0:
        exp -= 1
        next_dig = n // 10**exp
        n = n % 10**exp
        if next_dig < digit:
            return False
        if next_dig == digit: 
            has_double[next_dig] += 1
        #     has_double = True
        digit = next_dig
    return 1 in has_double
    # return has_double

def passwords(lower, upper):
    pws = 0
    for i in range(lower, upper):
        if (meets_criteria(i)):
            pws += 1
    return pws

if __name__ == "__main__":
    print(passwords(248345, 746315))
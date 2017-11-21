def permutations(string):
    #your code here
    if len(string) == 1: return [string]
    if len(set(string)) == 1: return [string]
    for i in range(len(string)):
        return [string[i] + e for i in range(len(string)) for e in permutations(string[:i]+string[i+1:])]

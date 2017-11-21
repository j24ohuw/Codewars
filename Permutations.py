def permutations(string):
    return [string] if len(set(string)) == 1 \
                    else set([string[i] + e for i in range(len(string)) for e in permutations(string[:i] + string[i+1:])])

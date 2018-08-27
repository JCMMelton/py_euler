from string import ascii_uppercase

def make_letter_scores():
    letter_scores = {}
    for i in range(0, 26):
        letter_scores[ascii_uppercase[i]] = i+1
    return letter_scores

def alph_score(name, letter_scores):
    score = 0
    for c in name:
        score += letter_scores.get(c)
    return score

with open('p022_names.txt') as names_file:
    letter_scores = make_letter_scores()
    names_raw = [n for n in names_file]
    names = [name[1:-1] for name in names_raw[0].split(',')]
    names.sort()
    total_score = 0
    for n in range(1, len(names)+1):
        total_score += alph_score(names[n-1], letter_scores) * n
    print(total_score)

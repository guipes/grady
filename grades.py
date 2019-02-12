# read in grades.txt
# print out a list of students
# and their avg grade for class
# and rank them in order
# from high to low
# i.e., bob 98, sue 97, sara 76


from collections import defaultdict


def group(dct, a, b):
    dct[a].append(b)
    return dct


def dct_keys(dictionary, ky):
    if dictionary.get(ky) is None:
        dictionary.setdefault(ky, [])
    return dictionary


def mean(nums):
    return sum(nums) / len(nums)


def sort(lst):
    L = list(lst.items())
    return sorted(L, key=lambda t: t[1])[::-1]


with open('grades.txt') as f:
    dct = dict()
    avg_dct = dict()
    for line in f:
        entry = line.strip().split(' ')
        name = entry[0]
        grade = float(entry[1])
        dct = dct_keys(dct, name)
        dct2 = group(dct, name, grade)
    for person in dct2:
        avg = mean(dct2[person])
        avg_dct[person] = avg
    L = sort(avg_dct)
    print(L)

# --------------- CHYLD'S CODE ----------------


# def get_grades(fn):
#     grades = defaultdict(list)
#     with open(fn) as f:
#         for line in f:
#             name, grade = line.strip().split(' ')
#             grade = float(grade)
#             grades[name].append(grade)
#     return grades


# def get_averages(grades):
#     avgs = []
#     for name, scores in grades.items():
#         avg = sum(scores) / len(scores)
#         avgs.append((name, avg))
#     return avgs


# def rank_scores(avgs):
#     return sorted(avgs, key=lambda t: t[1])[::-1]

from grades import group, dct_keys, mean, sort


def test_mean():
    m = mean([1, 2, 3, 4, 5])
    assert m == 3


def test_dct_keys():
    d = {'sally': []}
    key1 = 'sam'
    key2 = 'sally'
    key3 = 'sam'
    key4 = 'bob'
    dct_keys(d, key1)
    dct_keys(d, key2)
    dct_keys(d, key3)
    dct_keys(d, key4)
    assert d == {'sally': [], 'sam': [], 'bob': []}


def test_group():
    a = 'bob'
    b = 78
    d = {'sally': [], 'sam': [], 'bob': []}
    new_dct = group(d, a, b)
    assert new_dct == {'sally': [], 'sam': [], 'bob': [78]}


def test_sort():
    us = {'sally': 27, 'sam': 98, 'bob': 78}
    s = sort(us)
    assert s == [('sam', 98), ('bob', 78), ('sally', 27)]
# --------------- CHYLD'S CODE ----------------
# from grades import get_grades, get_averages, rank_scores


# def test_get_grades():
#     grades = get_grades('grades.txt')
#     print(grades)
#     d = {'bob': [78.0, 88.0, 90.0], 'sara': [98.0], 'sue': [72.0, 95.0]}
#     assert grades == d


# def test_get_averages():
#     grades = get_grades('grades.txt')
#     avgs = get_averages(grades)
#     assert avgs == [('bob', 85.33333333333333), ('sara', 98.0), ('sue', 83.5)]


# def test_rank_scores():
#     grades = get_grades('grades.txt')
#     avgs = get_averages(grades)
#     rank = rank_scores(avgs)
#     assert rank == [('sara', 98.0), ('bob', 85.33333333333333), ('sue', 83.5)]

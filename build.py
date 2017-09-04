import operator


def solution_asc(dic):
        l=[]
        pair =()
        for key in sorted(dic.keys()):
            pair = (key,dic[key])
            l.append(pair)
        return l
print solution_asc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})

def solution_desc(dic):
    l=[]
    pair =()
    for key in sorted(dic.keys()):
        pair = (key,dic[key])
        l.append(pair)
        l1 = l[::-1]
    return l1
print solution_desc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})

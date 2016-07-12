# level 2.1
# tldr:
# sort input array of strings such that sum of all scores of all letters
# is prioritized (A = 1, B = 2, ... Z = 26), and after sorting by that you
# should sort by regular alphabetical order

def compare(item1, item2): # custom comparator
    value1 = 0; value2 = 0;
    for c in item1:
        value1 += ord(c) - ord('a') + 1;
    for c in item2:
        value2 += ord(c) - ord('a') + 1;
    #print(item1 + ", " + value1);
    #print(item2 + ", " + value2);
    if value1 < value2: # compare values
        return -1;
    elif value1 == value2: # if equal, alphabetical
        if item1 < item2:
            return -1;
        elif item1 == item2:
            return 0;
        else:
            return 1;
    else:
        return 1;

def answer(names):
    return sorted(names, cmp=compare, reverse=True);
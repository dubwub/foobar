# we represent in base 3 from left to right
# so 16 becomes: 1 2 1
# in ternary 10 - 1 = 2, so we replace all 2s with a 1 in the
# next highest bit and -1 in the current bit. this works because
# L (side with the weight) represents -1, 0 is not use, and 1 is R

def baseTenToTernary(x):
    array = []; # it is left to right, so [2, 1, 1] is 2*1 + 3 + 9
    power = 1;
    tmp = x;
    while tmp > 0:
        array.append(tmp%3);
        tmp -= tmp%3;
        tmp /= 3;
        power *= 3;
    #print array;
    return array;
    
def propagateRight(array):
    for i in range(0,len(array)):
        if array[i] >= 2:
            array[i] -= 3;
            if i == len(array)-1: 
                # check for out of bounds
                    array.append(1); # i think python is broken this indent was the only way this would compile
                else: # ????????????????????
                    array[i+1]+=1; # ??????????????????????????
    return array

def convertToSolution(array):
    solution = [];
    for i in array:
        if i == -1:
            solution.append("L");
        elif i == 0:
            solution.append("-");
        else: # should only be 1 left
            solution.append("R");
    return solution;

def answer(x):
    return convertToSolution(propagateRight(baseTenToTernary(x)));
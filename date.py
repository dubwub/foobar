#level 1
#tldr:
#given 3 numbers, figure out if exactly one date can be made from them
#and return ambiguous if more than one can be made.

def formatNumber(x):
    if x >= 10:
        return str(x);
    else:
        return "0" + str(x);

def answer(x, y, z):
    input = [x,y,z];
    numberOfDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    answer = "";
    for it in range(0,3):
        # assume numbers[it] is month
        if input[it] <= 12:
            day = 0; year = 0;
            if input[(it + 1)%3] <= numberOfDays[input[it]-1]: # check all permutations, boilerplate code unfortunately
                day = input[(it + 1)%3];
                year = input[(it + 2)%3];
                new_answer = "" + formatNumber(input[it]) + "/" + formatNumber(day) + "/" + formatNumber(year);
                if answer != "" and answer != new_answer:
                    return "Ambiguous";
                else:
                    answer = new_answer;
            if input[(it + 2)%3] <= numberOfDays[input[it]-1]:
                day = input[(it + 2)%3];
                year = input[(it + 1)%3];
                new_answer = "" + formatNumber(input[it]) + "/" + formatNumber(day) + "/" + formatNumber(year);
                if answer != "" and answer != new_answer:
                    return "Ambiguous";
                else:
                    answer = new_answer;
    return answer;
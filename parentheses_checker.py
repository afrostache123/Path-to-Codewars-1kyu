#https://www.codewars.com/kata/all-balanced-parentheses

def group_check(xs):
    index = 0
    p_dict = {
        '(' : ')',
        '[':']',
        '{':'}'
    }
    xs = list(xs)
    while True:
        print(index)
        print(xs)
        current_left = xs[index]
        try:
            current_right = xs[index + 1]
        except IndexError:
            return False
        if p_dict[current_left] == current_right:
            del xs[index]
            del xs[index]
            if index == 0:
                return True
            index -= 1

        elif p_dict[xs[index]] not in p_dict:
            return False

        else:
            index += 1

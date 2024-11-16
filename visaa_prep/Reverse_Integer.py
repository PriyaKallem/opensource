def reverse_integer(n):
    INT_MIN, INT_MAX=-2**31,2**31-1
    is_negative=n<0
    reversed_num=int(str(abs(n))[::-1])
    if is_negative:
        reversed_num=-reversed_num
    if reversed_num<INT_MIN or reversed_num> INT_MAX:
        return 0
    else:
        return reversed_num
print(reverse_integer(int(input())))

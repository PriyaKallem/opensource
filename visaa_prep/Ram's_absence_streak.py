def max_consecutive_absent_days(attendance_rcd):
    max_absent_days=0
    current_absent_days=0
    for day in attendance_rcd:
        if day == 0:
            current_absent_days += 1
            max_absent_days=max(max_absent_days, current_absent_days)
        else:
            current_absent_days=0
    return max_absent_days
N=int(input())
attendance_rcrd=list(map(int,input().split()))
result=max_consecutive_absent_days(attendance_rcrd)
print(result)

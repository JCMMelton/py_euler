start_year = 1900
day_of_week = 366
total = 0

for y in range(1, 101):
    #         Ja Fe Ma Ap My Jn Jl Au Se Oc No De
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if y % 4 == 0:
        months[1]+=1

    for m in range(0, len(months)):
        day_of_week += months[m]
        if day_of_week % 7 == 0:
            total +=1

print(total)

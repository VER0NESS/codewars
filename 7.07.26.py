def whatday(num):
    days = ["token","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    try:
        if num > 0 and num <= 7:
            print(days[num])
            return days[num]
        else:
            print('error')
    except Exception:
        print('error')

for i in range(0,10):
    print(i)
    whatday(i)

    num = int(input())
    reverse = 0
    while(num > 0):
        reminder = num %10
        reverse = (reverse *10) + reminder
        num = num //10
    print("reverse of entered number is = %d" %reverse)

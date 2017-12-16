n = int(input())
if (( n%400 == 0)or (( n%4 == 0 ) and ( n%100 != 0))):
    print("given year is leap")
else:
    print("given year is not leap")

'''
chocolate rapper
'''
total=0
amount=15
price=3
exc=2
chocalate=amount/price
rem_warapper=chocalate
total+=chocalate
chocalate=0
while rem_warapper>=2 or (rem_warapper+(chocalate//exc))>=2 or (rem_warapper+chocalate)/exc==1:
    print("total_chocolte",total)
    rem_warapper=chocalate+rem_warapper
    print("rem_wrapper=", rem_warapper)
    chocalate=rem_warapper//exc   #5//2=2
    print("chocolate+", chocalate)
    rem_warapper = rem_warapper%exc#5%2=1
    total+=chocalate


print("total_chocolate=",total)
print("remaining warapper=",rem_warapper)



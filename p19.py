import calendar
ans=0
for year in range(1901,2001):
    for month in range(1,13):
        if calendar.monthrange(year,month)[0]==6: ans+=1
print ans

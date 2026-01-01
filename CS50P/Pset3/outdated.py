y={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
while True:
     try:
        data=input("Date:").strip()
        if data[0].isdigit():
            data=data.replace("/"," ")
            month,day,year=data.split(" ")
            month=int(month)
            day=int(day)
            year=int(year)
            if 1<=int(day) and int(day)<=31 and 1<=int(month) and int(month)<=12:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
        if not data[0].isdigit():
            if (",") not in data:
                continue
            else:
                month,day,year=data.split(" ")
                day=day.replace(","," ")
                month=month.capitalize()
                month=y[month]
                day=int(day)
                year=int(year)
                if 1<=int(day) and int(day)<=31 and 1<=int(month) and int(month)<=12:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    continue
     except ValueError:
         continue


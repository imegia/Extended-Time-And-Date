from time import localtime

def twelve_hour():
  now = localtime()
  hour = now.tm_hour
  minute = now.tm_min
  if hour > 12:
    hour = hour - 12
    ampm = "PM"
  else:
    ampm = "AM"
  if hour < 10:
    hour = "0" + str(hour)
  if minute < 10:
    minute = "0" + str(minute)
  return str(hour) + ":" + str(minute) + " " + ampm

def long_date():
  now = localtime()
  dayofmonth = now.tm_mday
  typeofday = now.tm_wday
  month = now.tm_mon
  year = now.tm_year
  typeofday_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  typeofday = typeofday_list[typeofday]
  month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
  month = month_list[month]
  if dayofmonth == 1 or dayofmonth == 21 or dayofmonth == 31:
    dayofmonth = str(dayofmonth) + "st"
  elif dayofmonth == 2 or dayofmonth == 22:
    dayofmonth = str(dayofmonth) + "nd"
  elif dayofmonth == 3 or dayofmonth == 23:
    dayofmonth = str(dayofmonth) + "rd"
  else:
    dayofmonth = str(dayofmonth) + "th"
  return typeofday + " " + dayofmonth + " " + month + " " + str(year)

print("12 Hour -", twelve_hour())
print("Long Date -", long_date())

def timeConversion(s):

    h = s[-2:]
    if h == 'PM' and s[:2] != '12':
        s = str(12 + int(s[:2])) + s[2:]
    if h == 'AM' and s[:2] == '12':
        s = '00' + s[2:]
    return s[:-2]


hora = '07:05:45PM'
res = timeConversion(hora)
print(res)

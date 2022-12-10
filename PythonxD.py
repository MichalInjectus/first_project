import os
import time

#os.system('cmd /c "cd C:\\Users\\vdi-student\\Desktop && dir /s new.txt >> result.txt"')
#my_string1 ='my mom'
#my_string2 = 'my dad'
#sum1 = my_string1 + my_string2
#print(sum1)
#sum2 = 'my ' + my_string1 + ' and my ' + my_string2
#print(sum2)
#print(sum2[3:6])
#print(sum2[-4:-1])

import datetime
today = datetime.date.today()
print(type(today))
print(today)

data1 = today.strftime('Dzisiaj jest %d . dzień  %m . miesiąca')
data2 = today.strftime('%d--%m--%y')
print(data1)
print(data2)
import easygui as gui
#Attention!It's only applicaple after Oct. 4th,1582
gui.msgbox('this is a date-calculator')
gui.msgbox('it can calculate the week of the day')
gui.msgbox("let's try")
year=gui.enterbox('the year:')#the year of the date
assert year!=''
m=gui.enterbox('the month:')#the month of the date
assert m!=''
d=gui.enterbox('the day:')#the exact day of the date
assert d!=''
c=int(year[:2])
y=int(year[2:4])
m=int(m)
d=int(d)
week=(c//4-2*c+y+y//4+13*(m+1)//5+d-1)%7#the zeller formula
if week==0: 
    gui.msgbox('the week is:7')
else:
    gui.msgbox('the week is:'+str(week))
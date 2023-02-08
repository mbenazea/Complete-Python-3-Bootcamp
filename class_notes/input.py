#list = ['red', 'Green', 'white', 'Black']
#print(list[0], list[-1])

#exams_st_date = (11,12,2022)
#print( "The examination will start from: %i / %i / %i" %exams_st_date)

#program to print the calendar of a given month and year.
import calendar

y = int (input("Input the year : "))
m = int (input("Input the month : "))

print(calendar.month(y,m))
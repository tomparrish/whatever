#Calculates Easter on the Gregorian Calendar
#I'd like to grab several calculation to play with.
#I suppose the next one is Julian

#The current year
y = 2024

#The J.M. Oudin calculation
#Calculate the current century.
#You're calculating something in the Gregorian calendar and there are century specific rules
c = y//100
#Determine the position of the year to the 19-year Metonic cycle which links lunar phases to dates
n = y-19*(y//19)
#Corrects for the century specific difference in the Gregorian calendar
#k will adjust by a day if necessary in a later calculation
k = (c-17)//25
#determines how far off the lunar year is from the solar year
i = c-c//4-(c-k)//3+19*n+15
#we need this to fit within a month
i = i-30*(i//30)
#another change to make sure i doesn't exceed the 28 day lunar cycle in certain circumstance
i = i-(i//28)*(1-(i//28)*(29//(i+1))*((21-n)//11))
#A preliminary guess for Easter's date
j = y+y//4+i+2-c+c//4
#Easter has to fall on a Sunday
j = j-7*(j//7)
#difference between full moon and Sunday above
l = i-j
#This just converts it into the month
m = 3+(l+40)//44
#This just converts it into the day
d = l+28-31*(m//4)

print("Western Easter (Gregorian)")
print("  J.M. Oudin Calculation (1940)")
print("    "+str(m)+'/'+str(d)+'/'+str(y))

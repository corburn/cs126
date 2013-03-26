# A new Date object is sent an arbitrary month, day, and year to store. You should
# be able to advance the date by 1 day while observing the rules of the standard
# year. For example, the next day after "2-28-2010" would be "3-1-2010". You do
# not have to worry about leap years unless you're doing the extra credit. You
# should also be able to advance the date by an arbitrary number of days ("x" days).
# You should also be able to advance the date by an arbitrary number of weeks
# ("x" weeks) where each week advances the date by 7 days.
# The Date should have a __str__() method defined that returns an appropriate text string.
class Date:
	def __init__(self, month, day, year):
		self.year = year
		self.month = month
		self.day = day
	
	def __str__(self):
		return str(self.year) + "/" + str(self.month) + "/" + str(self.day)

	def addDay(self, days):
		if(days > 1):
			self.addDay(days - 1)
		if(self.month == 2):
			if self.year % 400 == 0:
				leapYear = True
			elif self.year % 100 == 0:
				leapYear = False
			elif self.year % 4 == 0:
				leapYear = True
			else:
				leapYear = False
			if not leapYear and self.day == 28 or leapYear and self.day == 29:
				self.day = 0
				self.month = 3
		elif self.day == 30 and self.month in [2,4,6,9,11] or self.day == 31:
			self.day = 0
			self.month = (self.month % 12) + 1
			if self.month == 1:
				self.year += 1
		self.day += 1

	def addWeek(self, weeks):
		self.addDay(weeks*7)

date = Date(1,1,2010)
print date
date.addDay(1)
print date
date.addDay(29)
print date
date.addWeek(4)
print date
for i in range(365):
	date.addDay(1)
	print date
print "\nExtra Credit: Jumping ahead to the next leap year..."
date.addDay(365)
print date
date.addDay(1)
print date
date.addDay(1)
print date

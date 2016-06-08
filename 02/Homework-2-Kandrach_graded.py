# Grade: 3.5 / 16
# TA-COMMENT: Don't worry too about the numerical grade here! How are you feeling about some of the syntax HW2 covered? I know you've had some time to practice since you completed this assignment, but let me know if you want to sit down and go over anything -- I'd be more than happy to do that!

#Sasha Kandrach
#05/25/16
#Homework 2
numbers = [22, 90, 0, -10, 3, 22, 48]
print(numbers)
print((numbers)[4]) # TA-COMMENT: (-1) This is an off-by-1 error! Remember that in python, we start counting with 0. So our 4th element is actually numbers[3]
print("element four is": numbers[4]) # TA-COMMENT: (-0.5) The syntax here actually is preventing the scripting from running. Always do a test run before submitting your homework! The current syntax is:

# print("element four is:", numbers[4])
# TA-COMMENT: The : should have been within the quotation marks and there should have been a comma between your string and numbers[4].

add(0+3)

# TA-COMMENT: (-1) remember how we access things out of a list. We can say, list_name[0] or list_name[1], and so forth.
print("The sum of the second and fourth element is:".format(number[2])")

print(numbers[6])

# TA-COMMENT: (-1) This isn't quite how we should structure if-statements! I see that you've started on breaking down the logic of what the question wants, but then you have to "convert" that logic into python syntax.

x=6
    if x<10
    x*30
    if x == even number
    x+6
    if x == not -10
    x-1
    else
print("Try again with a different number that is less than 10")

# TA-COMMENT: The if-statement structure for question 6 should look something like this:

for number in numbers:
	original = number

	if original < 10:
		number = number * 30

		if (original%2) == 0:
			number = number + 6

	elif original > 50:
		number = number - 10

	if original != -10:
		number = number - 1

	print(number)

# TA-COMMENT: Let me know if the above structure makes sense, because it's trying to do some tricky things!

# TA-COMMENT: For the problem below, we have to make dictionary data structure before we beginning access its contents as you do below.
"My favorite movie is", movie['Spotlight'], "which was released in", movie['2016'], "and was directed by", movie['Tom McCarthy']
movie['budget']= 20,000,000 # TA-COMMENT: Don't forget, we can't use commas in this way when we're coding.
movie['revenue']= 45,055,776
#http://www.boxofficemojo.com/movies/?id=spotlight.htm
print("This was a flop") # TA-COMMENT: This should be part of a if-else statement.
#While it didn't generate five times the amount it cost to make it, it still one an Oscar which isn't too shabby

parts_of_NYC = {
'Brooklyn' = 2,600,000
'Bronx' = 1,400,000
'Manhattan'= 1,600,000
'Staten Island' = 470,000
= # TA-COMMENT: we don't use '=' to associate keys with values in a dictionary; we use ':'. so what's inside your { } should look something like this:

# 'Brooklyn': 2600000
}
print(Brooklyn)
sum(parts_of_NYC.values) # TA-COMMENT: Good instinct; values actually has to look like values()
# Corrected code: print(sum(parts_of_NYC.values()))
print(sum(parts_of_NYC))
6,070,000*1,600,000

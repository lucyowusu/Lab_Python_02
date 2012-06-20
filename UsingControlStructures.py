print 'Lab 02'
print 'Written Exercises, Number 5      '



print ''
print ''

theInput= raw_input("Enter an integer: ")

if  int(theInput)%2 == 0:
    print 'the integer is even'
else:
    print 'the integer is odd'

print''

print''

print'Lab 02'
print'Question 5'
print''
print'.............................................................................'

print''

primarySchoolAge = 4
legalVotingAge =18
presidentAge = 45
retirementAge = 60
personsAge = input("Enter an age: ")


if personsAge<primarySchoolAge:
    print'Too Young'
    
elif personsAge>=legalVotingAge:
    print 'Remember to Vote'
    
if personsAge>=presidentAge:
    print 'Vote for me'
    
elif personsAge<presidentAge:
     print 'You cant vote.'
     
if personsAge>retirementAge:
     print'Too old.'

print''
print'..........................................................................'
print''
print'Question 7'
print''

print'the values are:'
for i in range (40,-1,-1):
    if i%3 == 0:
        print i
print'..........................................................................'
print''
print'Question 8'
print''


print'the values are:'

for i in range(6,30):
    if (i%2 != 0) and (i%3 != 0) and (i%5 != 0):
        print i


print'..........................................................................'
print''
print'Question 9'
print ''

j=0
while (True):
    if(79*j)%97==1:
        print j
        break
    j+=1


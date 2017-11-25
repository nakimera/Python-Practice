#request in put from useer
num=eval(input('Please enter an integer in the range 0....9999:'))
#attenaute the number if necessary
if num<0:            #make sure number is not too small
    num=0
if num>9999:         #make sure number is not too
    num=9999
    
print(end='[')       #print the left brace

#extract and print thousands-place digit
digit=num//1000     #determine the thousands-place digit
print(digit,end='') #print the thousands-place digit
num%=1000           #discard thousands-place digit

#extract and print hundreds-place digit
digit=num//100      #determine the hundreds-place digit
print(digit,end='') #print the hundreds-place digit
num%=100            #discard hundreds-place digit
 
#extract and print tens-place digit
digit=num//10       #determine the tens-place digit
print(digit,end='') #print the tens-place digit
num%=10             #discard tens-place digit

#remainder is the ones-place digit
print(digit,end='') #print the ones-place digit

print(end=']')       #print the right brace

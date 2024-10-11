newphrase = "rainstorm"
#create a new variable called shortphrase
#and assign value by slicing 
#the newphrase variable by removing
#the first 3 characters
#the last 3 characters
#first 3 characters are "rai"
#last 3 characters are "orm"
#subtring(str,start,end)
shortphrase = newphrase[3:len(newphrase)-3]
print(shortphrase)
#explain len(newphrase)-3= 9 - 3 = 6
#why does it end with 6?
#because the lst index is not included 




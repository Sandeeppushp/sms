import urllib
import requests



print('ARYA College of Engineering and Resrarch Centre\n\nNumbers are:\n')

body='FROM ACERC: Your Child is Absent in Todays Class'



f=open('number.txt','r')
numbers = f.read().split("\n")
print (numbers)



for i in range(0,len(numbers)):
    num=numbers[i]
    data='http://api.msg91.com/api/sendhttp.php?route=4&sender=TESTIN&mobiles='+num+'&authkey=############################&message='+body+' &country=91'
    r = requests.get(url = data)
    print('SMS send successfully to '+num)
    print r

raw_input('Press Enter to Close the Program...')


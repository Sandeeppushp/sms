import urllib.request
import http.cookiejar
import sys
 
def send(username,passwd,message,number,no_of_times):
    message = "+".join(message.split(' '))
    
    for i in range(0,int(no_of_times)):
        Siteurl = 'http://site21.way2sms.com/Login1.action?'
        data = 'username=' + username + '&password=' + passwd + '&Submit=Sign+in'
        
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
        
        #checking username and password
        try:
            usock = opener.open(Siteurl, data.encode('ascii'))
        except IOError:
            print ("Error while logging in. Check Username and Password")
            sys.exit(1)
            
        jession_id = str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site21.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token=' + jession_id + '&mobile=' + number + '&message=' + message + '&msgLen=136'
        opener.addheaders = [('Referer', 'http://site21.way2sms.com/sendSMS?Token=' + jession_id)]
        print('Sending Message to: '+number)
        print('Message: '+message)
        
        try:
            sms_sent_page = opener.open(send_sms_url, send_sms_data.encode('ascii'))
        except IOError:
            print ("Error while sending message")
        print ("SMS has been sent successfully.\n")
        
            

username =input("Enter way2sms Username: ")
passwd =input("Enter password: ")
message = input("Enter your message: ")
number = input('Enter sender mobile number: ')
no_of_times=input('Enter number of times: ')
send(username,passwd,message,number,no_of_times)

import json, urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


#Email function
def send_email(test):
 loginuser = "outmail"
 loginpassword="sSG.my8qYSVtQaaKQgby_2UWDw.BrNxvJXZyAD1elzVUy8qaHIQuCkcs6lfV9Z5OO719Mo"
 fromaddr="aganesh651@gmail "
 toaddr = "akulaganesh@yahoo.com"
 msg = MIMEMultipart()
 msg['From'] = fromaddr
 msg['To'] = toaddr
 msg['Subject'] = "Alert"
 body = "The list of long running job(s) are " + test
 msg.attach(MIMEText(body, 'plain'))
 server = smtplib.SMTP('smtp.sendgrid.net', 587)
 server.starttls()
 server.login(loginuser,loginpassword)
 text = msg.as_string()
 server.sendmail(fromaddr, toaddr, text)
 server.quit()


link="http://172.27.15.194:8088/ws/v1/cluster/apps?states=RUNNING"
#Mention your threshold time in milliseconds
Prescribed_limit=10800000
with urllib.request.urlopen(link) as response:
 result=json.loads(response.read().decode('utf8'))
# Below to parse the json
for jobs in result['apps']['app']:
    if jobs['elapsedTime']>prescribed_limit:
       send_email(str("\nApp Name: {}".format(jobs['name']) +" with Application id: {}".format(jobs['id'])+" running for {} hours".format(round(jobs['elapsedTime']/1000/60/60))))

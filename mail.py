import smtplib,ssl

port=465
smtp_server="smtp.gmail.com"

sender_email="1398abhisingh911@gmail.com"
reciever_email="1398abhisingh911@gmail.com"
password='chintumahi'
message="succeess"

server= smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,receiver_email,message)

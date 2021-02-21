import getpass
import smtplib, ssl

HOST = "smtp.gmail.com"
PORT = 465

username = "lakshyaagarwal8d24@gmail.com"
password = getpass.getpass("Provide Gmail Password: ")

server = smtplib.SMTP_SSL(HOST, PORT)

server.login(username, password)
(235, b'2.7.0 Accepted')
server.sendmail(
    "lakshyaagarwal8d24@gmail.com",
    "2137msglakshya@gmail.com",
    "This is an email sent by Python!",
)
{}
server.quit()
(221, b'2.0.0 closing connection s1sm24313728ljc.3 - gsmtp')
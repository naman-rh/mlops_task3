import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("11.naman.ns@gmail.com@gmail.com", "******")

message1 = "accuracy achieved"

s.sendmail("11.naman.ns@gmail.com", "1706***@kiit.ac.in", message1)


    # terminating the session
s.quit()

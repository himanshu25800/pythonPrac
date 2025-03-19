import smtplib

def sendMail(raddr='boynishant123@gmail.com'):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)

        server.starttls()

        server.login('himanshutest11150@gmail.com','jfaapuwhmyudlsjq')

        server.sendmail('himanshutest11150@gmail.com',raddr,"Data sent")
        print("Email sent")
    except Exception as e:
        print(f"Error occurs {e}")

    
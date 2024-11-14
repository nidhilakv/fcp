import smtplib
import random
otp = random.randint(100000, 999999)
print(otp)
def send_email(to_email, otp):
    from_email = "tech13.exynos@gmail.com"  
    from_password = "liv.eng13"      
    subject = "OTP Code"
    body = "Your OTP code is {otp}"
    message = "Subject: {subject}\n\n{body}"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email")
user_email = input("Enter your email address: ")
send_email(user_email, otp)
user_otp = input("Enter the OTP you received: ")

if user_otp == otp:
    print("OTP verified successfully!")
else:
    print("Invalid OTP. Please try again.")




    
    


    

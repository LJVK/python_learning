import smtplib
import random
import datetime as dt


my_email = "ljvk89@gmail.com"
password = "trefhkwybcuykyaa"
quote_list = []

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt", "r") as file:
        for line in file.readlines():
            quote_list.append(line)

    message = random.choice(quote_list)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ljvk89@yahoo.com",
                            msg=f"Subject:Monday Motivation \n\n {message}")

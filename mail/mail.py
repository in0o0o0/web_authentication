import os
import smtplib
from email.mime.text import MIMEText

from_addr = os.environ["GMAIL_ADDRESS"]
password = os.environ["GMAIL_PW"]
to_addr = "DBから取得したユーザのアドレス"
subject = "認証コード"

msg = MIMEText("作成したコード")
msg["Subject"] = subject
msg["From"] = from_addr
msg["To"] = to_addr

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(from_addr, password)
smtp.sendmail(from_addr, to_addr, msg.as_string())
smtp.close()

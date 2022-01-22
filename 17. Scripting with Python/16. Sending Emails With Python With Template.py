# https://docs.python.org/3/library/string.html#string.Template
# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
from os import name
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

path=Path(__file__).resolve().parent



html = Template(Path(path,'index.html').read_text())
email = EmailMessage()
email['from'] = 'cbinsights2@dabirsiaghi.ir'
email['to'] = 'cbin@dabirsiaghi.ir'
email['subject'] = 'You Won 1,000 dollars!!!!'

email.set_content(html.substitute({'name': 'mohammad'}),'html')
# email.set_content(html.substitute(name='_Mohamamd'))

with smtplib.SMTP(host='mail.dabirsiaghi.ir', port=25) as smtp:
    # smtp.ehlo()
    smtp.starttls()
    smtp.login('cbinsights2@dabirsiaghi.ir', '!QAZ1qaz')
    smtp.send_message(email)
    print('Done')

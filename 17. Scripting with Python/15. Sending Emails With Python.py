# https://docs.python.org/3/library/email.examples.html
# https://mailchimp.com/
# https://www.mailerlite.com/
# https://www.google.com/search?q=smtp&oq=smtp&aqs=chrome..69i57j35i39j0i512l2j69i65j69i60l3.1341j0j4&sourceid=chrome&ie=UTF-8
# https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/
# https://docs.python.org/3/library/email.html#module-email
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'test@mdabir.ir'
email['to'] = 'cbin@dabirsiaghi.ir'
email['subject'] = 'You Won 1,000 dollars!!!!'

email.set_content('I am python developer!!!!!!!')

with smtplib.SMTP(host='mail.mdabir.ir', port=587) as smtp:
    # smtp.ehlo()
    smtp.starttls()
    smtp.login('test@mdabir.ir', '!QAZ1qaz')
    smtp.send_message(email)
    print('Done')


# email['from'] = 'dabirsiaghim@gmail.com'
# email['to'] = 'm_dabirsiaghi@yahoo.com'
# email['subject'] = 'You Won 1,000 dollars!!!!'

# email.set_content('I am python developer!!!!!!!')

# with smtplib.SMTP(host='smtp.gmail.com', port=465) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('dabirsiaghim@gmail.com', '636220mkirD!@#$%')
#     smtp.send_message(email)
#     print('Done')
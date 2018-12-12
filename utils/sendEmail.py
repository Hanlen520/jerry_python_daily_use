from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr

import smtplib
from utils import config


class sendEmail(object):
    def __init__(self):
        self.server_host = config.smtp_server_host
        self.server_port = config.smtp_server_port
        self.from_email = config.smtp_from_email
        self.default_to_email= config.smtp_default_to_email
        self.server_user = config.smtp_server_user
        self.server_password = config.smtp_server_password

    def _format_addrs(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def init_MIMEMultipart(self,to_email,title,content,filename=''):
        msg = MIMEMultipart()
        msg['From'] = self._format_addrs('Autotest platform: %s' % self.from_email)
        msg['To'] = self._format_addrs('User : %s' % to_email)
        msg['Subject'] = Header(title, 'utf-8').encode()
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        if filename !='':
            fp = open(file=filename.replace(u'\u202a', ''), mode='rb')
            msgImage = MIMEImage(fp.read())
            msgImage['Content-Type'] = 'application/octet-stream'
            msgImage['Content-Disposition'] = 'attachment;filename="1.png"'
            fp.close()
            msg.attach(msgImage)
        return msg

    def init_server(self):
        server = smtplib.SMTP(self.server_host, self.server_port)
        server.starttls()
        server.set_debuglevel(1)
        return server

    def sendEmail(self, to_email,title = 'test result', content='', filename=''):
        filename.replace("\\", '/')
        server = self.init_server()
        msg = self.init_MIMEMultipart(to_email,title,content,filename)
        try:
            server.login(self.server_user, self.server_password)
            server.sendmail(self.from_email, [to_email], msg.as_string())
        except smtplib.SMTPAuthenticationError as e:
            print(e)
        except smtplib.SMTPDataError as e:
            print(e)
        server.quit()


def test_send_email():
    import os
    path = os.getcwd()
    sendEmail().sendEmail(to_email =['lizion138@163.com'], title='this is a test email', content='test email content', filename=path+'\\1.png')

if __name__ == '__main__':
    test_send_email()
import smtplib
import os
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr

class send_email_with_attachment():
    def __init__(self,postinfo):
        self.from_addr=postinfo.get('from_addr')
        self.password=postinfo.get('password')
        self.to_addr=postinfo.get('to_addr')
        self.smtp_server=postinfo.get('smtp_server','smtp.163.com')
        #default server is Netease mail

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def make_mail(self,Subject,text,path):
        self.msg=MIMEMultipart()
        self.msg['From']=self._format_addr('<%s>' % self.from_addr)
        self.msg['To']=self._format_addr('<%s>' % self.to_addr)
        self.msg['Subject']=Header(Subject,'utf-8').encode()
        self.msg.attach(MIMEText(text,'plain','utf-8'))
        filename=path.split('\\')[-1]
        with open(path,'rb') as f:
            mime=MIMEBase('application','octet-stream',filename=filename)
            mime.add_header('Content-Disposition', 'attachment', filename=filename)
            # mime.add_header('Content-ID', '<0>')
            # mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            self.msg.attach(mime)

    def send_email(self):
        server = smtplib.SMTP_SSL(self.smtp_server, 465)
        # server.starttls()
        # server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()

class send_email_only_txt():
    def __init__(self,postinfo):
        self.from_addr=postinfo.get('from_addr')
        self.password=postinfo.get('password')
        self.to_addr=postinfo.get('to_addr')
        self.smtp_server=postinfo.get('smtp_server','smtp.163.com')
        #default server is Netease mail

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def make_mail(self,Subject,text):
        self.msg = MIMEText(text, 'plain', 'utf-8')
        self.msg['From'] = self._format_addr('<%s>' % self.from_addr)
        self.msg['To'] = self._format_addr('<%s>' % self.to_addr)
        self.msg['Subject'] = Header(Subject, 'utf-8').encode()
    def send_email(self):
        server = smtplib.SMTP_SSL(self.smtp_server, 465)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()
if __name__=="__main__":
    dic={
        'from_addr':'发件人地址',
        'password':'邮箱授权码',
        'to_addr':'收件人地址'
    }
    mail=send_email_with_attachment(dic)
    Subject='hey man,how are you!!'
    text='we have not say each other for a long time'
    location=os.getcwd()+"\\push\\"+'pic.gif'
    mail.make_mail(Subject,text,location)
    mail.send_email()
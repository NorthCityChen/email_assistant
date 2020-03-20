# email_assistant
 a class used to send email

随便封装了一个class用来发送email

#### 使用方法：

首先需要构造一个字典，其中必须包括三个键：`from_addr,password,to_addr`,另外有`smtp_server`可选

他们分别表示了发件人地址，邮箱授权码，收件人地址，以及邮箱smtp服务器地址，使用时，先实例化一个类

1. `mail=send_email_with_attachment()`表示发送带有附件的邮箱，在向`make_email`方法中传入参数时，需要传入`subject(主题)`、`text(正文)`以及`location(附件的绝对地址)`三个参数，缺一不可

2. `mail=send_email_only_text()`表示发送仅有正文的邮箱，在向`make_email`方法中传入参数时，需要传入`subject(主题)`和`text(正文)`两个参数，缺一不可

然后使用`send_mail`方法发送邮件，看看你的邮箱里有没有收到邮件吧！
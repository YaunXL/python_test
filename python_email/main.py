#-*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方服务
mail_host = 'smtp.qq.com' # 设置服务器
mail_user = '505992504@qq.com'
mail_pass = 'xxxxxxx'

sender = '505992504@qq.com'
receivers = ['18875209107@163.com']
mail_msg = """
<p>Pthon 邮件...</p>
<p><a href = "http://www.baidu.com">请点击链接</a></p>
"""
message = MIMEText(mail_msg,'html','utf-8')
message['From'] = Header("龙",'utf-8')
message['To'] = Header("剑侠",'utf-8')

subject = 'Python 重要邮件'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpobj = smtplib.SMTP_SSL()
    smtpobj.connect(mail_host,465)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
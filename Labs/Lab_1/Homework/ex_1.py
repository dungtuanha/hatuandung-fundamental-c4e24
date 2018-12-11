import datetime
now = datetime.datetime.now()

from gmail import GMail, Message

html_content = '''
<p><strong>ch&agrave;o sếp</strong></p>
<p><em>em bị đau bụng =&gt; em bị kiết lị </em></p>
<p><span style="text-decoration: underline;">nh&acirc;n vi&ecirc;n</span></p>
'''

gmail = GMail('dungngovawater','dungngovawater2504')
msg = Message('DON XIN NGHI OM', to = 'c4e.techkidsvn@gmail.com', html = html_content)

if now.hour > 7:
    gmail.send(msg)
else:
    print("Not yet")
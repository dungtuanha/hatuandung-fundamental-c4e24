from gmail import GMail,Message
from random import *

sickness_list = ["kiết lị", "tiêu chảy"]
symptom_list = ["ỉa ra máu", "ỉa ra nước"]
#select a sickness

i = randint(0,len(sickness_list)-1)
sickness = sickness_list[i]
symptom = symptom_list[i]

html_template = '''
<p><strong>ch&agrave;o sếp</strong></p>
<p><em>em bị {{symptom}} =&gt; em bị {{sickness}}</em></p>
<p><span style="text-decoration: underline;">nh&acirc;n vi&ecirc;n</span></p>
'''
#2. Sickness + html_template = content
#Hint: google: str replace
html_content = html_template.replace("{{sickness}}", sickness, 1)
html_content = html_content.replace("{{symptom}}", symptom, 1)

gmail = GMail('dungngovawater','dungngovawater2504')
msg = Message('Test Message', to = 'c4e.techkidsvn@gmail.com', html = html_content)
gmail.send(msg)
#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import json
from requests.auth import HTTPBasicAuth
url="https://dev69236.service-now.com/api/now/table/incident?sysparm_query=state=1&short_descriptionLIKEalert"
response=requests.get(url,auth=HTTPBasicAuth("admin","BXlKlHamv9H4"))
re=response.json()['result']
print(response.json())
for i in range(1,len(re)):
    state=re[i]['state']
    num=re[i]['number']
    print(state+' and ' + num )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





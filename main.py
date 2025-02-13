import sys
import os
import requests
import datetime

TOKEN=os.environ.get("OWN_TOKEN")
USERNAME=os.environ.get("OWN_USER")
print(TOKEN)

user_endpoint='https://pixe.la/v1/users'

user_parameters={
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOFService':'yes',
    'notMinor':'yes'
}
# response=requests.post(url=user_endpoint,json=user_parameters)
# print(response.text)

graph_parameters={
    'id':'graph1',
    'name':'pages read',
    'unit':'pages',
    'type':'int',
    'color':'sora'
}

headers={
    'X-USER-TOKEN':TOKEN
}

graph_endpoint=f"{user_endpoint}/{USERNAME}/graphs"
# response2=requests.post(url=graph_endpoint,json=graph_parameters,headers=headers)
# print(response2.text) 

today=datetime.datetime.now()
if len(sys.argv) > 1:
    pages_read = sys.argv[1]

pixel_parameters={
    'date':today.strftime("%Y%m%d"),
    'quantity':pages_read
}

pixel_endpoint=f"{graph_endpoint}/graph1"
response3=requests.post(url=pixel_endpoint,json=pixel_parameters,headers=headers)
print(response3.text)

update_parameters={
    'quantity':'12'
}

update_endpoint=f"{pixel_endpoint}/{today.strftime("%Y%m%d")}"
# response4=requests.put(url=update_endpoint,json=update_parameters,headers=headers)
# print(response4.text)

import sys
import os
import requests
import datetime,time

TOKEN=os.environ.get("OWN_TOKEN")
USERNAME=os.environ.get("OWN_USER")
if not TOKEN or not USERNAME:
    print("❌ Error: Environment variables are missing!")
    sys.exit(1)
print(f"Using username: {USERNAME}")
print(f"Token length: {len(TOKEN) if TOKEN else 'MISSING'}")  

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

today=datetime.datetime.now(datetime.timezone.utc).astimezone()

if len(sys.argv) > 1 and sys.argv[1].isdigit():
    pages_read = sys.argv[1]
else:
    print("❌ Error: No valid pages read input received.")
    sys.exit(1)

pixel_parameters={
    'date':today.strftime("%Y%m%d"),
    'quantity':pages_read
}
print(pixel_parameters['date'])
pixel_endpoint=f"{graph_endpoint}/graph1"

MAX_RETRIES = 5  # Retry up to 5 times

for attempt in range(MAX_RETRIES):
    response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
    response_json = response.json()

    if response_json.get("isSuccess"):
        print("Successfully updated graph!")
        break  # Stop retrying
    elif response_json.get("isRejected"):
        print(f"Request rejected. Retrying... ({attempt + 1}/{MAX_RETRIES})")
        time.sleep(2)  # Wait 2 seconds before retrying
    else:
        print(f"Error: {response_json}")
        break  # Stop if there's another type of error



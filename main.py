import requests
PARAMS = {
    'password':"/",
    'grant_type':"password",
    'client_secret':"/",
    'client_id':"/",
    'username':"/"
    }
response = requests.post(
    url = "https://test.salesforce.com/services/oauth2/token",
    params = PARAMS
    )
data = response.json()
token = data['access_token'];
instance_url = data['instance_url']
print(token)

HEADERS = {
    "Authorization" : "Bearer " + token,
    "Content-Type" : "application/json"
}

for x in range(10):
    projectUrl =  instance_url + "/services/data/v55.0/sobjects/Project_TT__c/Project_number__c/TEST" + str(x)
    insertProject = requests.patch(
        url = projectUrl,
        data = '{"Name" : "Test"}',
        headers = HEADERS
    )
    print(insertProject)
    data = insertProject.json()
    print(data)

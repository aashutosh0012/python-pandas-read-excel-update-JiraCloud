'''
jira-assignUsers.py
Script read Users from File: users.xlsx
# customfield_xxxx1 = Country
# customfield_xxxx2 = Branch
# customfield_xxxx3 = Employee
# customfield_xxxx4 = Supervisor
# customfield_xxxx5 = Manager
# customfield_xxxx6 = Sr Manager
# customfield_xxxx7 = Director
# customfield_xxxx8 = Admin
# customfield_xxxx9 = Finance
'''


import requests,json,sys,time, pandas as pd
from requests.auth import HTTPBasicAuth

# assign issuekey, email, api-key from parameters passed to script from Jira webhook
jiraAPIToken=sys.argv[2]
issue_key=sys.argv[1]
email=sys.argv[2]
jiraAPIToken=sys.argv[3]
auth = HTTPBasicAuth(email,jiraAPIToken)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
url = f'https://domain.atlassian.net/rest/api/3/issue/{issue_key}'

# get request to retrive data
response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
data = json.loads(response.text)
country = data['fields']['customfield_xxxx1']['value']
branch  = data['fields']['customfield_xxxx1']['child']['value']

# Read Users File
# To encounter encoding issues, use read_csv with encoding
# users_df = pd.read_csv(file,encoding='ISO-8859-1')
users_df = pd.read_excel('users.xlsx')

# Convert Excel/CSV columns into dictionary pairs using using dict & zip 
# Can also Convert Excel/CSV columns into dictionary pairs using using pandas Dataframe, (UsersName & account_ID), not implemented
accountIDs_df = pd.read_excel('users.xlsx', sheet_name=1)
users_accountIDs = dict(zip(accountIDs_df.Name, accountIDs_df.AccountID))

# Filter Users based on country & branch using pandas dataframes
users = users_df[(users_df['country'] == country) & (users_df['branch'] == branch)]
print(users)

# fecth values from filtered row dataframe cells &
# get account_ID by passing userName as key to dictionary of userName/accountIds, users_accountIDs[username], users_accountIDs[row_df[]],
employee     = users_accountIDs[users['Employee'].values[0]]
Ssupervisor  = users_accountIDs[users['Supervisor'].values[0]]
manager      = users_accountIDs[users['Manager'].values[0]]
srManager    = users_accountIDs[users['Sr Manager'].values[0]]
director     = users_accountIDs[users['Director'].values[0]]
admin        = users_accountIDs[users['Admin'].values[0]]
finance      = users_accountIDs[users['Finance'].values[0]]


#update custom field as payload to be updated to jira
payload = json.dumps( {
    "fields": {
        #"customfield_10196": ceaAdmin,
        "customfield_10197": [{"accountId": sourcing}],
        "customfield_10198": [{"accountId": mananger1}],
        "customfield_10199": [{"accountId": controller1}],
        "customfield_10200": [{"accountId": mananger2}],
        "customfield_10201": [{"accountId": controller2}],
        "customfield_10292": [{"accountId": tfLeader}],
        }
})   

#Update fields in Jira via PUT
response = requests.request(
   "PUT",
   url,
   data=payload,
   headers=headers,
   auth=auth
)
print(f'Response = {response.status_code, response.text}')

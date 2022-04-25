# python-pandas-read-excel-update-JiraCloud
Integration between Jira cloud to read data from Excel using pandas and update via REST API using python script.


#####Jira Automation : Custom Logics | Python, REST API, Jira Cloud.
Whenever an issue is created in Jira, data from an csv/excel/databse can be used to update values in Jira automatically based on input conditions selected by user in Create Request Form.

Jira autoamtion rules can do a lot of automation, much more complex automation can be achived by triggerring webhooks to external programs, talking to each other via REST APIs.

####.Use Case scenario:
Customers place an order in Jira Form selecting Country & Branch Dropdown Select Field, and that ticket can be automatically assigned to corresponding people or team based on Country & Branch selected by user in the Order create Form.

####Steps:

#####Jira Automation
    When a new Ticket is created:
    Trigger a webhook to python script hosted on GithHub-Action Repository with custom data required.
####GitHub Action:
  Then run python script with arguments received from Jira webhook
  Python script, fetches values from Jira issue, does the data processing, business logic or any process, and updates the values to the required fields in Jira issue.
  In this script, we will assign User Picker Custom Field values based on data from an excel sheet.
  When Repository dispatched
  

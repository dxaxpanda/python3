#!/usr/bin/env python3
from jira import JIRA
import re
import os

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
options = {
        'server': 'xxx'
          }
#jira_username = os.getenv('JIRA_USERNAME')
#jira_password = os.getenv('JIRA_PASSWORD')
jira_username = "xxx"
jira_password = "xxx"
defined_project_key = 'STV4'
projects_dir = '/opt/jenkins_scripts' 
project_name = 'sportytrader-front'
version_file = 'prod_ver.txt'
issue_status = 'Done'
print("test")
test = projects_dir+'/'+project_name+'/'+version_file
print(os.stat(test))

# get last deploy date
try: 
    print("[*] Checking if version file exists \n")
    if os.path.exists(projects_dir+'/'+project_name+'/'+version_file):
        with open(projects_dir+'/'+project_name+'/'+version_file, 'r') as version:
            print("[*] Reading content : \n")
            version_date=version.read()
            print(version_date)
            # setup search parameters
            issues_search_parameters = ['project='+defined_project_key, ' AND ', 'status='+issue_status, ' AND ', 'updated > '+version_date]
            # connect to jira api using login form
            print("[*] Connecting to %s as %s\n\n" % (options['server'], jira_username))
            jira = JIRA(options, basic_auth=(jira_username, jira_password))

            # get projects
            projects = jira.projects()
            print("Printing projects:\n", projects)

            # search issues
            issues = jira.search_issues(''.join(issues_search_parameters))

            print("Printing issues found:\n")
            #print(issues)
            tagged_issues = ['['+issue.key+']'+' '+issue.fields.summary for issue in issues]
            print('\n'.join(tagged_issues))
            with open(projects_dir+'/'+project_name+'/'+'changelog.txt', 'w') as f:
                for i in tagged_issues:
                    f.write('<p>'+i+'</p>')
	    	
    else: 
        print("Path doesnt exist: ", projects_dir+'/'+project_name+'/'+version_file)
except Exception as e:
    print(e)


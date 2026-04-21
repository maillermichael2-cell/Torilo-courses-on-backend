# django introduction & setup | mtv architecture | first app

## WHATS django?
django is a high level open source python web framework that enables rapid dev of  a secure maintanable websites.

### django vs flask vs fastapi (quick comparism)

| feature       | django                    | flask             | fast api              |
|---------------|---------------------------|-------------------|-----------------------|
| type          | full-stack framework      | micro framework   | api framework         |
| admin-panel   | built in                  | manual            | manual                |
| orm           | built in                  | needs extra       | needs extra           |
| best for      | full web apps             | small apps        | high perfomace apis   |
| lerning curve | moderate                  | low               | moderate              |

## mtv architecture
    django follows the model template view pattern. it looks similar to the well known mvc pattern in naming diffrent. understanding this flow is essential every respect that hits yoru django app gets through this circle.

| layer     | mvc equivalent | responsibility                               | django- file      |
|-----------|----------------|----------------------------------------------|-------------------|
| model     | Model          | data structures and data logic               | models.py         |
| teamplet  | view           | html presentation                            | templates/html    |
| view      | controller     | bussiness logic connects model& template     | view.py           |      

### Request respinse cycle 
1 browser sends request 
2 django checks urls.py finds the matching url pattern
3 django calls the mapped view function in views.py
4 the view fetched data from models.py if needed 
5 the view passes data to the template html file


### creating and registerin app 
a django priject is the entire we app. a django app is a self contained module withing the project that handles specific feature - eg products, users, blog one project can have many apps.

. py manage.py startapp myapp


## views & url routing 
a view is a python function that recievec a http request and returns 

## sql basics 

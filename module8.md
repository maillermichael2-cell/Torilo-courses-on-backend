# module 8 django models , orm | sql basics & migrations

## 1. sql basics (structure query language)
    sql is how you communicate with a relational database. django orm writes sql for you automatically , but knowing the basics helps you 
understand what django is doing , and write custom queries when needed.

| **operation**     |  sql command                                              | what it does 
|-------------------|-----------------------------------------------------------|----------------------------------
| read              | "SELECT" FROM products                                    | retrive all rows from the table
| filter            | *SELECT* FROM  products WHERE price > 5000                | retrive rows matchig a condition
| create            | INSERT INTO products (name, price) VALUES ('bag', 3000)   | add a new row
| update            | UPDATE products set price = 3500 where id == 1            | modify an existing row
| delete            | delete from products where id == 1                        | delete an existing row


##DJANGO MODELS
 a django model is a python class that mpas directly to a database table , each class attribute becomes a column, django reads these 
 class definations and generates all the sql to create , altar and query yoru tables.


# migrations
a migrations is a python file that records changes to your models and knows hot to apply then to the database. Every time
you create or change a model you generate a migration and apply it .Think of migrations as a version control for your database schema .


1. py manage.py makemigrations : it reads all pending migrations files and execute their sql 
2. py manage.py migrate : 
3. py manage.py showmigrations : shows all the migartions applied 

###DJANGO ORM - QUERYING DATA WITH PYTHON 
the orm (object relational mapper) lets you read and write datbase data using python instead of sql. Django translate your python method calls into
the correct SQL  queries automatically. the django shell is the best place to practice 

using python shell : py manage.py shell in your powershell terminal.

first - from myapp.models import Product, Category
add records:
    cat = Category.objects.create(name='Electronics', description='Tech Products')
    p1 = Product.objects.create(name='Laptop', price=25000, stock=10, category=cat)
    p2 = products.objects.create(name='Phone', price=12000, stock=25, category=cat)

    get all
    Products.objects.all()

    filter 
    Product.objects.filter(stock__gt=0) stock > 0
    Product.objects.filter(price__lt=200000) price < 200,000
    Product.objects.filter(category=cat) products in a specific category

    Product.objects.get(id=1)

    foriegn key links 2 models

## django admin 
        py manage.py createsuperuser - this creates a super user for us a super user hass access to the admin panel.
        super user info : username : dare
                          email: dare@gmail.com
                          password : dare1234



### git hub 

create a repo 
create a git ignore 

code : 
    git init - initializes a git file 
    git add . - add all files to the staging environment 
    git commit -m "the classwork (blog)"
    git remote add origin https://github.com/username/reponame.git
    git push -u origin main or master


    add to exsting repo
        git add .
        git commit -m 'message'
        git push
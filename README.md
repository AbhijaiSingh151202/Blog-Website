# Blog-Website
*** Deprecation ***
This project was created following the 'django 3 by example' book. You can check their Github at [here](https://github.com/PacktPublishing/Django-3-by-Example)

Django Blog
This is a very simple Blog website built with Django.

Project Summary
---
First of all the website shows the home page from where you are go to the blog page. When the user goes to the bolg page their the user can see all the blog. on each page their would be 3 blogs. The user can open any blog and can also comment on that blog. At the right side the user can see what are the latest posts and can also see the most commented posts. Under the most commented posts part the user can see a link that makes the user subcribe to the rss feed of this blog website.

[![alt text]

Running this project
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

pip install virtualenv
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

virtualenv env
That will create a new folder env in your project directory. Next activate it with this command on mac/linux:

source env/bin/active
Then install the project dependencies with

pip install -r requirements.txt
Now you can run the project with this command

python manage.py runserver
Note if you want payments to work you will need to enter your own Stripe API keys into the .env file in the settings files.

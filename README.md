### *** Deprecation ***
This project was created following the 'django 3 by example' book. You can check their Github at [here](https://github.com/PacktPublishing/Django-3-by-Example)
___

# Blog-Website
This is a very simple Blog website built with Django.

Project Summary
---
First of all the website shows the home page from where you are go to the blog page. When the user goes to the bolg page their the user can see all the blog. on each page their would be 3 blogs. The user can open any blog and can also comment on that blog. At the right side the user can see what are the latest posts and can also see the most commented posts. Under the most commented posts part the user can see a link that makes the user subcribe to the rss feed of this blog website.

___
Running this project
---
Their are some steps that you need to follow to get this project up and running.

### 1st Step
You should have Python installed on your computer.

### 2nd Step
Clone or download this repository and open it in your editor of choice. In a terminal, run the following command in the base directory of this project.
```
env\Scripts\activate
```

### 3rd Step
Then install the project dependencies with
```
pip install -r requirements.txt
```
in any case if you get an error try running
```
python -m pip install -r requirements.txt
```

### 4th Step
Now you can run the project with this command
```
python manage.py runserver
```

**Note: if you want to share a post make sure to change the email and it's password in the settings.py file and also
remeber to turn on allow less-secure apps on the mail you would be using**
**Note: Do Not Use A Important mail make a new one and make sure it does not contains any type of official data of yours**

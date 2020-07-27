drf8react is a start of the project: django rest-framework with react redux.
I wanted to have a base project for my other django-react projects.
If you are looking for a fullstack project that simply manages users by profile, this project can help you.
I created an accounts application where there is a Profile model in OneToOne with the django.contrib.auth.models.User.
I serialized it to retrieve that value from the profile instead of an object embedded in User.

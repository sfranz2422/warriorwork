from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


    # remember to make migrations in the terminal and then migrate
class Week(models.Model):

    last_name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 100)
    week = models.CharField(max_length = 100)
    monday = RichTextField(blank=False)
    tuesday = RichTextField(blank=False)
    wednesday = RichTextField(blank=False)
    thursday = RichTextField(blank=False)
    friday = RichTextField(blank=False)


    # created will not show in the admin because it is auto added
    created = models.DateTimeField(auto_now_add = True)
    # need datetimes to be null and not blank like text fields
    # blank = true below allows it to be blank in the admin console

    # need a foreign key one to many relationship
    # did not need to call this user below.  not the same user variable
    # that is authenticated in the views.py
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    # this function below will make the tite of the todo in the admin
    # the actual title of the todo
    def __str__(self):
        # month = self.week.strftime("%b")
        # day = self.week.strftime("%d")
        # year = self.week.strftime("%Y")
        # return_date = "Week of " + month + " " + day + ", " + year
        return self.week

    # remember to make migrations in the terminal and then migrate

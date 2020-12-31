from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


    # remember to make migrations in the terminal and then migrate
class Week(models.Model):
    SUBJECT_CHOICES =(
        ("Art", "Art"),
        ("Business/Computer", "Business/Computer"),
        ("English", "English"),
        ("F.C. Science", "F.C. Science"),
        ("Foreign Language", "Foreign Language"),
        ("Math", "Math"),
        ("Music/Band", "Music/Band"),
        ("Phys Ed./Health", "Phys Ed./Health"),
        ("Science", "Science"),
        ("Social Studies", "Social Studies"),
        ("Special Ed.", "Special Ed."),
        ("Tech Education", "Tech Education"),
        )

    LAST_NAME_CHOICES = (
    ('Smith', 'Smith'),
    ('Franz', 'Franz'),
    ('Jones', 'Jones'),
    ('Doe', 'Doe'),

    )

    WEEK_CHOICES = (
    ('01/04/2021', '01/04/2021'),
    ('01/11/2021', '01/11/2021'),
    ('01/18/2021', '01/18/2021'),
    ('01/25/2021', '01/25/2021'),
    ('02/01/2021', '02/01/2021'),
    ('02/08/2021', '02/08/2021'),
    ('02/15/2021', '02/15/2021'),
    ('02/22/2021', '02/22/2021'),
    ('03/01/2021', '03/01/2021'),
    ('03/08/2021', '03/08/2021'),
    ('03/22/2021', '03/22/2021'),
    ('03/29/2021', '03/29/2021'),
    ('04/05/2021', '04/05/2021'),
    ('04/12/2021', '04/12/2021'),
    ('04/19/2021', '04/19/2021'),
    ('04/26/2021', '04/26/2021'),
    ('05/03/2021', '05/03/2021'),
    ('05/10/2021', '05/10/2021'),
    ('05/17/2021', '05/17/2021'),
    ('05/24/2021', '05/24/2021'),
    ('05/31/2021', '05/31/2021'),
    ('06/07/2021', '06/07/2021'),
    )
    last_name = models.CharField(max_length = 200,choices=LAST_NAME_CHOICES)
    subject = models.CharField(max_length = 100, choices=SUBJECT_CHOICES)
    week = models.CharField(max_length = 100, choices=WEEK_CHOICES)
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
        return_info = self.last_name + " " + self.subject + " " + self.week
        return return_info

    # remember to make migrations in the terminal and then migrate

from django.db import models


# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=30)
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=11)
    work_phone = models.CharField(max_length=11)
    jobCode = models.ForeignKey(Job, on_delete=models.CASCADE, null=False, blank=False, related_name='PersonJob')
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

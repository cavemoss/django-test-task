from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    employer_id = models.CharField(max_length=255)
    team = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""
id: {self.id}
title: {self.title}
description: {self.desc}
employer: {self.employer} id:{self.employer_id}
required team of {self.team} people
"""
    
class TeamMember(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=255)
    member_id = models.CharField(max_length=255)
    pending = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} name: {self.member_name} id:{self.member_id}"
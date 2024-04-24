from django.contrib import admin
from .models import Project, TeamMember

admin.site.register([Project, TeamMember])
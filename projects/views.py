from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Project, TeamMember

User = get_user_model()

def home(response):

    if response.method == 'POST':
        project = Project.objects.get(id=response.POST.get('project_id'))

        try: project.teammember_set.get(member_id=response.user.id)

        except: 
            project.teammember_set.create(
                member_name=f'{response.user.last_name} {response.user.first_name}',
                member_id=response.user.id
            )

    context = {
        'user' : response.user,
        'projects' : Project.objects.all(),
    }

    return render(response, 'projects/projects.html', context)


def account(response, id):

    user = response.user
    account = User.objects.get(id=id)
    projects = Project.objects.filter(employer_id = account.id)

    pending_applicants = []    
    for project in projects: 
        for one in project.teammember_set.all():
            if(one.pending is True): pending_applicants.append(one)
            
    my_projects = []
    for project in Project.objects.all():
        for one in project.teammember_set.all():
            if(account.id == int(one.member_id) and one.pending is False): my_projects.append(project)

    if response.method == 'POST':

        if response.POST.get("project_id") is not None:
            Project.objects.get(id=response.POST.get("project_id"))\
            .teammember_set.filter(member_id=response.POST.get("member_id"))\
            .update(pending=False)

        elif response.POST.get("project_id_fire") is not None:
            Project.objects.get(id=response.POST.get("project_id_fire"))\
            .teammember_set.filter(member_id=response.POST.get("member_id"))\
            .delete()

        else:
            title = response.POST.get("title")
            text = response.POST.get("desc")
            team = int(response.POST.get("team"))
            Project(title=title, desc=text, employer=f'{user.last_name} {user.first_name}', employer_id=user.id, team=team).save()
    
    context = {
        'user' : user,
        'account' : account,
        'projects' : projects,
        'applicants' : pending_applicants,
        'my_projects' : my_projects
    }

    return render(response, 'projects/account.html', context)


from django.shortcuts import render
from .models import *


def homepage(request):
    work = Work.objects.all()
    skill = Skill.objects.all()
    award = Award.objects.all()
    info = Info.objects.first()

    context = {
        'info': info,
        'work': work,
        'award': award,
        'skill': skill,
    }
    return render(request, 'home_page/index.html', context)




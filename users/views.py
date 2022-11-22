from django.shortcuts import render, get_object_or_404

from .choices import UserRole
from .models import User, Skill


def profiles(request):
    profiles = User.objects.filter(role=UserRole.DEVELOPER).all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = User.objects.get(id=pk)

    main_skills = profile.skills.all()[:2]
    extra_skills = profile.skills.all()[2:]

    context = {'profile': profile, 'main_skills': main_skills,
               "extra_skills": extra_skills}
    return render(request, 'users/user-profile.html', context)


def profiles_by_skill(request, skill_slug):
    skill = get_object_or_404(Skill, slug=skill_slug)
    profiles = User.objects.filter(skills__in=[skill])
    context = {
        "profiles": profiles
    }

    return render(request, "users/profiles.html", context)

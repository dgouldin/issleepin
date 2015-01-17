from __future__ import absolute_import
from django.shortcuts import render

from .models import Profile

def profile(request):
    slug = 'eden' # TODO: request.subdomain
    try:
        profile = Profile.objects.get(slug=slug)
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'main/profile.html', {
        'slug': slug,
        'profile': profile,
    })

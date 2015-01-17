from __future__ import absolute_import
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseForbidden, HttpResponseBadRequest

from .forms import ProfileForm
from .models import Profile

def profile(request):
    slug = request.subdomain
    try:
        profile = Profile.objects.get(slug=slug)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        if profile is None:
            raise Http404
        if profile.user != request.user:
            raise HttpResponseForbidden
        if request.POST.get('sleeping') not in ['true', 'false']:
            raise HttpResponseBadRequest
        profile.sleep_logs.create(sleeping=(request.POST['sleeping'] == 'true'))
        return redirect('/')


    return render(request, 'main/profile.html', {
        'slug': slug,
        'profile': profile,
    })

@login_required
def claim(request):
    slug = request.subdomain
    if Profile.objects.filter(slug=slug).exists():
        return redirect('/')

    instance = Profile(slug=slug, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProfileForm(instance=instance)

    return render(request, 'main/claim.html', {
        'slug': slug,
        'form': form,
    })

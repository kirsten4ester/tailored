from django.shortcuts import render, redirect

from .models import Photographer, Shoot
# from .forms import PhotographerForm, ShootForm
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'tailored/landing.html')

@login_required
def photographer_list(request): 
    photographers = Photographer.objects.all()
    return render(request, 'tailored/photographer_list.html', {'photographers': photographers})

@login_required
def photographer_detail(request, pk):
    photographer = Photographer.objects.get(id=pk)
    return render(request, 'tailored/photographer_detail.html', {'photographer': photographer})


def photographer_create(request):
    if request.method == 'POST':
        form = PhotographerForm(request.POST)
        if form.is_valid():
            photographer = form.save()
            return redirect('photographer_detail', pk=photographer.pk)
    else:
        form = PhotographerForm()
    return render(request, 'tailored/photographer_form.html', {'form': form})

def photographer_edit(request, pk):
    photographer = Photographer.objects.get(pk=pk)
    if request.method == "POST":
        form = PhotographerForm(request.POST, instance=photographer)
        if form.is_valid():
            photographer = form.save()
            return redirect('photographer_detail', pk=photographer.pk)
    else:
        form = PhotographerForm(instance=photographer)
    return render(request, 'tailored/photographer_form.html', {'form': form})

def photographer_delete(request, pk):
    Photographer.objects.get(id=pk).delete()
    return redirect('photographer_list')

@login_required
def shoot_list(request):
    shoots = Shoot.objects.all()
    return render(request, 'tailored/shoot_list.html', {'shoots': shoots})

@login_required
def shoot_detail(request, pk):
    shoot = Shoot.objects.get(id=pk)
    return render(request, 'tailored/shoot_detail.html', {'shoot': shoot})

def shoot_create(request):
    if request.method == 'POST':
        form = ShootForm(request.POST)
        if form.is_valid():
            shoot = form.save()
            return redirect('shoot_detail', pk=shoot.pk)
    else:
        form = ShootForm()
    return render(request, 'tailored/shoot_form.html', {'form': form})

def shoot_edit(request, pk):
    shoot = Shoot.objects.get(pk=pk)
    if request.method == "POST":
        form = ShootForm(request.POST, instance=shoot)
        if form.is_valid():
            shoot = form.save()
            return redirect('shoot_detail', pk=shoot.pk)
    else:
        form = ShootForm(instance=shoot)
    return render(request, 'tailored/shoot_form.html', {'form': form})

def shoot_delete(request, pk):
    Shoot.objects.get(id=pk).delete()
    return redirect('shoot_list')
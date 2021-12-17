from django.shortcuts import render, redirect
from .models import Laptop
from .forms import LaptopModelForm


def addLaptop(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')
    return render(request, 'Laptopapp/addLaptop.html', {'form':form})


def showLaptop(request):
    laptops = Laptop.objects.all()
    return render(request, 'Laptopapp/showLaptop.html', {'laptops': laptops})


def deleteLaptop(request,i):
    laptop = Laptop.objects.get(id=i)
    if request.method == 'POST':
        laptop.delete()
        return redirect('show_laptop')
    return render(request, 'Laptopapp/showLaptop.html', {'laptop': laptop})

def updateLaptop(request,i):
    laptops = Laptop.objects.get(id=i)
    form = LaptopModelForm(instance=laptops)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST, instance=laptops)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')
    return render(request,'Laptopapp/addLaptop.html', {'form': form})





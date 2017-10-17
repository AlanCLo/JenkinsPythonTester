# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat
from .forms import CatForm

# Create your views here.

def cat_list(request):
	cats = Cat.objects.all().order_by('created_date')
	return render(request, 'blahapp/cat_list.html', { 'cats': cats })

@login_required
def cat_new(request):
	if request.method == "POST":
		form = CatForm(request.POST)
		if form.is_valid():
			cat = form.save(commit=False)
			cat.save()
			return redirect('cat_detail', pk=cat.pk)
	else:
		form = CatForm()
	return render(request, 'blahapp/cat_edit.html', {'form': form})

def cat_detail(request, pk):
	cat = get_object_or_404(Cat, pk=pk)
	return render(request, 'blahapp/cat_detail.html', {'cat': cat})

@login_required
def cat_edit(request, pk):
	cat = get_object_or_404(Cat, pk=pk)
	if request.method == "POST":
		form = CatForm(request.POST, instance=cat)
		if form.is_valid():
			cat = form.save(commit=False)
			cat.save()
			return redirect('cat_detail', pk=cat.pk)
	else:
		form = CatForm(instance=cat)
	return render(request, 'blahapp/cat_edit.html', {'form': form})


def cat_delete(request, pk):
	cat = get_object_or_404(Cat, pk=pk)
	cat.delete()
	return redirect('cat_list')






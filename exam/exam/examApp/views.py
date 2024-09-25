from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def landing(request):
	return render(request,"landing.html")

def displayall(request):
	if request.session.get('uname')==None:
		return redirect(login)
	disp=taskModel.objects.all()
	return render(request,"displayall.html",{"disp":disp})

def add(request):
	if request.session.get('uname')==None:
		return redirect(login)
	if request.method=="POST":
		form=taskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(displayall)
	else:
		form=taskForm()
	return render(request,"add.html",{"form":form})

def signin(request):
	if request.method=="POST":
		form=userForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(login)

	else:
		form=userForm()
		return render(request,"Signin.html",{"form":form})

def login(request):
	if request.method=="POST":
		form=userForm(request.POST)
		if form.is_valid():
			u=form.cleaned_data.get('uname')
			p=form.cleaned_data.get('psw')
			c=userModel.objects.filter(uname=u,psw=p)
			if len(c)>0:
				request.session['uname']=u
				return redirect(displayall)

	else:
		form=userForm()
		return render(request,"Login.html",{"form":form})

def delete(request,id):
	d=get_object_or_404(taskModel,pk=id)
	d.delete()
	return render (request,"delete.html")

	
def edit(request,id):
	if request.method=="POST":
		form=taskModel(request.POST,instance=e)
		if form.is_valid():
			form.save()
			return redirect(displayall)
	else:
		form=taskForm(instance=e)
	return render(request,'edit.html')

def logout(request):
	del request.session['uname']
	return redirect(login)

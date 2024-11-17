from django.shortcuts import render
from .forms import CreateUserForm
from django.http import HttpResponse

def HomeCreateUser(request):
    form = CreateUserForm()
    return render(request, 'register.html',{'form':form})

def ValidateCrtUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
        return HttpResponse('Tudo certo')
    return HttpResponse('Ocorreu um erro no formulário')
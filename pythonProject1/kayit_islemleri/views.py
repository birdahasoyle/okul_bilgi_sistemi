from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import kayit_formu
from .models import Okul


def home(request):
    return render(request, 'home.html')


def register_form(request, id=0):

     if request.method == "GET":
        if id==0:
            form = kayit_formu()
        else:
            kayit = Okul.objects.get(pk=id)
            form = kayit_formu(instance=kayit)
        return render(request, 'Register_Form.html', {'form': form})
     else:
         if id==0:
            form = kayit_formu(request.POST)
         else:
            kayit = Okul.objects.get(pk=id)
            form = kayit_formu(request.POST, instance=kayit)
         if form.is_valid():
             form.save()
             # if form.data['kayit_turu']==2:
             #     return redirect('ogrenciliste/')
     return redirect('liste/')


def register_list(request):
    context = {'register_list': Okul.objects.all()}
    return render(request, "Register_List.html", context)


def ogrenci_list(request):
     context = {'register_list': Okul.objects.filter(kayit_turu=3)}
     return render(request, "Register_List.html", context)


def ogretmen_ogrenci_list(request):
    context = {'register_list': Okul.objects.exclude(kayit_turu=1)}
    return render(request, "Register_List.html", context)


def record_delete(request, id):
    kayit = Okul.objects.get(pk=id)
    kayit.delete()
    return redirect('liste/')


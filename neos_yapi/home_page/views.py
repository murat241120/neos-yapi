from django.shortcuts import redirect, render, HttpResponse
from.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def homepage(request):
    return render(request, "neosyapi.html")

def hakkimizda(request):
    return render(request,"hakkimizda.html")

def bizkimiz(request):
    return render(request,"bizkimiz.html")

def galeri(request):
    resim1 = resim.objects.all()
    paginator = Paginator(resim1, 6) # Show 25 contacts per page
    page = request.GET.get('page')
    
    try:
        resim1 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        resim1 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        resim1 = paginator.page(paginator.num_pages)
    nums = "a" * resim1.paginator.num_pages
    return render(request,"galeri.html", {"resim1":resim1, "nums":nums})

def urunler(request):
    data = kategori.objects.all()
    veri_cek = {"kategori":data}
    return render(request,"urunler2.html",veri_cek)

def urunler_dinamik(request,id):
    data = kategori.objects.filter(id = id)
    veri_cek = {"kategori":data}
    return render(request,"urun_goster.html",veri_cek)

def iletisim(request):
    return render(request, "iletisim.html")

def sss(request):
    return render(request, "sss.html")
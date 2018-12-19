from django.shortcuts import render

# Create your views here.
from mainproject.models import Books


def sesrch(request):
    return render(request,'header.html')


def showinfo(request,num):
    num = int(num)
    book_list = Books.objects.filter(bk_id=num)
    return render(request,'showinfo.html',{'book_list':book_list})
from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Departments,Doctors
# Create your views here.
def index(requst):
    # numbers={
    #     'num1':[1,2,3,4,5,6,7,8,9],
    # }

    # person ={
    #     'name':'john',
    #     'age':30,
    #     'place':'calicut'
    # }
    return render(requst,'index.html')  #person argument passing


def about(requst):
    return render(requst,'about.html')


def booking(requst):
    if requst.method=="POST":
        form = BookingForm(requst.POST)
        if form.is_valid():
            form.save()
            return render(requst,'confirmation.html')
    form = BookingForm()
    dic_form={
        'form' : form
    }
    return render(requst,'booking.html',dic_form)


def doctors(requst):
    dict_docs = {
        'doctors':Doctors.objects.all()
    }
    return render(requst,'doctors.html',dict_docs)

def contact(requst):
    return render(requst,'contact.html')

def department(requst):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(requst,'department.html',dict_dept)
 


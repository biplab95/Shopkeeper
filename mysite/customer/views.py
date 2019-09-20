from django.shortcuts import render,redirect,HttpResponse
from .forms import CustomerForm
from .models import Customer
from django.contrib import messages
# Create your views here.

def customer_signup(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Customer Added Successfully !')

    d ={
        'form':form
    }


    return render(request,'customer/signup.html',d)

def show_customer(request):
    c = Customer.objects.all()

    context ={
        'c':c
    }

    return render(request,'customer/customers.html',context)

def update_customer(request,id):
    customer = Customer.objects.get(id=id)



    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('all_customers')

    d = {
        'form': form
    }
    return render(request,'customer/signup.html',d)


def delete_customer(request,id):
    customer =Customer.objects.get(id=id)
    if request.method =='POST':

        customer.delete()
        return redirect('all_customers')
    return render(request,'customer/confirm.html')
    # return HttpResponse("Data delete ho gya")

from django.shortcuts import render


# Create your views here.
#from mysite.forms import ContactForm,ListForm,UserForm
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from banksite.forms import CsvForm
from bankapp.models import Account, Credit, Customer, Interest, Region, Csv
from datetime import datetime
from datetime import date
import csv
from django.db.models import Sum







def main(request):
    if request.method == 'POST':
        form = CsvForm(request.POST ,request.FILES or None )
        if form.is_valid():
            cd = form.cleaned_data
            csv=request.FILES['csv']
            print("CSV NAME")
            print(csv)
            Csv.objects.create(csv=request.FILES['csv'])

        form = CsvForm()    
        return render(request,'main.html',{'form': form})               
    else:
        form = CsvForm()
    return render(request, 'main.html', {'form': form})  


def store(request):
    with open('../media_cdn/AccountTable.csv','r') as csv_file:
        print(csv_file)
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if row[2]=="":
                row[2]=-1
            Account.objects.create(acct_id=row[0],acct_type=row[1],balance=row[2],overdraft_history=row[3])

    with open('../media_cdn/CreditTable.csv','r') as csv_file:
        print(csv_file)
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            Credit.objects.create(timestamp=row[0],existing_npa=row[1],cash_reserve=row[2])

    with open('../media_cdn/CustomerTable.csv','r') as csv_file:
        print(csv_file)
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            Customer.objects.create(cust_id=row[0],name=row[1],birth_date=row[2],fam_dependency=row[3],account_no=row[4],income=row[5],pincode=row[6])

    with open('../media_cdn/InterestRateTable.csv','r') as csv_file:
        print(csv_file)
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            Interest.objects.create(timestamp=row[0],mclr=row[1],fdr=row[2])

    with open('../media_cdn/RegionTable.csv','r') as csv_file:
        print(csv_file)
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            Region.objects.create(pincode=row[0],address = row[1])
    return render(request, 'main.html',{'display': True})  


def display(request):
    account_list = Account.objects.all()
    credit_list = Credit.objects.all()
    customer_list = Customer.objects.all()
    interest_list = Interest.objects.all()
    region_list = Region.objects.all()
    return render(request, 'display.html',{'account_list':account_list, 'credit_list':credit_list,'customer_list':customer_list,'interest_list':interest_list,'region_list':region_list})  


def duplicate(request):

    for row in Account.objects.all():
        if Account.objects.filter(acct_id=row.acct_id).count() > 1:
            row.delete()

    for row in Credit.objects.all():
        if Credit.objects.filter(timestamp=row.timestamp).count() > 1:
            row.delete()

    for row in Customer.objects.all():
        if Customer.objects.filter(cust_id=row.cust_id).count() > 1:
            row.delete()

    for row in Interest.objects.all():
        if Interest.objects.filter(timestamp=row.timestamp).count() > 1:
            row.delete()

    for row in Region.objects.all():
        if Region.objects.filter(pincode=row.pincode).count() > 1:
            row.delete()
    return render(request, 'main.html')  


def try_parsing_date(text):
    
    for fmt in ('%m-%d-%Y', '%m.%d.%Y', '%m/%d/%Y'):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    

def calculate_age(born):

    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def date_correction(request):
    for row in Customer.objects.all():
        if row.age!=-1:
            return render(request, 'main.html',{'display': True}) 
    for row in Customer.objects.all():
        birthday = row.birth_date
        corrected_birthday= try_parsing_date(birthday)  
        row.birth_date= corrected_birthday
        row.age= calculate_age(corrected_birthday)
        row.save()
    return render(request, 'main.html',{'display': True})  

def name_correction(request):
    for row in Customer.objects.all():
        name = row.name
        data = name.split()
        row.first_name=data[0]
        row.last_name=data[1]
        row.save()
    return render(request, 'main.html',{'display': True})  

def missing_value_correction(request):
    total_sum = Account.objects.aggregate(Sum('balance'))
    total_count = Account.objects.all().count()
    average_balance = total_sum.values()[0]/total_count
    queryset = Account.objects.filter(balance=-1)
    for row in queryset:
        row.balance= average_balance
        row.save()
    return render(request, 'main.html',{'display': True}) 






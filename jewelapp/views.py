
from .models import Dealer,Seldealer
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import StudentAddForm,LecturerAddForm,Dealerform,seldealerforms
import datetime
from django.db.models import Sum


# Create your views here.
def home(request):
    return render(request,"home.html")
def slog(request):
    return render(request,"slog.html")
def tlog(request):
    return render(request,"tlog.html")



def dail(request):
    
    student = Seldealer.objects.all()

    my_data_list = list(student.values_list('sstore_name'))
    distinct_values_sstore_name = set()

    for item in my_data_list:
        values = str(item[0]).split(',')
        for value in values:
            distinct_values_sstore_name.add(value.strip())

    distinct_values_list_sstore_name = list(distinct_values_sstore_name)



    my_data_list = list(student.values_list('scommuni'))
    distinct_values_scommuni = set()

    for item in my_data_list:
        values = str(item[0]).split(',')
        for value in values:
            distinct_values_scommuni.add(value.strip())

    distinct_values_list_scommuni = list(distinct_values_scommuni)


    my_data_list = list(student.values_list('sname'))
    distinct_values_sname = set()

    for item in my_data_list:
        values = str(item[0]).split(',')
        for value in values:
            distinct_values_sname.add(value.strip())

    distinct_values_list_sname = list(distinct_values_sname)

    
    my_data_list = list(student.values_list('sproduct_name'))
    distinct_values_sproduct = set()

    for item in my_data_list:
        values = str(item[0]).split(',')
        for value in values:
            distinct_values_sproduct.add(value.strip())

    distinct_values_list_sproduct = list(distinct_values_sproduct)

  
    my_data_list = list(student.values_list('stype_of_product'))
    distinct_values_type = set()

    for item in my_data_list:
        values = str(item[0]).split(',')
        for value in values:
            distinct_values_type.add(value.strip())

    distinct_values_list_type = list(distinct_values_type)

    formdd = Dealerform()
    if request.method== 'POST':
        formdd = Dealerform(request.POST)
        if formdd.is_valid():
            sn  = request.POST['name']
            pap = request.POST['store_name']
            aut = request.POST['contact']
            jou = request.POST['product_name']
            ind = request.POST['type_of_product']
            dfd = request.POST['created_at']
            fd  = request.POST['product_quality']
            hu = request.POST['precious_metal']
            we = request.POST['percent']
            zs = request.POST['pure_rate']
            tyu = (int(zs)/100*int(we))
            print(tyu)
            Dealer.objects.create(name = sn, store_name =pap, contact =aut, product_name= jou, type_of_product=ind,created_at=dfd,product_quality  =  fd,percent = we,precious_metal = hu,discount = tyu,pure_rate = zs)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'tlogfor.html', {'student': student,'distinct_values_sstore_name': distinct_values_list_sstore_name, 'distinct_values_scommuni': distinct_values_list_scommuni, 'distinct_values_sname': distinct_values_list_sname, 'distinct_values_sproduct': distinct_values_list_sproduct, 'distinct_values_type': distinct_values_list_type})



def seldail(request):
    fo = seldealerforms()
    fdf = Seldealer.objects.all()
    if request.method== 'POST':
        fo = seldealerforms(request.POST)
        if fo.is_valid():
            sn  = request.POST['sname']
            pap = request.POST['sstore_name']
            aut = request.POST['scommuni']
            jou = request.POST['sproduct_name']
            ind = request.POST['stype_of_product']
            print(type(jou))
            Seldealer.objects.create(sname = sn, sstore_name =pap, scommuni =aut, sproduct_name= jou, stype_of_product=ind)
            messages.success(request,'saved successfully')

            return redirect('/sel/')
    return render(request, 'mas.html',{'ket':fdf})



from dateutil import parser

def dret(request):
    persons = Dealer.objects.all()
    if request.method == 'POST': 
        start_date_str = request.POST['fo']
        end_date_str = request.POST['to']
        typ = request.POST['sel']
       
        try:
            start_date = parser.parse(start_date_str).date() if start_date_str else None
            end_date = parser.parse(end_date_str).date() if end_date_str else None
            if start_date and end_date and typ:
                pers = persons.filter(created_at__range=(start_date, end_date), precious_metal=typ)
                return render(request,'dret.html',{'ket':pers})
            elif start_date and end_date:
                perspo = persons.filter(created_at__range=(start_date, end_date))
                pure = persons.filter(created_at__range=(start_date, end_date)).aggregate(total_pure_rate=Sum('pure_rate'))
                dis = persons.filter(created_at__range=(start_date, end_date)).aggregate(total_discount=Sum('discount'))
                por = pure['total_pure_rate'] - dis['total_discount']
                return render(request, 'dret.html', {'po':por,'total_pure_rate': pure['total_pure_rate'],'ket':perspo,'total_discount':dis['total_discount']})
            else:
                pers = persons.filter(precious_metal=typ) 
                pure = persons.filter(precious_metal=typ).aggregate(total_pure_rate=Sum('pure_rate'))
                dis = persons.filter(precious_metal=typ) .aggregate(total_discount=Sum('discount'))
                por = pure['total_pure_rate'] - dis['total_discount']
                return render(request, 'dret.html', {'po':por,'total_pure_rate': pure['total_pure_rate'],'ket':pers,'total_discount':dis['total_discount']})
        except:
            gfh = Dealer.objects.all()
            pure = Dealer.objects.all().aggregate(total_pure_rate=Sum('pure_rate'))
            dis = Dealer.objects.all().aggregate(total_discount=Sum('discount'))
            por = pure['total_pure_rate'] - dis['total_discount']
            return render(request, 'dret.html', {'po':por,'total_pure_rate': pure['total_pure_rate'],'ket':gfh,'total_discount':dis['total_discount']})
    else:
        gfh = Dealer.objects.all()
        pure = Dealer.objects.all().aggregate(total_pure_rate=Sum('pure_rate'))
        dis = Dealer.objects.all().aggregate(total_discount=Sum('discount'))
        por = pure['total_pure_rate'] - dis['total_discount']
        return render(request, 'dret.html', {'po':por,'total_pure_rate': pure['total_pure_rate'],'ket':gfh,'total_discount':dis['total_discount']})




def delete_view(request, id):
    student = Dealer.objects.get(id=id)
    student.delete()
    messages.success(request,'Deleted Successfully')
    return redirect('/dailret/')
   

def de(request, id):
    student = Seldealer.objects.get(id=id)
    student.delete()
    messages.success(request,'Deleted Successfully')
    return redirect('/sel/')
        

def upda(request, id):
    student = Dealer.objects.get(id=id)
    formdd = Dealerform()
    if request.method== 'POST':
        formdd = Dealerform(request.POST)
        if formdd.is_valid():
           student.name = request.POST['name']
           student.store_name = request.POST['store_name']
           student.contact = request.POST['contact']
           student.product_name = request.POST['product_name']
           student.type_of_product = request.POST['type_of_product']
           student.created_at = request.POST['created_at']
           student.product_quality = request.POST['product_quality']
           student.precious_metal = request.POST['precious_metal']
           we = request.POST['percent']
           student.percent = request.POST['percent']
           zs = request.POST['pure_rate']
           print(zs)
           student.pure_rate = request.POST['pure_rate']
           student.discount = (int(zs)/100*int(we))
           student.save()
           messages.success(request,'Edit successfully saved')
        return redirect('/dailret/')
    return render(request, 'tlogforup.html',{'student': student})


def up(request, id):
    student = Seldealer.objects.get(id=id)
    formdd = seldealerforms()
    if request.method== 'POST':
        formdd = seldealerforms(request.POST)
        if formdd.is_valid():
           student.sname = request.POST['sname']
           student.sstore_name = request.POST['sstore_name']
           student.scommuni = request.POST['scommuni']
           student.sproduct_name = request.POST['sproduct_name']
           student.stype_of_product = request.POST['stype_of_product']
           student.save()
           messages.success(request,'Edit successfully saved')
        return redirect('/sel/')
    return render(request, 'selforup.html',{'student': student})


def LecturerSignUp(request):
    if request.method == "POST":
        email = request.POST['email']
        uname = request.POST['username']
        passs = request.POST['password1']
        form = LecturerAddForm(request.POST or None)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.user_type = 'lecturer'
            lecturer.save()
            messages.success(request,'your account was created successfully.')
            return redirect('/ghg/')
    else:
       form = LecturerAddForm()
    return render(request,'Student_signup.html',{'form':form})



def StudentSignUp(request):
    if request.method == "POST":
        email = request.POST['email']
        uname = request.POST['username']
        passs = request.POST['password1']

        form = StudentAddForm(request.POST or None)
        if form.is_valid():
            student = form.save(commit=False)
            student.user_type = 'student'
            student.save()
            messages.success(request,'your account was created successfully.')
            return redirect('/tlog/')
    else:
       form = StudentAddForm()
    return render(request,'Student_signup.html',{'form':form})

def slogm(request):
    gfg = Dealer.objects.all()
    return render(request,'slogm.html',{'ket':gfg})



x = datetime.datetime.now()

def SignInView(request):
    if request.method == "POST": 
        global username
        username = request.POST['username']
        request.session['username'] = username
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            if request.user.is_authenticated:
                if request.user.is_student:
                    c = x.strftime("%H")
                    if int(c)>=19:
                        tt = ("Good Night! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    elif int(c)>=16:
                        tt = ("Good evening! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    elif int(c)>=12:
                        tt = ("Good afternoon! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    else:
                        tt = ("Good morning! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    request.session.set_expiry(800)
                    print('hi')
                    return redirect ('/slog/')
                else:
                    fl = "***your username or password is wrong***"
                    return render(request, 'login_form_workers.html',{'jk':fl})
        else:
            fl = "***your username or password is wrong***"
            return render(request, 'login_form_workers.html',{'jk':fl})
    return render(request, 'login_form_workers.html')




def tsing(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            if request.user.is_authenticated:
                if request.user.is_lecturer:
                    c = x.strftime("%H")
                    if int(c)>=19:
                        tt = ("Good Night! ")
                        messages.success(request,'your account was login successfully ,'+tt +' '+username+'. ')

                    elif int(c)>=16:
                        tt = ("Good evening! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    elif int(c)>=12:
                        tt = ("Good afternoon! ")
                        messages.success(request,'your account was login successfully ,'+tt +' '+username+'. ')
                    else:
                        tt = ("Good morning! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    request.session.set_expiry(800)
                    return redirect ('/tlog/')
                else:
                    fl = "***your username or password is wrong***"
                    return render(request, 'login_form.html',{'jk':fl})

        else:
            fl = "***your username or password is wrong***"
            return render(request, 'login_form.html',{'jk':fl})
    return render(request, 'login_form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

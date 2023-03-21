from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import StudentAddForm,LecturerAddForm
import datetime
# Create your views here.
def home(request):
    return render(request,"home.html")
def slog(request):
    return render(request,"slog.html")
def tlog(request):
    return render(request,"tlog.html")


def reactapp(request):
    return render(request, 'index.html')    


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

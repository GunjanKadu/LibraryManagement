from django.shortcuts import render
from Library_App.forms import UserForm,UserProfileInfoForm

from django.db import connection
#login Logour function
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from Library_App.models import Book,Bookinstance
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from Library_App.filter import BookFilter1,BookFilter


def index(request):
    return render(request,'Library_App/Indexpage/index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username') # we use the .get('username') because we used the same in the html file login.html
        password = request.POST.get('password') # we use the .get('password') because we used the same in the html file login.html

        user = authenticate(username=username,password=password)#authentication happend automatically

        if user:
            if user.is_active:
                login(request,user) #just simply login the user if authenticated succesfully
                return HttpResponseRedirect(reverse('special')) #Redirect to home page or profile page
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            #return render(request,'Library_App/Login_Page/invalid.html')
            print("Someone Tried To Login And Failed")
            print("Username:{} and Password {} ".format(username,password))
            return render(request,'Library_App/Login_Page/invalid.html')
            #return HttpResponse("Invalid login Details Supplied!")
    else:
        return render(request,'Library_App/Login_Page/login.html',{})

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST) #same variable as we declared in the html file
        profile_form = UserProfileInfoForm(data=request.POST)#same variable as we declared in the html file

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)   #Use to hash the passowrd so that admin cannot see it
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'Library_App/Signup_Page/signup.html',
                                {'user_form':user_form,
                                'profile_form':profile_form,
                                'registered':registered})

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'Library_App/UserPage/index.html', args)


def search_book(request):
    #booklist = Book.objects.all() and Bookinstance.objects.all()
    booklist = Book.objects.all()
    booksearch = BookFilter1(request.GET, queryset=booklist)
    return render(request, 'Library_App/UserPage/search.html',{'booksearch':booksearch})

def view_book(request):
    book= None

    with connection.cursor() as cursor:
        cursor.execute('SELECT b.name, a.f_name ,a.l_name, g.gen, b.edition,l.lang, bi.status FROM Library_App_book b JOIN Library_App_bookinstance bi ON (b.id=bi.book_id) JOIN Library_App_author a ON (a.id=b.author_id) JOIN Library_App_genre g ON (g.id=b.genre_id) JOIN Library_App_language l ON (l.id=bi.language_id);')
        book = cursor.fetchall()
    context = {
    'book' : book,
    }
    return render(request, 'Library_App/UserPage/book.html',context)


def profileoverview(request):
    return render(request,'Library_App/UserPage/profile.html')

def bookoverview(request):
    return render(request,'Library_App/UserPage/book.html')

def contactpage(request):
    return render(request,'Library_App/UserPage/contact.html')

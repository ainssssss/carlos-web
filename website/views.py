from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.conf import settings
import os
from django.http import FileResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import RegisterForm,LoginForm,BooksForm
from django.contrib.auth.models import User
from .models import Book
from datetime import datetime

def index_view(request):
    context = {
            "books" : Book.objects.all(),
    }
    return render(request,'website/index.html',context=context)

def book_id_view(request,book_id):
    if request.method == 'POST':        
        if not request.user.is_authenticated:
            context = {
                  'form' : LoginForm(),
                  'error' : "You have to login for use this funcion"
            }
            return render(request,'website/login.html',context)
        form = BooksForm(request.POST)
        if form.is_valid():    
            Bookname_POST_VALUE = form.cleaned_data["bookname"]
            Context_POST_VALUE  = form.cleaned_data["context"] 
            Editorial_POST_VALUE = form.cleaned_data["editorial"]
            Paginas_POST_VALUE  = form.cleaned_data["paginas"]
            Picture_POST_VALUE = form.cleaned_data["picture"]  
            Active_Book = Book.objects.get(id=book_id)

            Active_Book.BookName = Bookname_POST_VALUE
            Active_Book.Context = Context_POST_VALUE
            Active_Book.Editorial = Editorial_POST_VALUE
            Active_Book.Paginas = Paginas_POST_VALUE
            Active_Book.Picture = Picture_POST_VALUE
            Active_Book.save()

            return redirect('website:login')
  
        else:
            context = { 
                "form" : BooksForm(),
                "error" : "Algo ha fallado al enviar el formulario"
                         }   
            return render(request,'website/changebook.html',context=context)
    else:
        if request.user.is_authenticated:
            book = Book.objects.get(id=book_id) 
            
            initial_values = {
            'bookname': book.BookName,
            'context': book.Context,
            'editorial': book.Editorial,
            'paginas': book.Paginas,
            'picture': book.Picture,
            }
            BookFormWithValues = BooksForm(instance=book, initial=initial_values)

            context = {
                  "form" : BookFormWithValues,
            }
            return render(request,'website/changebook.html',context=context)
        else:
            context = {
                    'form' : LoginForm(),
                    'error' : "You have to login for use this funcion"
            }
            return render(request,'website/login.html',context)

def addbook_view(request):
    if request.method == 'POST':        
        if not request.user.is_authenticated:
            context = {
                'form' : LoginForm(),
                'error' : "You have to login for use this funcion"
                }
            return render(request,'website/login.html',context)
        form = BooksForm(request.POST)
        if form.is_valid():    
            Bookname_POST_VALUE = form.cleaned_data["bookname"]  
            Context_POST_VALUE  = form.cleaned_data["context"] 
            Editorial_POST_VALUE = form.cleaned_data["editorial"]  
            Paginas_POST_VALUE  = form.cleaned_data["paginas"] 
            Picture_POST_VALUE = form.cleaned_data["picture"]  
            Author_value = User.objects.get(id=request.user.id)
            Book.objects.create(Author=Author_value,
                                BookName=Bookname_POST_VALUE,
                                Context=Context_POST_VALUE,
                                Editorial=Editorial_POST_VALUE,
                                Paginas=Paginas_POST_VALUE,
                                Picture=Picture_POST_VALUE,
                                Date=datetime.now()) 
            return redirect('website:addbook') 
    
        else:
            context = { 
              "form" : BooksForm(),
              "error" : "Algo ha fallado al enviar el formulario"
                       }   
            return render(request,'website/addbook.html',context=context)
    else:
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            context = {
                "form" : BooksForm(),
            }
            return render(request,'website/addbook.html',context=context)
        else:
            return redirect('website:login') 
def login_view(request):       
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            Username_POST_VALUE = form.cleaned_data["username"]
            Password_POST_VALUE  = form.cleaned_data["password"] 
            
            user = authenticate(username=Username_POST_VALUE, password=Password_POST_VALUE)

            if user is not None:
                login(request,user)
                return redirect('website:index') 
            else:
                context = {
                    'form' : LoginForm(),
                    'error' : "User or Password Incorrect"
                }
                return render(request,'website/login.html',context)
        

        else:
          context = { 
              'form' : LoginForm(),
            }     
          return render(request,'website/login.html',context=context)  
    
    else:
        logout(request)        
        context = {
            'form' : LoginForm(),
        }
        
        return render(request,'website/login.html',context=context)             

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            Username_POST_VALUE = form.cleaned_data["username"]
            Password_POST_VALUE  = form.cleaned_data["password"]
            RePassword_POST_VALUE = form.cleaned_data["repassword"]
            
            valid_register = True
            error_message = ""
            if Password_POST_VALUE != RePassword_POST_VALUE:
                valid_register = False
                error_message = "Las contraseñas no coinciden"

            if len(Password_POST_VALUE) < 4:
                valid_register = False
                error_message = "La contraseña es demasiada corta"

            if len(Username_POST_VALUE) < 4:
                valid_register = False
                error_message = "La usuario es demasiado corta"

            if valid_register == True:
                user = User(
                first_name=Username_POST_VALUE,
                username=Username_POST_VALUE,
                )
                user.set_password(Password_POST_VALUE)
                user.save()
                return redirect('website:login')
            else:
                context = {
                    'form' : RegisterForm(),
                    'error' : error_message,
                }
                return render(request,'website/register.html',context=context) 
        else:
            context = {
                'form' : RegisterForm(),
                'error' : "Ha habido un error al validar los campos",
            }
            return render(request,'website/register.html',context=context) 

    context = {
        'form' : RegisterForm(),
    }
    return render(request,'website/register.html',context=context)

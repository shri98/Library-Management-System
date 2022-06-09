from lab_manage_app.forms import LoginForm, SignupForm, Addbook, Deletebook, Updatebook
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Users, Books


def hello(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today": today})


def login(request):
    if request.method == "POST":
        login_user = LoginForm(request.POST)
        if login_user.is_valid():
            print(login_user.cleaned_data['username'])
            if login_user.validate_user():
                return render(request, "library.html", {'books': Books.objects.all()})
            else:
                return render(request, "login.html", {"message": "Login failed. Please try again."})
        else:
            return HttpResponse("Found invalid form")
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        signup_user = SignupForm(request.POST)
        print(request.POST)
        if signup_user.is_valid():
            new_user = Users()
            new_user.first_name = signup_user.cleaned_data['first_name']
            new_user.last_name = signup_user.cleaned_data['last_name']
            new_user.email = signup_user.cleaned_data['email']
            new_user.password = signup_user.cleaned_data['password']
            new_user.phone_number = signup_user.cleaned_data['phone_number']
            new_user.is_admin = True
            try:
                new_user.save()
            except:
                return render(request, "login.html", {"message": "Email already exits. Please try with different email."})
            return render(request, "login.html", {"message": "Signup successful. Please login."})
        else:
            return HttpResponse("Invalid Signup Form")

    return render(request, "signup.html")


def addbook(request):
    if request.method == 'POST':
        book = Addbook(request.POST)
        if book.is_valid():
            new_book = Books()

            new_book.title = book.cleaned_data['title']
            new_book.total_pages = book.cleaned_data['total_pages']
            new_book.rating = book.cleaned_data['rating']
            new_book.isbn = book.cleaned_data['isbn']
            new_book.author_name = book.cleaned_data['author_name']
            new_book.publication = book.cleaned_data['publication']
            new_book.price = book.cleaned_data['price']

            new_book.save()
            return render(request, "library.html", {"message": "Book Added Successfully", 'books': Books.objects.all()})
        else:
            return render(request, "Addbook.html", {"message": "Unable to add, Please try again"})
    return render(request, "Addbook.html")



def viewbook(request, book_id):
    print(book_id)
    book = Books.objects.get(book_id=book_id)
    print(book.book_id, book.title)
    try:
        return render(request, 'viewbooks.html', {'book_id': book.book_id, 'title': book.title, 'total_pages': book.total_pages, 'rating': book.rating, 'isbn': book.isbn, 'author_name': book.author_name, 'publication': book.publication, 'price': book.price })
    except:
        return render(request, 'viewbooks.html', {'books': "No Books Found"})


def deletebook(request, book_id):
    delete_book = Deletebook(request.POST)
    # print(request.POST['book_name'])
    db_book = Books.objects.get(book_id=book_id)
    db_book.delete()
    return render(request, "library.html", {"message": "Book Deleted Successfully", 'books': Books.objects.all()})



def updatebook(request,book_id):
    if request.method == 'POST':
        book = Updatebook(request.POST)
        if book.is_valid():
            new_book = Books.objects.get(book_id=book_id)

            new_book.title = book.cleaned_data['title']
            new_book.total_pages = book.cleaned_data['total_pages']
            new_book.rating = book.cleaned_data['rating']
            new_book.isbn = book.cleaned_data['isbn']
            new_book.author_name = book.cleaned_data['author_name']
            new_book.publication = book.cleaned_data['publication']
            new_book.price = book.cleaned_data['price']

            new_book.save()
            return render(request, "library.html", {"message": "Book Updated Successfully", 'books': Books.objects.all()})
        else:
            return render(request, "library.html", {"message": "Unable to update, Please try again",'books': Books.objects.all()})
    return render(request, "library.html", {'books': Books.objects.all()})

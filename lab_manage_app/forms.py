from django import forms
from lab_manage_app.models import Users


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def validate_user(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        print(username, password)
        dbuser = Users.objects.all().filter(email=username, password=password)
        if not dbuser:
            return False
        return True


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=100)


class Addbook(forms.Form):
    # book_id = forms.AutoField()
    title = forms.CharField(max_length=100)
    total_pages = forms.CharField(max_length=100)
    rating = forms.CharField(max_length=100)
    isbn = forms.CharField(max_length=100)
    author_name = forms.CharField(max_length=100)
    publication = forms.CharField(max_length=100)
    price = forms.CharField(max_length=100)


class Updatebook(forms.Form):
    title = forms.CharField(max_length=100)
    total_pages = forms.CharField(max_length=100)
    rating = forms.CharField(max_length=100)
    isbn = forms.CharField(max_length=100)
    author_name = forms.CharField(max_length=100)
    publication = forms.CharField(max_length=100)
    price = forms.CharField(max_length=100)


class Deletebook(forms.Form):
    book_name = forms.CharField(max_length=100)






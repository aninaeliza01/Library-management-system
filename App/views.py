from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import CustomUser
from django.http import HttpResponse
from django.db import models
from django.shortcuts import *
from .models import *

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)

                if user.is_user:
                    request.session["username"] = user.username
                    return redirect(reverse('user_home')) 
                elif user.is_superuser:
                    request.session["username"] = user.username
                    return redirect(reverse('admin_home')) 
              
            else:
               
                messages.error(request, "Invalid credentials.")
                return redirect(reverse('login'))
        else:
           
            messages.error(request, "Please provide both username and password.")
            return redirect(reverse('login'))
    
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


def admin_home(request):
    return render(request, 'admin_home.html')


def maintenance(request):
    return render(request, 'maintenanace.html')


def reports(request):
    return render(request, 'reports.html')

def transactions(request):
    return render(request, 'transactions.html')


def user_home(request):
    return render(request, 'user_home.html')

def check_book_availability(request):
    return render(request, 'check_book_availability.html')


def issue_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        issue_date = request.POST.get('issue_date')
        return_date = request.POST.get('return_date')
        remarks = request.POST.get('remarks')
        
        messages.success(request, 'Book issued successfully!')
        
        return redirect('success_page') 
    return render(request, 'issue_book.html')


def return_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        serial_no = request.POST.get('serial_no')
        issue_date = request.POST.get('issue_date')
        return_date = request.POST.get('return_date')
        remarks = request.POST.get('remarks')
        return HttpResponse("Book returned successfully.") 
    else:
        return render(request, 'return_book.html')

def pay_fine(request):
    if request.method == 'POST':
        pass
    return render(request, 'pay_fine.html')

def master_list_books(request):
    return render(request, 'master_list_books.html')

def master_list_movies(request):
    return render(request, 'master_list_movies.html')

def master_list_memberships(request):
    return render(request, 'master_list_memberships.html')

def active_issues(request):
   
    return render(request, 'active_issues.html')

def overdue_returns(request):
   
    return render(request, 'overdue_returns.html')

def pending_issue_requests(request):
    
    return render(request, 'pending_issue_requests.html')

from django.shortcuts import render



def membership(request):
    return render(request, 'membership.html')

def books_movies(request):
    return render(request, 'books_movies.html')

def user_management(request):
    return render(request, 'user_management.html')


def add_membership(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_name = request.POST['contact_name']
        contact_address = request.POST['contact_address']
        aadhar_card_no = request.POST['aadhar_card_no']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        membership_type = request.POST['membership_type']
        
       
        membership = Membership(
            first_name=first_name,
            last_name=last_name,
            contact_name=contact_name,
            contact_address=contact_address,
            aadhar_card_no=aadhar_card_no,
            start_date=start_date,
            end_date=end_date,
            membership_type=membership_type
        )
        membership.save()
        
        
    
    return render(request, 'add_membership.html')



def add_book_movie(request):
    if request.method == 'POST':
        type = request.POST.get('type')  
        name = request.POST.get('name')
        procurement_date = request.POST.get('procurement_date')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        cost = request.POST.get('cost')
        
        try:
            if type == 'book':
                author = request.POST.get('author')
                category = request.POST.get('category')
                Book.objects.create(
                    name=name,
                    author=author,
                    category=category,
                    status=status,
                    cost=cost,
                    procurement_date=procurement_date,
                    quantity=quantity
                )
            elif type == 'movie':
                director = request.POST.get('director')
                genre = request.POST.get('genre')
                Movie.objects.create(
                    name=name,
                    director=director,
                    genre=genre,
                    status=status,
                    cost=cost,
                    procurement_date=procurement_date,
                    quantity=quantity
                )
            return redirect('add_book_movie')  
        except Exception as e:
            return HttpResponse('Error: ' + str(e)) 
    else:
        return render(request, 'add_book_movie.html')

def register(request):
    error = None
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            error = "Passwords don't match"
        elif CustomUser.objects.filter(username=username).exists():
            error = "Username already exists"
        elif CustomUser.objects.filter(email=email).exists():
            error = "Email already exists"
        else:
            user = CustomUser.objects.create_user(username=username, email=email, password=password1)
            user.first_name = first_name
            user.last_name = last_name
            user.is_user = True
            user.user_type = 'USER'
            user.save()
            
    return render(request, 'register.html', {'error': error})


def view_users(request):
    users = CustomUser.objects.all()
    return render(request, 'view_users.html', {'users': users})

def update_membership(request):
    if request.method == 'POST':
        membership_number = request.POST.get('membership_number')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        membership_extn = request.POST.get('membership_extn')
        membership_remove = request.POST.get('membership_remove')
        
        try:
            membership = get_object_or_404(Membership, pk=membership_number)
        except Membership.DoesNotExist:
            return HttpResponse('Membership does not exist')

        if membership_remove:
           
            membership.delete()
            return HttpResponse('Membership deleted successfully')

        membership.start_date = start_date
        membership.end_date = end_date
        
        
        if membership_extn:
            if membership_extn == 'six_months':
                membership.membership_type = 'Six Months'
            elif membership_extn == 'one_year':
                membership.membership_type = 'One Year'
            elif membership_extn == 'two_years':
                membership.membership_type = 'Two Years'
        
        membership.save()
        
        return HttpResponse('Membership updated successfully') 
    else:
        return render(request, 'update_membership.html')
    


def update_book_movie(request):
    book_list = Book.objects.all()
    movie_list = Movie.objects.all()
    
    book_movie_list = list(book_list) + list(movie_list)
    
    if request.method == 'POST':
        type = request.POST.get('type')
        name = request.POST.get('name')
        serial_no = request.POST.get('serial_no')
        status = request.POST.get('status')
        date = request.POST.get('date')
        
        if type == 'Book':
            try:
                book = Book.objects.get(name=name)
                
                book.serial_no = serial_no
                book.status = status
                book.procurement_date = date
                book.save()
                return HttpResponse('Book updated successfully')
            except Book.DoesNotExist:
                return HttpResponse('Book does not exist')
        elif type == 'Movie':
            try:
                movie = Movie.objects.get(name=name)
                
                movie.serial_no = serial_no
                movie.status = status
                movie.procurement_date = date
                movie.save()
                return HttpResponse('Movie updated successfully')
            except Movie.DoesNotExist:
                return HttpResponse('Movie does not exist')
        else:
            return HttpResponse('Invalid type')
    else:
        return render(request, 'update_book_movie.html', {'book_movie_list': book_movie_list})
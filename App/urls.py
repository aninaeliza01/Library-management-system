from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_user, name='login'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('reports/', views.reports, name='reports'),
    path('transactions/', views.transactions, name='transactions'),
    path('userhome/', views.user_home, name='user_home'),
    path('check-book/', views.check_book_availability, name='check_book'),
    path('issue-book/', views.issue_book, name='issue_book'),
    path('return-book/', views.return_book, name='return_book'),
    path('pay-fine/', views.pay_fine, name='pay_fine'),
    path('master-list-books/', views.master_list_books, name='master_list_books'),
    path('master-list-movies/', views.master_list_movies, name='master_list_movies'),
    path('master-list-memberships/', views.master_list_memberships, name='master_list_memberships'),
    path('active-issues/', views.active_issues, name='active_issues'),
    path('overdue-returns/', views.overdue_returns, name='overdue_returns'),
    path('pending-issue-requests/', views.pending_issue_requests, name='pending_issue_requests'),
    
    path('membership/', views.membership, name='membership'),
    path('books-movies/', views.books_movies, name='books_movies'),
    path('user-management/', views.user_management, name='user_management'),

    path('add-membership/', views.add_membership, name='add_membership'),
    path('add-book-movie/', views.add_book_movie, name='add_book_movie'),
    path('register/', views.register, name='register'),
    path('view_users/', views.view_users, name='view_users'),

    path('update_membership/', views.update_membership, name='update_membership'),
    path('update_book_movie/', views.update_book_movie, name='update_book_movie'),
    # path('search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

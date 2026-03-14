from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:pk>/borrow/', views.borrow_book, name='borrow_book'),
    path('return/<int:pk>/', views.return_book, name='return_book'),
    path('profile/', views.profile, name='profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # Author CRUD
    path('manage/authors/', views.author_list, name='author_list'),
    path('manage/authors/create/', views.author_create, name='author_create'),
    path('manage/authors/<int:pk>/update/', views.author_update, name='author_update'),
    path('manage/authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
    # Category CRUD
    path('manage/categories/', views.category_list, name='category_list'),
    path('manage/categories/create/', views.category_create, name='category_create'),
    path('manage/categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('manage/categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    # Book CRUD
    path('manage/books/', views.book_admin_list, name='book_admin_list'),
    path('manage/books/create/', views.book_create, name='book_create'),
    path('manage/books/<int:pk>/update/', views.book_update, name='book_update'),
    path('manage/books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    # BorrowRecord CRUD
    path('manage/borrow-records/', views.borrow_record_list, name='borrow_record_list'),
    path('manage/borrow-records/create/', views.borrow_record_create, name='borrow_record_create'),
    path('manage/borrow-records/<int:pk>/update/', views.borrow_record_update, name='borrow_record_update'),
    path('manage/borrow-records/<int:pk>/delete/', views.borrow_record_delete, name='borrow_record_delete'),

    # Incoming borrow requests (admin)
    path('manage/borrow-requests/', views.incoming_borrow_requests, name='incoming_borrow_requests'),
    path('manage/borrow-requests/<int:pk>/approve/', views.approve_borrow_request, name='approve_borrow_request'),
    path('manage/borrow-requests/<int:pk>/reject/', views.reject_borrow_request, name='reject_borrow_request'),
]

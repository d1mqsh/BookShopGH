from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns




app_name = 'store'

urlpatterns = [
	path('', views.index, name = "index"),
	path('login', views.signin, name="signin"),
	path('logout', views.signout, name="signout"),
	path('registration', views.registration, name="registration"),
	path('book/<int:id>', views.get_book, name="book"),
	path('books', views.get_books, name="books"),
	path('category/<int:id>', views.get_book_category, name="category"),
	path('writer/<int:id>', views.get_writer, name = "writer"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserRUD.as_view()),
    path('bookdetail/', views.BookDetail.as_view(), name='book_list'),
    path('portusers/', views.receive_message, name='receive_message'),
    
    
    


    

]

urlpatterns = format_suffix_patterns(urlpatterns)


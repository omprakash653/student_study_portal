from django.urls import path
from .views import home,books,notes,note_detail,delete_note,homework,delete_homework,todo,create_todo,delete_todo,dictionary_view,conversion,wikipedia_view,youtube_view,contact_us
urlpatterns = [
    path('', home, name='home'),
    path("books", books, name="books"),
    path('notes', notes, name='notes'),
    path('notes-detail/<int:pk>', note_detail, name='notedetail'),
    path('notes-delete/<int:pk>', delete_note, name='notedelete'),
    path('homework/', homework, name='homework'),
    path('homework/delete/<int:homework_id>/', delete_homework, name='delete_homework'),
    path('todo', todo, name='todo'),
    path('create-todo', create_todo, name='create-todo'),
    path('delete-todo/<int:todo_id>', delete_todo, name='delete-todo'),
    path("dict", dictionary_view, name="dictionary"),
    path('conversation', conversion, name='conversation'),
    path("wiki", wikipedia_view, name="wikipedia"),
    path('youtube-search', youtube_view, name='youtube-search'),
    path("contact/", contact_us, name="contactus"),
    
#     
]
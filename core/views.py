from django.shortcuts import render,redirect
import requests# A Python library used to make HTTP requests, in this case, to the Google Books API.
from .models import Notes,Homework
# Create your views here.
#1home#######################################################################################################
def home(request):
    return render(request, 'home.html')#request: Represents the incoming HTTP request from the user.

#2books######################################################################################################
def books(request):
    if request.method == 'GET' and 'book_name' in request.GET:
        book_name = request.GET['book_name']
        results = search_books(book_name)
    else:
        results = []  

    context = {
        'results': results,
    }
    return render(request, 'books.html', context)


############## when we will search for books
def search_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=10"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])

        results = []
        for item in items:
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', 'Unknown Title')
            subtitle = volume_info.get('subtitle', '')
            description = volume_info.get('description', 'No description available.')
            thumbnail = volume_info.get('imageLinks', {}).get('thumbnail', '')
            categories = volume_info.get('categories', [])
            pageCount = volume_info.get('pageCount', '')
            averageRating = volume_info.get('averageRating', '')

            book_data = {
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'thumbnail': thumbnail,
                'categories': categories,
                'pageCount': pageCount,
                'averageRating': averageRating,
                'preview': volume_info.get('previewLink', ''),
            }
            results.append(book_data)
        
        return results
    else:
        return [] 
    

#3notes####################################################################################################
def notes(request):
    notes = Notes.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Notes.objects.create(title=title, description=description)
            return redirect('notes') 

    context = {
        'notes': notes,
    }
    return render(request, 'notes.html', context)

##################
def note_detail(request, pk):
    note = Notes.objects.get(pk=pk)
    context ={
        "note":note
    }

    return render(request, 'notes-details.html', context)

#############
def delete_note(request, pk):
    note = Notes.objects.get(pk=pk)
    note.delete()
    return redirect('notes')


#4Homework#####################################################################################################
def homework(request):
    homeworks = Homework.objects.all()
    context = {
        'homeworks': homeworks
    }

    if request.method == 'POST':
        subject = request.POST.get('subject')
        title = request.POST.get('title')
        description = request.POST.get('description')
        due = request.POST.get('due')
        is_finished = request.POST.get('is_finished', False)
        
        homework = Homework.objects.create(
            subject=subject,
            title=title,
            description=description,
            due=due,
            is_finished=is_finished
        )
        return redirect('homework')

    return render(request, 'homework.html', context)

#############
def delete_homework(request, homework_id):
    homework = Homework.objects.get(id=homework_id)
    homework.delete()
    return redirect('homework')
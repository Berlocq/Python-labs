from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from book.models import Author

def author_list(request):
    author = Author.objects.all()
    context = {'author': author}
    return render(request, template_name='home.html', context=context)

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    context = {'object': author}
    return render(request, template_name='detail.html', context=context)

def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    message = f'Author { author.name } has been delete!!'
    genres = author.genres.all().delete()
    author.delete()
    context = {"message": message}
    context = {'object': author}
    return render(request, template_name='delete.html', context=context)

# def author_create(request):
#     context = {}
#     return render(request, template_name='create.html', context=context)


# def home_page(request):
#     return render
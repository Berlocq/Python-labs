from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from book.models import Author

def home_page(request):
    author = Author.objects.last()
    return HttpResponse(f"The last author is {author.name} with pk = {author.pk}")

# def home_page(request):
#     return render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView,ListView, DeleteView, CreateView, UpdateView

from . import forms
# Create your views here.
from book.models import Author, Genre, Series, Izdatel

def author_list(request):
    author = Author.objects.all()
    context = {'author': author, 'page_title': 'Autor'}
    return render(request, template_name='home.html', context=context)

class AuthorList(PermissionRequiredMixin, ListView):
    model=Author
    login_url = '/s-admin/login/'
    permission_required = 'book.add_author'

    def get_context_date(self, **kwargs):
        context = super().get_context_date(**kwargs)
        context['page_title'] = 'Autor'
        return context


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    context = {'object': author}
    return render(request, template_name='detail.html', context=context)

class AuthorDetail(DetailView):
    model=Author


def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    message = f'Author { author.name } has been delete!!'
    genres = author.genres.all().delete()
    author.delete()
    context = {"message": message}
    context = {'object': author}
    return render(request, template_name='delete.html', context=context)


class AuthorDelete(DeleteView):
    success_url=reverse_lazy('author-list')
    model=Author

class AuthorCreate(CreateView):
    model=Author
    fields=('name', 'book_name')
    success_url=reverse_lazy('author-list')


def author_create(request):
    context = {}
    if request.method == "POST":
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return HttpResponseRedirect(reverse('author-detail', kwargs={'pk':author.pk}))
        else:
            context['form'] = form
    else:
         context['form'] = forms.AuthorForm()       
    return render(request, template_name='create.html', context=context)

def author_update(request, pk):
    if request.method == "GET":
        author = Author.objects.get(pk=pk)
        context = {'author': author}
    elif request.method == "POST":
        name = request.POST.get('name')
        book_name = request.POST.get('book_name')
        # author = Author.objects.create(name=name, book_name=book_name)
        author = Author.objects.get(pk=pk)
        author.name=name 
        author.book_name=book_name
        author.save()
        return HttpResponseRedirect(reverse('author-detail', kwargs={'pk':author.pk}))
    #context = {}
    return render(request, template_name='update.html', context=context)
# def home_page(request):
#     return render

class AuthorUpdate(UpdateView):
    success_url=reverse_lazy('author-list')
    model=Author
    fields = ['name', 'book_name']




    # Genre views

class GenreList(PermissionRequiredMixin, ListView):
    model=Genre
    login_url = '/s-admin/login/'
    permission_required = 'book.add_genre'

class GenreDetail(DetailView):
    model=Genre


class GenreDelete(DeleteView):
    success_url=reverse_lazy('genre-list')
    model=Genre


class GenreCreate(CreateView):
    model=Genre
    fields=('author', 'style', 'description')
    success_url=reverse_lazy('genre-list')


class GenreUpdate(UpdateView):
    success_url=reverse_lazy('genre-list')
    model=Genre
    fields = ['author', 'style', 'description']    

class SeriesList(PermissionRequiredMixin, ListView):
    model=Series
    login_url = '/s-admin/login/'
    permission_required = 'book.add_series'

class SeriesDetail(DetailView):
    model=Series


class SeriesDelete(DeleteView):
    success_url=reverse_lazy('series-list')
    model=Series


class SeriesCreate(CreateView):
    model=Series
    fields=('author', 'number')
    success_url=reverse_lazy('series-list')


class SeriesUpdate(UpdateView):
    success_url=reverse_lazy('series-list')
    model=Series
    fields = ['author', 'number'] 



class IzdatelList(PermissionRequiredMixin, ListView):
    model=Izdatel
    login_url = '/s-admin/login/'
    permission_required = 'book.add_izdatel'

class IzdatelDetail(DetailView):
    model=Izdatel


class IzdatelDelete(DeleteView):
    success_url=reverse_lazy('izdatel-list')
    model=Izdatel


class IzdatelCreate(CreateView):
    model=Izdatel
    fields=('author', 'izdatel_name')
    success_url=reverse_lazy('izdatel-list')


class IzdatelUpdate(UpdateView):
    success_url=reverse_lazy('izdatel-list')
    model=Izdatel
    fields = ['author', 'izdatel_name'] 
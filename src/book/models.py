from django.db import models

# Create your models here.
class Author(models.Model): 
    name = models.CharField(
        verbose_name='Author name',
        max_length=50,) 
    book_name = models.CharField(
        verbose_name='Book name',
        max_length=50,
        blank=True)

    def __str__(self):
        return f'{self.name} {self.book_name}'    
          
class Genre(models.Model): 
    author = models.ForeignKey(
        'Author',
        verbose_name='Author',
        on_delete=models.PROTECT,
        related_name="genres",
        blank=True,
        )    
    style = models.CharField(
        verbose_name='style book',
        max_length=50,
        blank=True)
    description = models.TextField(
        verbose_name='book description',
        max_length=100,
        blank=True)      


    
    def __str__(self):
        return f'{self.author.name} {self.author.book_name} {self.style} {self.description}'

class Series(models.Model):
    author = models.ForeignKey(
        'Author',
        verbose_name='Author',
        on_delete=models.PROTECT,
        related_name="series",
        blank=True,
        )     
    number = models.CharField(
        verbose_name='Series number',
        max_length=50,) 
    

    def __str__(self):
        return f'{self.author.name} {self.author.book_name} {self.number}' 



        #return f' {self.style} {self.description}'
class Izdatel(models.Model):
    author = models.ForeignKey(
        'Author',
        verbose_name='Author',
        on_delete=models.PROTECT,
        related_name="izdatel",
        blank=True,
        )     
    izdatel_name = models.CharField(
        verbose_name='Name of Izdatel',
        max_length=50,) 
    

    def __str__(self):
        return f'{self.author.name} {self.author.book_name} {self.izdatel_name}'    
        
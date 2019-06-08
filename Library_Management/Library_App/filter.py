from django.contrib.auth.models import User
from Library_App.models import Book,Bookinstance
import django_filters


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Bookinstance
        fields = ['language']

class BookFilter1(BookFilter):
    class Meta:
        model = Book
        fields = ['__all__']

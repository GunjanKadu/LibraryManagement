from django.contrib import admin
from Library_App.models import UserProfileInfo
from Library_App.models import Genre
from Library_App.models import Language
from Library_App.models import Purchase_Type
from Library_App.models import Author
from Library_App.models import Publisher
from Library_App.models import Fine
from Library_App.models import Book
from Library_App.models import Bookinstance
from Library_App.models import Transaction_Detail
from Library_App.models import Borrow_Detail
#from Library_App.models import Condition
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Purchase_Type)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Fine)
admin.site.register(Book)
admin.site.register(Bookinstance)
admin.site.register(Transaction_Detail)
admin.site.register(Borrow_Detail)
#admin.site.register(Condition)


admin.site.site_header = 'WELCOME TO LIBRARY ADMINISTRATOR'
admin.site.site_title = 'Library Administration'

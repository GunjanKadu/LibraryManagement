from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from django.db.models.signals import post_save
# Create your models here.

class UserProfileInfo(models.Model):
#building a one to one releationship with users and
#linking them with the additional attributes created by us
#we dont direclty inherit therefore use the one to one releationship
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING,)


    #additional attributes
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    #return something
    def __str__(self):
        return self.user.username


#def create_profile(sender, **kwargs):
    #if kwargs['created']:
        #user_profile = UserProfileInfo.objects.create(user=kwargs['instance'])

#post_save.connect(create_profile, sender=User)


#class Condition(models.Model):
    #type =  models.CharField(max_length = 30, help_text = "Enter a book Condition(e.g New,Old,Cannot Be used)")
    #def __str__(self):
        #return self.type

class Genre(models.Model):
    gen = models.CharField(max_length = 100, help_text = "Enter a book Genre(e.g Science,Fiction,Non-Fiction)")
    def __str__(self):
        return self.gen

class Language(models.Model):
    lang = models.CharField(max_length = 100, help_text = "Enter a book Language")
    def __str__(self):
        return self.lang

class Purchase_Type(models.Model):
    type = models.CharField(max_length = 100, help_text = "Enter Whether Loan or Purchase")
    def __str__(self):
        return self.type

class Author(models.Model):
    f_name = models.CharField(max_length = 20)
    l_name = models.CharField(max_length = 20)
    def __str__(self):
        return self.f_name

class Publisher(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        return self.name

class Fine(models.Model):
    fine = models.IntegerField()
    def __str__(self):
        return self.fine


class Book(models.Model):
    author = models.ForeignKey('Author',on_delete=models.CASCADE,max_length = 30)
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE,max_length = 30)
    genre  = models.ForeignKey('Genre',help_text = "Enter a book Genre(e.g Science,Fiction,Non-Fiction)",on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    edition = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Bookinstance(models.Model):

    book = models.ForeignKey('Book',on_delete=models.CASCADE,max_length = 30)
    #condition = models.ForeignKey('Condition',on_delete=models.CASCADE,default='Status Not Available')
    language = models.ForeignKey('Language',on_delete=models.CASCADE,max_length = 30)
    purchase_type =  models.ForeignKey('Purchase_Type',on_delete=models.CASCADE,max_length = 30)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text = "Unique Id for the book for the entire library")
    status = models.CharField(max_length = 30)
    date_added = models.DateField(default=timezone.now)
    date_modified = models.DateField(default=timezone.now)

    def __str__(self):
        return self.book.name

class Transaction_Detail(models.Model):
    book_instance_id = models.ForeignKey('Bookinstance',on_delete=models.CASCADE,max_length = 30)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,max_length = 30)
    borrow_id = models.ForeignKey('Borrow_Detail',on_delete=models.CASCADE,max_length = 30)
    fine = models.ForeignKey('Fine',on_delete=models.CASCADE)
    due_date = models.DateField(default=timezone.now)
    return_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.book_instance_id

class Borrow_Detail(models.Model):
    book_instance_id = models.ForeignKey('Bookinstance',on_delete=models.CASCADE,max_length = 30)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,max_length = 30)
    fine = models.ForeignKey('Fine',on_delete=models.CASCADE)
    flag_lock = models.IntegerField()
    def __str__(self):
        return self.flag_lock

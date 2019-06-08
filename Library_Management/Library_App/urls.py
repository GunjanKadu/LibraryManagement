from django.conf.urls import url
from Library_App import views

#Template urls

app_name = 'libapp'

urlpatterns=[
url(r'^$',views.index,name='index'),
url(r'^register/$',views.register,name='register'),
url(r'^user_login/$',views.login_page,name='user_login'),
url(r'^profile/$',views.profileoverview,name='profile'),
url(r'^contact/$',views.contactpage,name='contact'),
url(r'^overview/$',views.view_profile,name='special'),
url(r'^books/$',views.view_book,name='viewbook'),
url(r'^search/$',views.search_book,name='search'),

]

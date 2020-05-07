from django.urls import path 
from first_app import views




app_name = 'first_app'

urlpatterns =[

       path('', views.index, name= 'index'),
       path('users/', views.users, name ='users'),
       path('formpage/', views.form_name_view, name= 'formpage'),
       path('register/', views.register, name= 'register'),
       path('userss/', views.user_s, name= 'user_s'),
       path('user_login/', views.user_login, name='user_login'),
      
       
          
          

]



# urlpatterns=[
   
#     url(r'^$', views.index, name='index'),

#     url(r'^topics/$', views.topics, name ='topics'),

#     url(r'^topics/(?P<topic_id>\d+)/$', views.topic , name='topic'),

#     url(r'^java/$', views.java, name ='java_test'),



# ]
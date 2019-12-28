from django.urls import path
from comment import views

urlpatterns = [
    #/http://localhost/comment
    path('update_comment',views.update_comment,name='update_comment'),

]

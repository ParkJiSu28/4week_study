from .import views
from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns =[
    path('example/',views.ExmodelListAPIView.as_view()),
    path('example/<int:pk>',views.ExmodelDetailAPIView.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)
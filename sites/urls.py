from django.urls import path
from .views import helloworldfunc, BlogList, BlogList2

urlpatterns = [
    path('helloworldapp/', helloworldfunc),
    path('list/', BlogList.as_view()),
    path('list2/', BlogList2.as_view()),
]

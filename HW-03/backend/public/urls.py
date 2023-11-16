from django.urls import path
from .views import *

urlpatterns = [
    path("", submitDataList.as_view(), name="transition-list"),
    path("create/", submitDataCreate.as_view()),
    path("submitData/", submitDataListUser.as_view()),
    path("submitData/<int:pk>/", submitDataUpdate.as_view()),
    path("delete-transition/<int:pk>/", UserPerevalDelete.as_view()),
    path("submitData/<slug:slug>/", submitDataDetail.as_view(), name="transition-detail"),

]
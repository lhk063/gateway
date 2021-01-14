from django.urls import path
from blog import views

# 2021-01-08
# from .views import MainView, SignIn, Comment

# 2021-01-11
from django.urls import path, include
from . import views as account_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("post/create", views.PostCreate.as_view(), name="post_create"),


    # # 2021-01-11
    # path('account/signup/', views.SignupView.as_view(), name='signup'),
    # path('account/signup/done/', views.SignupDoneView.as_view(), name='signup_done'),
    # path('account/login/', auth_views.LoginView.as_view(template_name='account/login.html.j2'), name='login'),
    # path('accounts/', include('django.contrib.auth.urls')),

    # 2021-01-08
    # path("comment/", Comment.as_view()),
    # path('signin/', SignIn.as_view()),
    # path('', MainView.as_view()),
]




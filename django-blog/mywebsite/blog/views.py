from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls.resolvers import URLPattern
from blog.models import Category, Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

# 2021-01-08
# import json
# from django.views import View
# from django.http import JsonResponse
# from blog.models import Users, Comment_Data

# #2021-01-11
# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from django.views.generic import TemplateView
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy


# Don't touch
# Create your views here.
# ========================================
def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest": post_latest
    }

    return render(req, "index.html", context=context)

class PostDetailView(generic.DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "title_image", "content", "category"]
# =========================================


# 2021-01-11

# class SignupView(CreateView):
#     template_name = 'account/signup.html.j2'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('signup_done')


# class SignupDoneView(TemplateView):
#     template_name = 'account/signup_done.html.j2'

# 2021-01-08

# class Comment(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         Comment_Data(
#             name_co = data['name_co'],
#             text_co = data['text_co']
#         ).save()
#         Co = Comment_Data.objects.values()
#         return JsonResponse({'commnet':list(Co)}, status = 200)

#         def get(self, request):
#             Co = Comment_Data.objects.values()
#             return JsonResponse({'comment':list(Co)}, status = 200)

# class MainView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         Users(
#             name = data['name'],
#             email = data['email'],
#             password = data['password']
#         ).save()

#         return JsonResponse({'message':'SUCCESS'}, status=200)

#     def get(self, request):
#         user_data = Users.objects.values()
#         return JsonResponse({'users':list(user_data)}, status=200)

# class SignIn(View):
#    def post(self, request):
#         data = json.loads(request.body)
#         try:
#             if Users.objects.filter(email = data['email']).exists():
#                 user = Users.objects.get(email = data['email'])
#             else:
#                 return JsonResponse({'message':'get wrong'}, status = 401)

#             if user.password == data['password']:
#                 return JsonResponse({'message':'SUCCESS'}, status=200)
#             return JsonResponse({'message':'get wrong'}, status = 401)
#         except KeyError:
#             return JsonResponse({'message':'key wrong'}, status=400)

from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls.resolvers import URLPattern
from blog.models import Category, Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

# 2021-01-08
from django.urls import path
from .views import MainView, SignIn, Comment

# Create your views here.
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

# 2021-01-08
import json
from django.views import View
from django.http import JsonResponse
from .models import Users, Comment_Data

class Commnet(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment_Data(
            name_co = data['name_co'],
            text_co = data['text_co']
        ).save()
        Co = Comment_Data.objects.values()
        return JsonResponse({'commnet':list(Co)}, status = 200)

        def get(self, request):
            Co = Comment_Data.objects.values()
            return JsonResponse({'comment':list(Co)}, status = 200)
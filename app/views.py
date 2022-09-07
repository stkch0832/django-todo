from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'app/index.html', context= {
            'post_data': post_data,
        })


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', context= {
            'post_data': post_data,
        })


class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        form = PostModelForm(request.POST or None)

        return render(request, 'app/post_form.html', context = {
            'form': form,
            })

    def post(self, request, *args, **kwargs):
        form = (request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.user = request.user
            post_data.title = form.cleaned_data['title']
            post_data.status = form.cleaned_data['status']
            post_data.priority = form.cleaned_data['priority']
            post_data.limit_datetime = form.cleaned_data['limit_datetime']
            post_data.description = form.cleaned_data['description']

            post_data.save()
            return redirect('post_detail', post_data.id)

        return render(request, 'app/post_form.html', context = {
            'form': form,
        })

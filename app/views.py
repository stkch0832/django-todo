from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')

        paginator = Paginator(post_data, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'app/index.html', context= {
            # 'post_data': post_data,
            'page_obj': page_obj,
        })


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', context= {
            'post_data': post_data,
        })


class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostModelForm(request.POST or None)

        return render(request, 'app/post_form.html', context = {
            'form': form,
            })

    def post(self, request, *args, **kwargs):
        form = PostModelForm(request.POST or None)

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


class PostEditView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostModelForm(
            request.POST or None,
            initial={
                'title': post_data.title,
                'status': post_data.status,
                'priority': post_data.priority,
                'limit_datetime': post_data.limit_datetime,
                'description': post_data.description,
            }
        )

        return render(request, 'app/post_form.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = PostModelForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            post_data.status = form.cleaned_data['status']
            post_data.priority = form.cleaned_data['priority']
            post_data.limit_datetime = form.cleaned_data['limit_datetime']
            post_data.description = form.cleaned_data['description']
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/post_form.hrml', context={
            'form': form,
        })


class PostDeleteView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', context= {
            'post_data': post_data,
        })

    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')

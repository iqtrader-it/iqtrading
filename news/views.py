from django.shortcuts import render, redirect
from .forms import PostForm, PostForm2
from .models import Post
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .parser import get_html, get_link_head, get_link_content
from django.http import JsonResponse


def catalog(request):
    data = dict()
    data['title'] = 'List of News'
    all_posts = Post.objects.order_by('-id')
    data['posts'] = all_posts

    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'news/catalog.html', context=data)


def show(request, post_id):
    data = dict()
    data['title'] = 'Full view'
    data['post'] = Post.objects.get(id=post_id)
    return render(request, 'news/show.html', context=data)


def add(request):
    data = dict()
    data['parser_heads'] = get_link_head(get_html('https://www.finanz.ru/novosti'))
    data['title'] = 'New topic'
    # data['content'] = get_link_content(get_html(url))
    if request.method == 'GET':
        if request.user.username == 'admin' or 'superuser_iqtrading' or 'iadmin':
            data['form'] = PostForm(data=data)
            return render(request, 'news/add.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_in')
    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/news')


def add_ajax(request):
    response = dict()
    link = request.GET.get('link')
    response['content'] = get_link_content(get_html(link))
    return JsonResponse(response)


def delete(request, post_id):
    data = dict()
    data['title'] = 'Remove new'
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        if request.user.username == 'admin':
            data['post'] = post
            return render(request, 'news/delete.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method =='POST':
        post.delete()
        return redirect('/news')
    

def update(request, post_id):
    data = dict()
    data['title'] = 'New`s topic'
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        if request.user.username == 'admin':
            data['form'] = PostForm2(instance=post)
            data['post'] = post
            return render(request, 'news/update.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        form2 = PostForm2(request.POST)
        if form2.is_valid():
            post.topic = form2.cleaned_data['topic']
            post.about = form2.cleaned_data['about']
            post.content = form2.cleaned_data['content']
            post.source = form2.cleaned_data['source']
            post.save()
        return redirect('/news')
            
def parser(request):
    pass

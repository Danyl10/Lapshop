import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Laptop, Category, Comment, Post


# Create your views here.

def home(request):
    all_laptops = Laptop.objects.all()
    return render(request, 'pages/home.html', {
        'active_page': 'home',
        'laptops': all_laptops,
    })


from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['laptop']
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['laptop']


from django.core.paginator import Paginator


def laptops(request):
    category_id = request.GET.get('category_id')
    to_price = request.GET.get('to_price')
    query_to_db = {}
    if category_id:
        query_to_db['category'] = int(category_id)
    if to_price:
        query_to_db['price__lte'] = int(to_price)

    all_laptops = Laptop.objects.all()
    if query_to_db:
        filtered_laptops = Laptop.objects.filter(**query_to_db)
    else:
        filtered_laptops = all_laptops
    categories_id = []
    for laptop in all_laptops:
        categories_id.append(laptop.category_id)
    all_laptops_categories = Category.objects.filter(id__in=categories_id)
    return render(request, 'pages/laptop.html', {
        "all_laptops": filtered_laptops,
        'all_laptops_categories': all_laptops_categories,
        'search': query_to_db,
    })


def laptop_detail(request, laptop_id):
    laptop = Laptop.objects.get(id=laptop_id)
    comments = Comment.objects.filter(laptop=laptop_id).order_by('-publish_date')
    return render(request, 'pages/laptop_detail.html', {
        'laptop': laptop,
        'comments': comments,
        'comment_form': CommentForm()
    })

def post(request):
    all_post = Post.objects.all()
    if request.method == 'POST':
        new_post = Post(
            author=request.POST.get('author'),
            text=request.POST.get('text'),
            rate=request.POST.get('rate')
        )
        new_post.save()
    return render(request, 'post.html', {
        'all_posts': all_post,
        'post_form': PostForm()})




def add_comment(request):
    if request.method == 'POST':
        laptop_id = request.POST.get('laptop_id')
        new_comment = Comment(
            laptop_id=int(laptop_id),
            author=request.POST.get('author'),
            text=request.POST.get('text'),
            rate=request.POST.get('rate')
        )
        new_comment.save()

        return redirect('/laptop-detail/{}'.format(laptop_id))


def mail(request):
    from django.core.mail import send_mail
    email = 'dahspill@gmail.com'
    send_mail(
        'Subject here',
        'Here is the message.',
        email,
        [email],
    )
    return HttpResponse('Send email is OK!')

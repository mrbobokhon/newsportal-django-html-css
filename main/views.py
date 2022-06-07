import datetime
from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Category
from .forms import PostForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Carousel


# Create your views here.

def main_index(request):
    return render(request, 'main/index.html', {
        "carousel": Carousel.objects.all(),
        "last_posts": Post.objects.order_by("-id").all()[:4],
        "top_like": Post.objects.order_by("-like")[:4],
        "top_dislike": Post.objects.order_by("-dislike")[:4],
        "top_read": Post.objects.order_by("-read")[:4],
    })


def main_cat(request, pk):

    category = Category.objects.get(id=pk)
    request.page_title = category.name

    request.breadcrumb = [
        [category.name]
    ]

    post_list = Post.objects.filter(category_id=pk).all()

    paginator = Paginator(post_list.order_by('-id'), per_page=4)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, "main/cat.html", context={
        "object_list": page.object_list,
        "page_obj": page,
        "category": category,
        "now": "{: %H:%M:%S }".format(datetime.datetime.now()),
        "time": format(date.today())
    })


def main_about(request):
    request.page_title = _("Biz haqimizda")
    request.breadcrumb = [
        [request.page_title, "index"],
        ["Nimadir", "about"]

    ]
    return render(request, "main/about.html", {
    })


@login_required
def main_add_post(request):
    request.page_title = _("Maqola qo'shish")
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

            messages.success(request, _("Maqola muvaffqiyatli qo'shildi"))

            return redirect('main:index')

    return render(request, 'main/add-post.html', {
        'form': form,
    })


@login_required
def main_delete_post(request, pk):
    Post.objects.filter(id=pk).delete()

    messages.success(request, _("Maqola Muvaffqiyatli o'chirldi"))
    return redirect('main:index')


def main_view_post(request, pk):
    post = Post.objects.get(id=pk)
    post.read += 1
    post.save()

    request.page_title = post.subject_ru

    request.breadcrumb = [
        [request.page_title]
    ]
    return render(request, 'main/view.html', {
        'post': post,
        'page_title': post.subject
    })


@login_required
def main_edit_post(request, pk):
    # if not request.user.is_authenticated:

    #     return redirect('account:login')

    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()

            messages.success(request, _("Maqola muvaffqiyatli tahrirlandi"))

            return redirect('main:index')

    request.page_title = _("Maqolani tahrirlash")
    return render(request, 'main/edit-post.html', {
        'form': form,
        'post': post,
    })


def main_like(request, type, id):
    post = Post.objects.get(id=id)
    if type == 'like':
        post.like += 1
    elif type == 'dislike':
        post.dislike += 1

    post.save()

    return redirect('main:index')


# def main_news(request):
#     return render(request, "main/news.html", {
#     })
#
#
# def main_shop(request):
#     return render(request, "main/shop.html", {
#     })
#
#
# def main_support(request):
#     return render(request, "main/support.html", {
#     })
#
#
# def main_reference(request):
#     return render(request, "main/reference.html", {
#     })
#
#
# def main_training(request):
#     return render(request, "main/training.html", {
#     })
#
#
# def main_price(request):
#     return render(request, "main/price.html", {
#     })

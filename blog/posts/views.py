from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.db.models import Q


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, 'Successfully created')# Esli forma sazdana poyavitsya eto soobshenie<!--https://docs.djangoproject.com/en/1.9/ref/contrib/messages/-->
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "blog/post_form.html", context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance,)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        messages.success(request, 'Successfully updated')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    return render(request, "blog/post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'Successfully deleted')
    return redirect("posts:list")


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }
    return render(request, "blog/post_detail.html", context)


def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active().filter(category="list").order_by("-timestamp")

    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all().filter(category="list").order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 2)# Show 10 posts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,

        "page_request_var": page_request_var,
        "today": today,

    }
    return render(request, 'blog/post_list.html', context)


def post_useful(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active().filter(category="useful").order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all().filter(category="useful").order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 10)  # Show 10 posts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,

        "page_request_var": page_request_var,
        "today": today,

    }
    return render(request, "blog/post_useful.html", context)


def post_events(request):

    today = timezone.now().date()
    queryset_list = Post.objects.active().filter(category="events").order_by("-timestamp")

    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all().filter(category="events").order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 10)  # Show 10 posts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,

        "page_request_var": page_request_var,
        "today": today,

    }
    return render(request, "blog/post_events.html", context )


def post_other(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active().filter(category="other").order_by("-timestamp")

    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all().filter(category="other").order_by("-timestamp")
    query = request.GET.get("q")# url
    if query:  # Ishet to chto vvodit polsovatel filtruet po title, content, name
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 10)  # Show 10 posts per page
    page_request_var = 'page'# url
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,

        "page_request_var": page_request_var,
        "today": today,

    }
    return render(request, "blog/post_other.html", context)


def post_about_us(request):

    return render(request, "blog/about.html")

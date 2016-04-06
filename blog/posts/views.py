from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.db.models import Q


def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    if not request.user.is_authenticated():
        return redirect("log_in")
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, 'Successfully created')
        return redirect(instance.get_absolute_url())
    else:
        context = {
            "form": form,
                }
        return render(request, "blog/post_form.html", context)


def post_update(request, slug=None):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    if not request.user.is_authenticated():
        return redirect("log_in")
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance,)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        messages.success(request, 'Successfully updated')
        return redirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    return render(request, "blog/post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_authenticated():
        return redirect("log_in")
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'Successfully deleted')
    return redirect("posts:list")


def post_detail(request, slug=None):
    if not request.user.is_authenticated():
        return redirect("log_in")
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


class PostView:
    @staticmethod
    def universal_view(html, cat, request):
        if not request.user.is_authenticated():
            return redirect("log_in")
        today = timezone.now().date()
        queryset_list = Post.objects.active().filter(category=cat).order_by("-timestamp")

        if request.user.is_staff or request.user.is_superuser:
            queryset_list = Post.objects.all().filter(category=cat).order_by("-timestamp")
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
            "title": "List",
            "page_request_var": page_request_var,
            "today": today,

        }
        return render(request, html, context)


def post_list(request):
    x = PostView()
    return x.universal_view('blog/post_list.html', 'list', request)


def post_useful(request):
    x = PostView()
    return x.universal_view('blog/post_useful.html', 'useful', request)


def post_events(request):
    x = PostView()
    return x.universal_view('blog/post_events.html', 'events', request)


def post_other(request):
    x = PostView()
    return x.universal_view('blog/post_other.html', 'other', request)






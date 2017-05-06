from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import RequestContext, loader
from cmsblog.models import Post
from cmsblog.forms import PostForm
import logging

logger = logging.getLogger('views')
# This isn't writing to log file


# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")


def list_view(request):
    """Display all posts"""
    logger.info('----- executing list_view -----')
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    # templates are rendered by passing in a context
    return render(request, 'list.html', context)
    # render() is a shortcut for render_to_response (uses RequestContext)


def detail_view(request, post_id):
    """Display a single post"""
    logger.info('----- executing detail_view -----')
    # TODO add delete functionality (here?)
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'detail.html', context)


def post_new(request):
    """Create new Post"""
    # TODO Display forms for Post and Category
    # If method is POST then construct the PostForm with data from the form
    # Else blank form (new)
    if request.method == "POST":
        logger.info('----- executing post_new POST -----')
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            published = Post.objects.exclude(published_date__exact=None)
            posts = published.order_by('-published_date')
            context = {'posts': posts}
            return render(request, 'list.html', context)
            # return redirect('detail.html', pk=post.pk)
    else:
        logger.info('----- executing post_new NOT POST -----')
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    """Edit Post"""
    # TODO Display forms for Post and Category
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        logger.info('----- executing post_edit POST -----')
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return render(request, 'blog_detail', context)
            # return redirect('blog_detail', pk=post.pk)
            context = {'post': post}
            return render(request, 'detail.html', context)

    else:
        logger.info('----- executing post_edit NOT POST -----')
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
    # return render(request, 'blog/post_edit.html', {'form': form})

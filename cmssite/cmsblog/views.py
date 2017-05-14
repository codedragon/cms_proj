from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import RequestContext, loader
from cmsblog.models import Post, Category
from cmsblog.forms import PostForm, CategoryForm
import logging


# create logger with module name
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
log_file_name = __name__ + '.log'
fh = logging.FileHandler(log_file_name)
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)


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
    """Display a single post
    by getting all posts then filtering by pk"""
    logger.info('----- executing detail_view -----')
    # TODO add delete functionality (here?)
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    logger.info('request: %s', request)  # s string required
    logger.info('post: %s', post)
    return render(request, 'detail.html', context)


def post_new(request):
    """Create new Post
    using form"""
    # TODO Display forms for Post and Category
    # If method is POST then construct the PostForm with data from the form
    # Else blank form (new)
    if request.method == "POST":
        # GET and POST are the only HTTP methods to use when dealing with forms
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
    else:
        logger.info('----- executing post_new NOT POST -----')
        form = PostForm()
        # model = Post; fields = ('title', 'text',)
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    """Edit Post
    GET = form
    POST = post"""
    # TODO Display forms for Post and Category
    post = get_object_or_404(Post, pk=pk)
    cats = post.categories.all()  # QuerySet
    # 'QuerySet' object has no attribute '_meta'
    logger.info('cats: %s', cats)
    if request.method == "POST":
        logger.info('----- executing post_edit POST -----')
        form = PostForm(request.POST, instance=post)
        cform = CategoryForm(request.POST, instance=cats)
        logger.info('cform type: %s', type(cform))
        logger.info('cform: %s', cform)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            context = {'post': post}
            return render(request, 'detail.html', context)
    else:
        logger.info('----- executing post_edit NOT POST -----')
        form = PostForm(instance=post)
    logger.info('request: %s', request)  # s string required
    logger.info('form: %s', form)
    return render(request, 'post_edit.html', {'form': form})

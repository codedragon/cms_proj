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
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    logger.info('request: %s', request)  # s string required
    logger.info('post: %s', post)  # returns name of post
    logger.info('type post: %s', type(post))
    return render(request, 'detail.html', context)


def post_new(request):
    """Create new Post
    using form"""
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
    # request: <WSGIRequest: POST '/post/14/edit/'>
    # pk (Primary Key):
    post = get_object_or_404(Post, pk=pk)
    # type(post) = <class 'cmsblog.models.Post'>
    cats = post.categories.all()
    cat = cats[0].clean()
    # type(cats) = <class 'django.db.models.query.QuerySet'>
    # type(cats[0]) = <class 'cmsblog.models.Category'>
    # cats[0].name is correct
    logger.info('request: %s', request)
    logger.info('pk: %s', pk)
    logger.info('type post: %s', type(post))
    logger.info('type cats: %s', type(cats))
    logger.info('type cats[0]: %s', type(cats[0]))
    logger.info('cats[0].name: %s', cats[0].name)
    if request.method == "POST":
        logger.info('----- executing post_edit POST -----')
        logger.info('POST: %s', request.POST)  # POST does not contain cat data
        form = PostForm(request.POST, instance=post)
        # form type: <class 'cmsblog.forms.PostForm'>
        # ...name="title" value="Time" maxlength="128" required id="id_title"..
        catform = CategoryForm(cat)
        # if catform.is_valid():
        #     logger.info('! catform is valid!')
        # else:
        #     logger.info('...catform is NOT valid...')
        # catform type: <class 'cmsblog.forms.CategoryForm'>
        # ...class="errorlist"><li>This field is required.</li>
        logger.info('form type: %s', type(form))
        logger.info('form: %s', form)
        logger.info('catform type: %s', type(catform))
        logger.info('catform: %s', catform)  # BAD DATA!!!
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            context = {'post': post}
            logger.info('context: %s', context)
            return render(request, 'detail.html', context)
        else:
            logger.info('form is not valid!')
    else:
        logger.info('----- executing post_edit NOT POST -----')
        form = PostForm(instance=post)
    logger.info('request: %s', request)  # s string required
    logger.info('form: %s', form)
    return render(request, 'post_edit.html', {'form': form})

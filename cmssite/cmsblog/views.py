from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import RequestContext, loader
from cmsblog.models import *
from cmsblog.forms import *
import logging
import datetime


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
    """Home page - Calendar"""
    logger.info('----- executing list_view -----')
    # RuntimeWarning: naive datetime while time zone support is active
    events = Event.objects.filter(event_start__gte=datetime.datetime.today()).order_by('event_start')
    current_event = events[0]
    next_event = events[1]
    context = {'current_event': current_event, 'next_event': next_event}
    return render(request, 'list.html', context)


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
    post = get_object_or_404(Post, pk=pk)
    logger.info('request: %s', request)
    logger.info('pk: %s', pk)
    logger.info('type post: %s', type(post))
    if request.method == "POST":
        logger.info('----- executing post_edit POST -----')
        logger.info('POST: %s', request.POST)  # POST does not contain cat data
        form = PostForm(request.POST, instance=post)
        logger.info('form type: %s', type(form))
        logger.info('form: %s', form)
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


def post_index(request):
    """Display all posts"""
    logger.info('----- executing post_index -----')
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'post_index.html', context)


def event_index(request):
    """Display all events"""
    logger.info('----- executing event_index -----')
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'event_index.html', context)


def event_detail(request, event_id):
    """Display a single event
    by getting all posts then filtering by pk"""
    logger.info('----- executing event_detail -----')
    events = Event.objects.all()
    try:
        event = events.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404
    context = {'event': event}
    return render(request, 'event_detail.html', context)


def event_edit(request, pk):
    """Edit Event
    GET = form
    POST = post"""
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        logger.info('----- executing event_edit POST -----')
        logger.info('POST: %s', request.POST)
        form = EventForm(request.POST, instance=event)
        logger.info('form type: %s', type(form))
        logger.info('form: %s', form)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context = {'event': event}
            logger.info('context: %s', context)
            return render(request, 'event_detail.html', context)
        else:
            logger.info('form is not valid!')
    else:
        logger.info('----- executing event_edit NOT POST -----')
        form = EventForm(instance=event)
    logger.info('request: %s', request)  # s string required
    logger.info('form: %s', form)
    return render(request, 'event_edit.html', {'form': form})


def talk_index(request):
    """Display all talks"""
    logger.info('----- executing talk_index -----')
    talks = Talk.objects.all()
    context = {'talks': talks}
    return render(request, 'talk_index.html', context)


def talk_detail(request, talk_id):
    """Display a single talk"""
    logger.info('----- executing talk_detail -----')
    talks = Talk.objects.all()
    try:
        talk = talks.get(pk=talk_id)
    except Talk.DoesNotExist:
        raise Http404
    context = {'talk': talk}
    return render(request, 'talk_detail.html', context)


def talk_edit(request, pk):
    """Edit Talk"""
    talk = get_object_or_404(Talk, pk=pk)
    if request.method == "POST":
        logger.info('----- executing talk_edit POST -----')
        logger.info('POST: %s', request.POST)
        form = TalkForm(request.POST, instance=talk)
        logger.info('form type: %s', type(form))
        logger.info('form: %s', form)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context = {'talk': talk}
            logger.info('context: %s', context)
            return render(request, 'talk_detail.html', context)
        else:
            logger.info('form is not valid!')
    else:
        logger.info('----- executing event_edit NOT POST -----')
        form = TalkForm(instance=talk)
    logger.info('request: %s', request)  # s string required
    logger.info('form: %s', form)
    return render(request, 'talk_edit.html', {'form': form})


def speaker_index(request):
    """Display all Speakers"""
    logger.info('----- executing speaker_index -----')
    speakers = Speaker.objects.all()
    context = {'speakers': speakers}
    return render(request, 'speaker_index.html', context)


def speaker_detail(request, speaker_id):
    """Display a single speaker and all of their talks"""
    logger.info('----- executing speaker_detail -----')
    speakers = Speaker.objects.all()
    try:
        speaker = speakers.get(pk=speaker_id)
    except Talk.DoesNotExist:
        raise Http404
    logger.info('speaker: %s', speaker)
    talks = Talk.objects.filter(speaker__name__icontains=speaker)
    context = {'speaker': speaker, 'talks': talks}
    return render(request, 'speaker_detail.html', context)


def speaker_edit(request, pk):
    """Edit Speaker"""
    speaker = get_object_or_404(Speaker, pk=pk)
    if request.method == "POST":
        logger.info('----- executing speaker_edit POST -----')
        logger.info('POST: %s', request.POST)
        form = SpeakerForm(request.POST, instance=speaker)
        logger.info('form type: %s', type(form))
        logger.info('form: %s', form)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context = {'speaker': speaker}
            logger.info('context: %s', context)
            return render(request, 'speaker_detail.html', context)
        else:
            logger.info('form is not valid!')
    else:
        logger.info('----- executing speaker_edit NOT POST -----')
        form = SpeakerForm(instance=speaker)
    logger.info('request: %s', request)  # s string required
    logger.info('form: %s', form)
    return render(request, 'speaker_edit.html', {'form': form})


def venue_index(request):
    """Display all venues"""
    logger.info('----- executing venue_index -----')
    venues = Venue.objects.all()
    context = {'venues': venues}
    return render(request, 'venue_index.html', context)


def venue_detail(request, venue_id):
    """Display a single venue and all of their talks"""
    logger.info('----- executing venue_detail -----')
    venues = Venue.objects.all()
    try:
        venue = venues.get(pk=venue_id)
    except Venue.DoesNotExist:
        raise Http404
    logger.info('venue: %s', venue)
    context = {'venue': venue}
    return render(request, 'venue_detail.html', context)


def venue_edit(request, pk):
    """Edit Venue"""
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == "POST":
        logger.info('----- executing venue_edit POST -----')
        logger.info('POST: %s', request.POST)
        form = VenueForm(request.POST, instance=venue)
        logger.info('form type: %s', type(form))
        logger.info('form: %s', form)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context = {'venue': venue}
            logger.info('context: %s', context)
            return render(request, 'venue_detail.html', context)
        else:
            logger.info('form is not valid!')
    else:
        logger.info('----- executing speaker_edit NOT POST -----')
        form = VenueForm(instance=venue)
    logger.info('request: %s', request)  # s string required
    logger.info('form: %s', form)
    return render(request, 'venue_edit.html', {'form': form})

"""Experiment and exploration"""


from cmsblog.models import *
from cmsblog.forms import *

def main():

    poa = Post.objects.all()

    for entry in poa:
        # print(entry.pk, entry.title)
        # Only with a specific entry object can we find many to many data
        c_count = 0
        cats = entry.categories.all()
        for cat in cats:
            print(entry.pk, entry)
            print('Category: %s %s' % (c_count, cat))
            catform = CategoryForm(cat)
            print(type(catform))


# colors = ['red', 'yellow', 'blue', 'green']
# for color in colors:
#     print('color: %s' % color)

from cmsblog.models import *
import datetime

events = Event.objects.all()
events = events.order_by('event_start')
current_events = []
for event in events:
    # fix for offset-naive
    t = event.event_start.replace(tzinfo=None)
    if t > datetime.datetime.today():
        current_events.append(event.pk)

current_event = Event.objects.get(pk=current_events[0])
next_event = Event.objects.get(pk=current_events[1])

for event in events:
    t = event.event_start.replace(tzinfo=None)
    event.event_start = t
    event.save()

events = Event.objects.exclude(event_start__gte=datetime.date.today())
events = events.order_by('event_start')

# TypeError: can't compare offset-naive and offset-aware datetimes

events = Event.objects.filter(event_start__gte=datetime.datetime.today()).order_by('event_start')
current_event = events[0]
next_event = events[1]


if __name__ == "__main__":

    main()



    {% for event in events %}
        <hr>
        <h1><a href="{% url 'event_detail' event.pk %}">{{ event }}</a></h1>
        <p>{{ event.event_start }} - {{ event.event_end|time }}</p>
        <p>{{ event.venue }}: {{ event.venue.address }}</p>
        <h2>The Talks</h2>
            {% for talk in event.talks.all %}
                <h3>{{ talk }}</h3>
                <p>{{ talk.speaker }}</p>
            {% endfor %}
    {% endfor %}

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



if __name__ == "__main__":

    main()

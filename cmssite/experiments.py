"""Experiment and exploration"""


from cmsblog.models import Post


def main():

    poa = Post.objects.all()

    for entry in poa:
        print(entry.pk, entry.title)
        # Only with a specific entry object can we find many to many data
        cats = entry.categories.all()
        for cat in cats:
            print('\t', cat)


if __name__ == "__main__":

    main()

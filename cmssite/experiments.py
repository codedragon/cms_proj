"""Experiment and exploration"""


from cmsblog.models import Post


def main():

    poa = Post.objects.all()

    for entry in poa:
        print(entry.pk, entry.title)


if __name__ == "__main__":

    main()

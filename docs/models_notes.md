#Models Notes

##Post
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

##Categorys (Categories)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True,
                                   related_name='categories')


##Speaker
    name
    contact (phone, email)
    bio

##Venue
    name
    address
    contact

##Event
    name
    date
    venue
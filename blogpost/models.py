from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True) #auto timestamp everytime created
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category' #renaming category in django admin
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    #post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL)
    tag = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True) #auto timestamp everytime created
    created = models.DateTimeField(auto_now_add=True) #only take the timestamp first created
    def __str__(self):
        return self.tag
    class Meta:
        verbose_name = 'Tag' #renaming category in django admin
        verbose_name_plural = '  Tags' #spacing allows to reorder models in django admin
    
class Post(models.Model):
    #tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.SET_NULL)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="medias/")
    title = models.CharField(max_length=200)
    #post = models.TextField(null=True, blank=True)
    post = HTMLField()
    category = models.ManyToManyField(Category,blank=True)
    tag = models.ManyToManyField(Tag,blank=True)

    STATUSES = [('Published','Published'),
                ('Pending','Pending'),
                ('Draft','Draft')]
    status = models.CharField(max_length=50,choices=STATUSES,default='Draft')
    #status = models.ForeignKey(PostStatus, blank=True, null=True, on_delete=models.SET_NULL)
    updated = models.DateTimeField(auto_now=True) #auto timestamp everytime created
    created = models.DateTimeField(auto_now_add=True) #only take the timestamp first created
    def __str__(self):
        return self.title #this will display in Django Admin

    def category_list(self):
        categories = self.category.all()
        return ",\n".join([p.category for p in categories])

    def tag_list(self):
        return ",\n".join([k.tag for k in self.tag.all()])

    class Meta:
        verbose_name = 'Post' #renaming category in django admin
        verbose_name_plural = '   Posts' #spacing allows to reorder models in django admin

class Comment(models.Model):
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    comment = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
class Setting(models.Model):
   site_title = models.CharField(max_length=100)
   site_slogan = models.TextField(null=True, blank=True)
   site_description = models.TextField(null=True, blank=True)
   site_footer = models.TextField(null=True, blank=True)
   def __str__(self):
       return self.site_title

class SocialMedia(models.Model):
    setting = models.ForeignKey(Setting, blank=True, null=True, on_delete=models.SET_NULL)
    social_media = models.CharField(max_length=500)
    def __str__(self):
        return self.social_media
"""
class PostStatus(models.Model):
    STATUSES = [('Pb','Published'),
                ('Pd','Pending'),
                ('Dr','Draft')]
    status = models.CharField(max_length=50,choices=STATUSES)
    def __str__(self):
        return self.status
"""

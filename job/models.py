from django.core.exceptions import DisallowedRedirect
from django.db import models
from django.db.models.fields import CharField
from PIL import Image
from django.utils.text import slugify

# Create your models here.


JOP_TYPE = (
    ('part time', 'part time'),
    ('full time', 'full time')
)


def image_upload(instance, filename):
    ''' this user defined function built to help us customise image or file name to be as we need  '''
    imgName, extension = filename.split(".")
    return "job/%s.%s" % (instance.id, extension)


class Jop(models.Model):
    title = models.CharField(max_length=100)
    # Location --> from library
    job_type = models.CharField(max_length=15, choices=JOP_TYPE)
    description = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=5000)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(max_length = 50 , blank=True , null=True)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Jop, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 70 or img.width > 70:
                output_size = (70, 70)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return self.title


class Category(models.Model):
    cat_name = CharField(max_length=25)

    def __str__(self):
        return self.cat_name




class ApplicantInfo(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length = 200) 
    cv = models.FileField(upload_to='applicants_cvs/')
    cover_letter = models.TextField()
    created_at = models.DateField(auto_now=True)
    jop = models.ForeignKey(Jop, on_delete=models.CASCADE)

    def __str__(self):
        return f' Aplicant Name is : {self.name} '
    
    
    
    
    
    
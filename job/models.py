from django.db import models

# Create your models here.


JOP_TYPE=(
    ('part time','part time'),
    ('full time','full time')
    )


class Jop(models.Model):
    title = models.CharField(max_length=100)
    # Location --> from library
    job_type=models.CharField(max_length=15 , choices=JOP_TYPE)
    description=models.TextField(max_length=500)
    published_at=models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=5000)
    experience =models.IntegerField(default=1)
    # category---as relationship

    def __str__(self):
        return self.title

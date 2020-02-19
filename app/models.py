from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(max_length=300, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    about_image = models.ImageField()

    def __str__(self):
        return self.title


class CoverImage(models.Model):
    image_desc = models.CharField(max_length=255)
    cover_image = models.ImageField()

    def __str__(self):
        self.image_desc


class Skills(models.Model):
    skill_title = models.CharField(max_length=100)
    skill_content = models.CharField(max_length=255)
    skill_image = models.ImageField()

    def __str__(self):
        return self.skill_title


class Education(models.Model):
    institue_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.institue_name



from django.shortcuts import render
from django.http import JsonResponse

from .models import ContactForm, About, CoverImage, Skills, Education

def main_page(request):
    cover_image = CoverImage.objects.all()[:1]
    about = About.objects.all()[:1]
    skill = Skills.objects.all()[:1]
    education = Education.objects.all()[:1]

    context = {
        'cover_image':cover_image,
        'about':about,
        'skill':skill,
        'education':education
    }
    return render(request, 'main.html', context)

def contact_form(request):
    pass


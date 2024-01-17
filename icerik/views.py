from django.shortcuts import render,get_object_or_404
from .models import Teacher, URL

def home(request):
    icerik = URL.objects.all()
    return render(request, 'home.html', {'icerik': icerik})

def icerik_index(request):
    kidsicerik = Teacher.objects.all()
    ogretmenicerik = URL.objects.all()
    return render(request, 'page/kids.html', {'kidsicerik': kidsicerik, 'ogretmenicerik': ogretmenicerik})

def icerik_index2(request):
    teachersicerik = Teacher.objects.all()
    ogretmenicerik = URL.objects.all()
    return render(request, 'page/teachers.html', {'teachersicerik': teachersicerik, 'ogretmenicerik': ogretmenicerik})



def icerik_icerik(request, icerikanabaslik):
    ticerik = get_object_or_404(Teacher, icerikanabaslik=icerikanabaslik)
    teachers = Teacher.objects.filter(zip_file__isnull=False, id=ticerik.id)
    custom_models = Teacher.objects.filter(custom_zip_file__isnull=False, id=ticerik.id)
    ticerik = teachers.first()

    image_data = [{'teacher': teacher, 'images': teacher.extract_images()} for teacher in teachers]
    custom_data = [{'custom_model': custom_model, 'custom_images': custom_model.extract_custom_images()} for custom_model in custom_models]

    if image_data and image_data[0]['images']:
        image_data[0]['images'] = sorted(image_data[0]['images'])

    # custom_data içindeki custom_images'ı sırala
    if custom_data and custom_data[0]['custom_images']:
        custom_data[0]['custom_images'] = sorted(custom_data[0]['custom_images'])

    context = {'image_data': image_data, 'custom_data': custom_data, 'ticerik': [ticerik]}
    
    return render(request, 'page/teachersicerik/teachersicerik.html', context)








def icerik_icerik2(request, icerikanabaslik):
    kicerik = get_object_or_404(Teacher, icerikanabaslik=icerikanabaslik)

    teachers = Teacher.objects.filter(zip_file__isnull=False, id=kicerik.id)
    custom_models = Teacher.objects.filter(custom_zip_file__isnull=False, id=kicerik.id)

    kicerik = teachers.first()

    image_data = [{'teacher': teacher, 'images': teacher.extract_images()} for teacher in teachers]
    custom_data = [{'custom_model': custom_model, 'custom_images': custom_model.extract_custom_images()} for custom_model in custom_models]

    if image_data and image_data[0]['images']:
        image_data[0]['images'] = sorted(image_data[0]['images'])

    # custom_data içindeki custom_images'ı sırala
    if custom_data and custom_data[0]['custom_images']:
        custom_data[0]['custom_images'] = sorted(custom_data[0]['custom_images'])

    context = {'image_data': image_data, 'custom_data': custom_data, 'kicerik': [kicerik]}

    return render(request, 'page/kidsicerik/kidsicerik.html', context)
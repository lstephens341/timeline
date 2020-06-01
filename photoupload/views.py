from django.views.generic.edit import FormView
from .forms import FileFieldForm, ImageInspect
from .models import Image
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings


def map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    images = Image.objects.all().exclude(yearField='').exclude(yearField='year')
    if images is not None:
        images0 = images[0]
    api_key = settings.G_API_KEY
    return render(request, 'photoupload/map.html',
                  { 'images': images, 'images0': images0, 'api_key': api_key})

def explore(request):
    if request.method == 'GET':
        images = Image.objects.all().exclude(yearField='').exclude(yearField='year')
        if images is not None:
            images0 = images[0]
        api_key = settings.G_API_KEY
        return render(request, 'photoupload/photo_upload.html', {'images': images, 'images0' : images0, 'api_key': api_key})

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'photoupload/upload.html'  # Replace with your template.
    success_url = 'photoupload/photo_upload.html'  # Replace with your URL or reverse().


    def post(self, request, *args, **kwargs):
        # images = Image.objects.all()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                instance = Image(image=f, yearField=form.cleaned_data['year'])  # match the model.
                instance.save()
            form = self.form_valid(form)
            return render(request, 'photoupload/photo_upload.html', {'form': form})
            # return self.form_valid(form)
        else:
            return self.form_invalid(form)


def login(request):
    if request.method == 'GET':
        return render(request,"photoupload/login.html")
    elif request.method == 'POST':
        return redirect('photoupload')

def inspect(request, key):
    if request.method == 'GET':
        images = Image.objects.all().exclude(yearField='').exclude(yearField='year')
        key_int = int(key)
        key_int_corrected = key_int - 1
        image = images[key_int_corrected]
        api_key = settings.G_API_KEY
        form = ImageInspect(initial={'caption': image.caption, 'memories': image.memories, 'tags':image.tags, 'location':image.location})
        return render(request, 'photoupload/inspect.html', {'image': image, 'form': form, 'api_key': api_key})
    if request.method == 'POST':
        images = Image.objects.all().exclude(yearField='').exclude(yearField='year')
        key_int = int(key)
        key_int_corrected = key_int - 1
        image = images[key_int_corrected]
        form = ImageInspect(request.POST, instance = image)
        if form.is_valid():
            form.save()
        return render(request, 'photoupload/photo_upload.html', {'images': images})

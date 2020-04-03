from django.views.generic.edit import FormView
from .forms import FileFieldForm, ImageInspect
from .models import Image
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def explore(request):
    if request.method == 'GET':
        images = Image.objects.all().exclude(yearField='').exclude(yearField='year')
        images0 = images[0]
        return render(request, 'photoupload/photo_upload.html', {'images': images, 'images0' : images0})

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
        form = ImageInspect(initial={'caption': image.caption, 'memories': image.memories, 'tags':image.tags})
        return render(request, 'photoupload/inspect.html', {'image': image, 'form': form})
    if request.method == 'POST':
        images = Image.objects.all().exclude(yearField='').exclude(yearField='year')
        key_int = int(key)
        key_int_corrected = key_int - 1
        image = images[key_int_corrected]
        form = ImageInspect(request.POST, instance = image)
        if form.is_valid():
            form.save()
        return render(request, 'photoupload/photo_upload.html', {'images': images})

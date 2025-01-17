from django.shortcuts import render, get_object_or_404, redirect
from core.forms import DogForm
from .models import Dog


# Create your views here.
def upload_form(request):
	if request.method == "POST":
		form = DogForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		else:
			context = {'form': form}
			return render(request, 'core/index.html', context=context)

	context = {'form': DogForm()}
	return render(request, 'core/index.html', context=context)


def list_dogs(request):
	dogs_data = Dog.objects.all()
	context = {'dogs': dogs_data}

	return render(request, "core/dogs.html", context=context)


def delete_dogs(request, pk):
	dog = get_object_or_404(Dog, pk=pk)
	dog.delete()

	return redirect('all-dogs')

from django.shortcuts import render
from core.forms import DogForm


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

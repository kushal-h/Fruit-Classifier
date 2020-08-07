from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def predict(request):
    if request.method == 'POST':
        try:

        except Exception as e:
            print('errir is', e )


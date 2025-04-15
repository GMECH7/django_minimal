from django.http import HttpResponse


# Create your views here.def home():
def home(request):
    return HttpResponse("Hello, world! This is an attempt to host my app on Linux.")

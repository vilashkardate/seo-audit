from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp/base.html')

def audit(request):
    return render(request,'myapp/audit.html')
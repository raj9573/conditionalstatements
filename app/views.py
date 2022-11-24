from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'conditionsonhtml.html',d)
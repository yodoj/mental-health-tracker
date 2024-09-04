from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165692',
        'name': 'Nadira Aliya Nashwa',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
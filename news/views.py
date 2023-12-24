from django.shortcuts import render

# Create your views here.
#News
def news(request):
    return render(request, 'News.html')

def news_ar(request):
    return render(request, 'ar/News.html')

#News_Details
def news_details(request,id):
    return render(request, 'News_Details.html')

def news_details_ar(request,id):
    return render(request, 'ar/News_Details.html')
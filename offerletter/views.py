from django.http import HttpResponse
from django.shortcuts import render


def offerLetterPage(request):
    offerletterdata = {
        'joining_data' : "today"
    }
    return render(request, "offerletter.html", offerletterdata)

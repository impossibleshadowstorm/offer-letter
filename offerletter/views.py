from django.http import HttpResponse
from django.shortcuts import render


def offerLetterPage(request):
    offerletterdata = {
        "company_name": "Microsoft Corporation",
        "company_logo": "/static/offerletter/img/ms-logo.svg",
        "address": {
            "street_city": "1 Orchard Rd, Armonk",
            "state_pin": "New York, 10504",
            "country": "United States Of America",
        },
        "offer_date": "08th September 2022",
        "candidate_name": "Mr. Sumit Saurav",
        "candidate_address": {
            "street_city": "1 Orchard Rd, Armonk",
            "state_pin": "New York, 10504",
            "country": "United States Of America",
        },
        "job_profile": "Senior Software Developer",
        "reporting_manager": "Chris Liddell",
        "joining_date": "May 1, 2006",
        "job_location": "Armonk",
        "probation_period": "six [06] months",
        "salary": {
            "basic_salary": {
                "salary_component": "Basic Salary",
                "percentage": "Nil",
                "amount": 13750,
            },
            "hra": {
                "salary_component": "HRA",
                "percentage": "Nil",
                "amount": 8750,
            },
            "special_allowance": {
                "salary_component": "Special Allowance",
                "percentage": "Nil",
                "amount": 13750,
            },
            "total": {
                "salary_component": "Total",
                "percentage": "Nil",
                "amount": 13750,
            },
        },
    }
    return render(request, "offerletter.html", offerletterdata)

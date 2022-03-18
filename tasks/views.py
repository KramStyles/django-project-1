from django.shortcuts import render
from django.http import HttpResponse


def january(request):
    return HttpResponse("<h2>This is a heading 2 from Python Django</h2>")


def february(request):
    return HttpResponse("<h2>February has 28 - 29 days depending on it's mood</h2>")


def monthly_tasks(request, month):
    months_and_tasks = {
        'mar': "Let us keep marching forward! That's what they told us",
        'apr': "It's first of April and i've decided to profess my love to her. Do you think she would take me serious",
        'may': "I may or may not marry you.. That's a reply to a proposal!",
        'jun': "A month of uncertainty, confusion and invalid personas",
        'jul': "A Cancerous month indeed",
        'aug': "We need to have a meeting. If you know you know",
        'sept': "Get me my scepter. I have a proclamation!",
        'oct': "And we thought we were free on 1st of 1960",
        'nov': "It's time to f**k some turkeys up!",
        'dec': "Peru, para. December coming."
    }
    return HttpResponse(f"<h2>{months_and_tasks[month]}</h2>")

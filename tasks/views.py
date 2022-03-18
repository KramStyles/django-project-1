from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

months_and_tasks = {
    'feb': "February has 28 - 29 days depending on it's mood",
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


def january(request):
    return HttpResponse("<h2>This is a heading 2 from Python Django</h2>")


def num_month(request, num_months):
    index = list(months_and_tasks.keys())[num_months - 1]
    # return monthly_tasks('', index)
    return HttpResponseRedirect(f'/{index}')


def monthly_tasks(request, month):
    try:
        jokes = months_and_tasks[month]
    except KeyError:
        return HttpResponseNotFound(f"<h1>Invalid url: {month} <br>Jokes on you!</h1>")
    return HttpResponse(f"<h2>{jokes}</h2>")

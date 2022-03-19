from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

months_and_tasks = {
    'jan': "The start of your year.. Guess what, The chinese think you wrong!!",
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


def home(request):
    links = ""
    for link in months_and_tasks.keys():
        links += f"<a href='/tasks/{link}' class='list-group-item list-group-item-action'>{link.upper()}</a>"
    arg = {'links': links}
    response = render(request, 'tasks/index.html', arg)
    return HttpResponse(response)


def january(request):
    return HttpResponse("<h2>This is a heading 2 from Python Django</h2>")


def num_month(request, num_months):
    if num_months <= len(months_and_tasks):
        num_months = list(months_and_tasks.keys())[num_months - 1]
        return HttpResponseRedirect(f'/tasks/{num_months}')
    return HttpResponseNotFound(f'<h1>Omoooo which month do you want us to find now.. Do we have up to {num_months} months</h1>')


def monthly_tasks(request, month):
    try:
        jokes = months_and_tasks[month]
    except KeyError:
        return HttpResponseNotFound(f"<h1>Invalid url: {month} <br>Jokes on you!</h1>")
    prev = list(months_and_tasks.keys()).index(month)
    nxt = list(months_and_tasks.keys()).index(month) + 2

    arg = {
        'content': jokes,
        'month': month,
        'prev': prev,
        'next': nxt if nxt < 12 else nxt % 12
    }
    return render(request, 'tasks/months.html', arg)

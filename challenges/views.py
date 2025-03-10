from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    'january': 'january challenge',
    'february': 'february challenge',
    'march': 'march challenge',
    'april': 'april challenge',
    'may': 'may challenge',
    'june': 'june challenge',
    'july': 'july challenge',
    'august': 'august challenge',
    'september': 'september challenge',
    'october': 'october challenge',
    'november': 'november challenge',
    'december': None,
}


def index(request):

    # response_data = ""
    # months = list(monthly_challenges)
    # for month in months:
    #     month_path = reverse('month-challenge', args=[month])
    #     response_data += f"<li><a href=\"{month_path}\">{month}</a></li>"
    # return HttpResponse(f'<ul>{response_data}</ul>')

    try: 
        return render(request,'challenges/index.html',{'months': list(monthly_challenges)})
    
    except:
        return HttpResponseNotFound(render_to_string('404.html'))

def monthly_challenge_by_number(request, month):
    try:
        return HttpResponseRedirect(reverse('month-challenge', args=[list(monthly_challenges)[month-1]]))

        # return HttpResponseRedirect('/challenges/' + list(monthly_challenges)[month-1])

        # return HttpResponse(list(monthly_challenges.values())[month-1])

    except:
        return HttpResponseNotFound(render_to_string('404.html'))


def monthly_challenge(request, month):

    try:
        monthly_challenge = monthly_challenges[month]
        return render(request,'challenges/challenge.html',{'text':monthly_challenge , 'month': month})
    except:
        raise Http404()



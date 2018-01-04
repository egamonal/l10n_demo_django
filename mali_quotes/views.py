from django.http import HttpResponse
from django.template import loader



def index(request):
    latest_quotes = [
        "It's just a job. Grass grows, birds fly, waves pound the sand. I beat people up.",
        "It isn't the mountains ahead to climb that wear you out; it's the pebble in your shoe.",
        "It's hard to be humble when you're as great as I am.",
        "A man who has no imagination has no wings.",
        "Impossible is just a big word thrown around by small men who find it easier to live in the world "
        "they've been given than to explore the power they have to change it. Impossible is not a fact. It's an opinion. Impossible is not a declaration. It's a dare. Impossible is potential. Impossible is temporary. Impossible is nothing.",
    ]

    template = loader.get_template('mali/index.html')
    context = {
        'latest_quotes': latest_quotes,
    }
    return HttpResponse(template.render(context, request))

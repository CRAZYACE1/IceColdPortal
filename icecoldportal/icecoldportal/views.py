from django.http import HttpRequest, HttpResponse


def welcomebrothers(request):
    return HttpResponse("This is the the landing page for the portal. If you see this, then your setup was successful "
                        "🤙🏾")

from django.shortcuts import render
from menumaker.models import Week


def main(request):
    weeks = Week.objects.all()
    context = {
        "weeks":weeks
    }
    return render(request,"menumaker/menumain.html", context)

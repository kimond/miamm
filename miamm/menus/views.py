from django.shortcuts import render
from menus.models import Week


def main(request):
    weeks = Week.objects.all()
    context = {
        "weeks":weeks
    }
    return render(request,"menus/menumain.html", context)

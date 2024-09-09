from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        number = request.POST.get("myNumber")
        answer = int(number) + 1
        context = {
            "myNumber": number,
            "myAnswer": answer,
        }
        return render(request, "index.html", context)
    else:
        "myNumber": "",
        "myAnswer": "",
    return(request, "index.html", context)
    
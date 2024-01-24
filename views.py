from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse("<b>Welcome</b>")

def coursedetails(request,courseid):
    return HttpResponse(courseid)

def calculator(request):
    c=''
    try:
        if request.method =="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
        
    except:
        c="Invalid"
    print(c)
    return render(request,"calculator.html",{'c':c})




def homepage(request):
    return render(request,"index.html")


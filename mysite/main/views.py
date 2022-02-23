from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from main.models import Contact, Skill, My_Skill
# Create your views here.
def home(request):
    data = Skill.objects.all()
    data1 = My_Skill.objects.all()
    return render(request, 'index.html', {"data1" :data1, 'data':data})
def main(request):
    return render(request,'main.html')
def sendMessage(request):
    if request.method == 'POST':
        send=Contact()
        send.name = request.POST.get("name")
        send.email = request.POST.get("email")
        send.message = request.POST.get("message")
        send.save()
        return HttpResponseRedirect('/')
# def sendMessage(re)
# def name(request):
#     if request.method == 'POST'
#     send = Person()
#     send.name = request.POST.get("name")
#     send.last_name = request.POST.get("last_name")
#     send.gender = request.POST.get("gender")
#     send.profession = request.POST.get("profession") 

    #     "h5_values":"My name is Nurbek and",
    #     "text": "lorem ipsup dolor sit amit" 
    # }
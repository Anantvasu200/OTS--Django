from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from OTS.models import *
from django.template import loader


# Create your views here.

def Welcome(request):
    templates=loader.get_template('Welcome.html')
    #res = render(request, 'Welcome.html') isko mein ese bhi render kr skta tha.
    return HttpResponse(templates.render())

def candidateRegistrationForm(request):
    res = render(request, 'registration_form.html')#isko mein ese bhi render kr skta tha.
    return res 

def candidateRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        #Check if the username already exists
        if (len(Candidate.objects.filter(username=username)) > 0):
            return HttpResponse("Username already exists. Please choose another username.")
        password = request.POST['password']
        name = request.POST['name']

        # Save the new candidate
        new_candidate = Candidate(username=username, password=password, name=name)
        new_candidate.save()

        return redirect('OTS:login')  # Redirect to login page after successful registration
    else:
        return render(request, 'registration_form.html')

def loginview(request):
    pass

def candidateHome(request):
    pass

def testPaper(request):
    pass

def calculateTestResult(request):
    pass

def testresultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutview(request):
    pass

def handleSubmit(request): # clint se request aa rhi hai or server se response ja rha hai.
    return render(request, 'signupresponse.html')# server se response ja rha hai.
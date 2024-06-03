from django.urls import path
from django.contrib import admin
from OTS.views import * # Import views from the current package
app_name = 'OTS'

urlpatterns = [
    path('', Welcome, name='welcome'),
    path('new-candidate', candidateRegistrationForm, name='registrationForm'),
    path('store-candidate', candidateRegistration, name='StoreCandidate'),
    path('login', loginview, name='login'),
    path('home', candidateHome, name='home'),
    path('test-paper', testPaper, name='testPaper'),
    path('calculate-result', calculateTestResult, name='calculateResult'),
    path('test-history', testresultHistory, name='testHistory'),
    path('result', showTestResult, name='showResult'),
    path('logout', logoutview, name='logout'),
    path('submit', handleSubmit, name='submit'),
]

from django.shortcuts import render
from .models import Patients, Patients_mood

import google.generativeai as genai
import os
# Create your views here.

def show_homepage(request):
    return render(request,'landing.html')

def show_accountpage(request):
    return render(request,'loginpage.html')

def tell_mood(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        age = request.POST['age']
        marital_status = request.POST['marital_status']
        user = request.user

        Patients.objects.create(name=name ,email = email, gender=gender,age=age,marital_status=marital_status,user=user)
     
    data = {
        'name': name,
        'email': email,
    }

    return render(request,'questions.html',data)

def instant_relief(request):
    
    if request.method == 'POST':
        mood = request.POST['mood']
        emotions = request.POST['emotions']
        feelings = request.POST['feelings']


        user = request.user

        Patient = Patients.objects.filter(user = user).last()
        name = Patient.name
        gender = Patient.gender
        age = Patient.age
        marital_status = Patient.marital_status

        Patients_mood.objects.create(mood = mood, emotions= emotions, user=request.user)
        os.environ["API_KEY"] = 'AIzaSyCRikYbzyNjEfdJArZ4tkP3MG7N94Chxu0'
        genai.configure(api_key=os.environ["API_KEY"])
        response = None
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(f'write a small paragraph giving affirmation to somebody having some kind of feeling described as {feelings} also whose name = {name} marital_status = {marital_status}, gender = {gender}')
        movies_response =  model.generate_content(f'give suggestion for movies to somebody having some kind of feeling described as {feelings} also whose name = {name}, age = {age}, marital_status = {marital_status}, gender = {gender}   . important note just give movies names seperated by | only and only 3 and nothing else in the answer')
        musics_response =  model.generate_content(f'give suggestion for music to somebody having some kind of feeling described as {feelings} also whose name = {name}, age = {age}, marital_status = {marital_status}, gender = {gender}   . important note just give music names seperated by | only and only 3 and nothing else in the answer')
        thoughts_response =  model.generate_content(f'give quotes of great peoples to read to somebody having some kind of feeling described as {feelings} also whose name = {name}, age = {age}, marital_status = {marital_status}, gender = {gender}   . important note just give quotes by great people  seperated by | .')


    
        movies = movies_response.text.split('|')
        musics = musics_response.text.split('|')
        thoughts = thoughts_response.text.split('|')
        

        
        context = {'response' : response.text,
                   'movies':  movies,
                   'musics': musics ,
                   'thoughts' : thoughts
                   }

        
        print(thoughts_response.text)
    return render(request,'instant_relief.html',context)




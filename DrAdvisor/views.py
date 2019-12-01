from django.shortcuts import render
from django.http import HttpResponse
import sys
import pandas as pd
from os import system, name

val1 = 0
age = 0
data=pd.read_csv("C:/Users/nikil/Desktop/DrAdvisor/html/health.csv")
datap=pd.read_csv("C:/Users/nikil/Desktop/DrAdvisor/html/prescriptions_15.csv")
datapp=pd.read_csv("C:/Users/nikil/Desktop/DrAdvisor/html/prescriptions_30.csv")
datappp=pd.read_csv("C:/Users/nikil/Desktop/DrAdvisor/html/prescriptions_60.csv")

def home(request):
    return render(request, 'home.html', {'name':'Welcome'})


def add(request):
    val1 = request.GET['sym']
    age = int(request.GET['age'])
    pos = 0
    flag = False
    for col in data.columns:
        if(val1 == col):
            pos = data.index[data[col] == 1]
            x = data[col] == 1
            flag = True
    if(flag == False):
        return render(request, 'home.html', {'name':'Wrong Symptom'})
    buffer = data.iloc[pos,-1]
    count = buffer.size
    if(count>=2):
        return render(request, 'home.html', {'name':'Enter other symptom'})
    else:
        pos = 0
        if(age <= 15):
            pos = datap.index[datap['id'] == int(buffer)]
            res = datap.iloc[pos,2]
            ress = datap.iloc[pos,3]
            resss = datap.iloc[pos,4]
            res1 = "Disease: " + res.to_string(index=False) + ress.to_string(index=False) + resss.to_string(index=False)
            return render(request, 'home.html', {'name':res1})
        elif(age <= 30):
            pos = datapp.index[datapp['id'] == int(buffer)]
            res = datapp.iloc[pos,2]
            ress = datapp.iloc[pos,3]
            resss = datapp.iloc[pos,4]
            res1 = "Disease: " + res.to_string(index=False) + ress.to_string(index=False)+ '\n' + resss.to_string(index=False)
            return render(request, 'home.html', {'name':res1})
        elif(age <= 60):
            pos= datappp.index[datappp['id'] == int(buffer)]
            res = datappp.iloc[pos,2]
            ress = datappp.iloc[pos,3]
            resss = datappp.iloc[pos,4]
            res1 = "Disease: " + res.to_string(index=False) + ress.to_string(index=False) + resss.to_string(index=False)
            return render(request, 'home.html', {'name':res1})
        else:
            res = "Invalid"
            ress = " Age"
            res1 = "Disease: " + res + ress
            return render(request, 'home.html', {'name':res1})


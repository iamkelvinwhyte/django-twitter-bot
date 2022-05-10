from ast import If
from re import search
import json
from django.shortcuts import render
import user.tweet  as tp
from user.forms import TwitterFrom



def home(request):
    file_name=""
    if request.method == "POST":

        TwForm= TwitterFrom(request.POST)
        search = request.POST['search']
        file_type=request.POST['doc_type']
        tweets=tp.SearchTweet(search,10)

        if(file_type=='csv'):
            file_name=tp.tweet2csv(tweets)
        elif(file_type=='json'):
            file_name= tp.tweet2json(tweets)
        elif(file_type=='text'):
            file_name=tp.tweet2txt(tweets)
      
    else:
         TwForm= TwitterFrom()
         tweets={}
     
    return render(request, 'user/home.html', {'file_name':file_name,'TwForm':TwForm,"json_string": tweets})




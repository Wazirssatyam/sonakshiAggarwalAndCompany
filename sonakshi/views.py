from django.shortcuts import render
from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


# Subscription Logic
def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
# "Email received. thank You! "
# Create your views here.
def index(request):
     if request.method == "POST":
        email = request.POST['email']
        print(email)
        subscribe(email)    
                        # function to access mailchimp
        messages.success(request, "Your Mail is Successfully Registered.! ") # message

    #  url="https://gstcouncil.gov.in/2022-gst-updates"
    #  response = requests.request("GET", url)
    #  soup=BeautifulSoup(response.content,"html.parser")
    #  targert=soup.find("table",class_="custum-tbl table table-bordered")
    #  # print(targert)
     result={}
    #  for  i in targert.find_all("a",target="_blank",href=True):
    #      result[i['href']]=i.decode_contents()
     return render(request,"index.html",{'data':result})
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")
def act(request):
    return render(request,"act.html")
def team(request):
    return render(request,"team.html")
def contact(request):
    return render(request,"contact.html")

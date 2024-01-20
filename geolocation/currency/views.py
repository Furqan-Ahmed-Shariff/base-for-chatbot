from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import os
import requests
import json

# Create your views here.
from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2

api_key = os.getenv("AbstractApi")


api_url = "https://ipgeolocation.abstractapi.com/v1/?api_key=" + api_key


def get_ip(request):
    # g = GeoIP2()
    remote_addr = request.META.get("HTTP_X_FORWARDED_FOR")
    if remote_addr:
        address = remote_addr.split(",")[-1].strip()
    else:
        address = request.META.get("REMOTE_ADDR")
    # country = g.country("103.2.232.250")
    country = get_ip_geolocation_data("103.2.232.250").decode()
    country = json.loads(country)
    long = country["longitude"]
    lat = country["latitude"]
    return HttpResponse(f"You are visiting from: {country['city']}")


def get_ip_geolocation_data(ip_address):
    response = requests.get(api_url + "&ip_address=" + ip_address)

    return response.content


def test(request):
    return render(request, "currency/index.html")

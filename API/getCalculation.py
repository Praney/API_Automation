import requests
import json
from jsonschema import validate
import jsonschema
import pytest
from nested_lookup import nested_lookup
from random import randint

def weather():
    a= randint(-100,100)
    b= randint(-100,100)
    print a
    print b
    url = "http://localhost:8080/math/add?a="+ str(a)+"&b=" + str(b)
    getResponse = requests.get(url=url)
    print getResponse
    response = getResponse.text
    print response
    data = getResponse.json()
    print data
    print a+b
    
weather()
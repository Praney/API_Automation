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
    
    # currentTemp = int(data['currently']['temperature'])
    
    # if case == 1:
        
    #     minTemp = nested_lookup('temperatureMin',data['daily']['data'])
    #     minTemp = minTemp[1:6]
    #     for i in range(len(minTemp)):
    #         minTemp[i] = str(int(minTemp[i]))
    #     return minTemp

    # elif case == 2:
    #     maxTemp = nested_lookup('temperatureMax',data['daily']['data'])
    #     maxTemp = maxTemp[1:6]
    #     for i in range(len(maxTemp)):
    #         maxTemp[i] = str(int(maxTemp[i]))

    #     return maxTemp

    # else :
    #     currentTemp = str(int(data['currently']['temperature']))
    #     return currentTemp
    
weather()
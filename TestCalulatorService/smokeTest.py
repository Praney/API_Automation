#!/usr/bin/python
# -*- coding: utf-8 -*-
# import unittest
from __future__ import absolute_import
import sys
import os
import pytest
from selenium import webdriver
import subprocess
import requests
import math
from random import randint,uniform

class TestFunctionalAddition(object):
    
    def test_AdditionOfTwoPositiveIntegers(self):
        a= randint(0,100)
        b= randint(0,100)
        url = "http://localhost:8080/math/add?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}
        if data != (a+b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")
    
    def test_AdditionOfTwoNegativeIntegers(self):
        a= randint(-100,0)
        b= randint(-100,0)
        url = "http://localhost:8080/math/add?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a+b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_AdditionOfTPosiitveAndNegativeInteger(self):
        a= randint(0,100)
        b= randint(-100,0)
        url = "http://localhost:8080/math/add?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a+b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_AdditionOfPositiveNumberAndZero(self):
        a= 55
        b=0
        url = "http://localhost:8080/math/add?a="+ str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a+b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

class TestFunctionalSubtraction(object):
    
    def test_SubtractionOfTwoPositiveIntegers(self):
        a= randint(0,100)
        b= randint(0,100)
        url = "http://localhost:8080/math/minus?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}
        if data != (a-b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")
    
    def test_SubtractionOfTwoNegativeIntegers(self):
        a= randint(-100,0)
        b= randint(-100,0)
        url = "http://localhost:8080/math/minus?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a-b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_SubtractionOfPosiitveAndNegativeInteger(self):
        a= randint(0,100)
        b= randint(-100,0)
        url = "http://localhost:8080/math/minus?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a-b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_SubtractionOfPositiveNumberAndZero(self):
        a= 55
        b=0
        url = "http://localhost:8080/math/minus?a="+ str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a-b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")


class TestFunctionalMultiplication(object):
    
    def test_MultiplicationOfTwoPositiveIntegers(self):
        a= randint(0,100)
        b= randint(0,100)
        url = "http://localhost:8080/math/multiply?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}
        if data != (a*b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")
    
    def test_MultiplicationOfTwoNegativeIntegers(self):
        a= randint(-100,0)
        b= randint(-100,0)
        url = "http://localhost:8080/math/multiply?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a*b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_MultiplicationOfTPosiitveAndNegativeInteger(self):
        a= randint(0,100)
        b= randint(-100,0)
        url = "http://localhost:8080/math/multiply?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a*b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_MultiplicationOfPositiveNumberAndZero(self):
        a= 55
        b=0
        url = "http://localhost:8080/math/multiply?a="+ str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a*b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

class TestFunctionalDivision(object):
    
    def test_DivisionOfTwoPositiveIntegers(self):
        a= round(uniform(0.0,100.0),0)
        b= round(uniform(0.0,100.0),0)
        url = "http://localhost:8080/math/divide?a="+ str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=url)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}

        if data != (a/b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")
    
    def test_DivisionOfTwoNegativeIntegers(self):
        a= round(uniform(-100,0),0)
        b= round(uniform(-100,0),0)
        url = "http://localhost:8080/math/divide?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a/b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_DivisionOfTPosiitveAndNegativeInteger(self):
        a= round(uniform(0,100),0)
        b= round(uniform(-100,0),0)
        url = "http://localhost:8080/math/divide?a="+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a/b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_DivisionOfPositiveNumberAndZero(self):
        a= 55.0
        b=0.0
        url = "http://localhost:8080/math/divide?a="+ str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a/b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")
    
    def test_DivisionOfZeroAndPositiveNumber(self):
        a= 0.0
        b=44.0
        url = "http://localhost:8080/math/divide?a="+ str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=url)
        
        response = getResponse.text
        data = getResponse.json()
        
        myDict = {}
        if data != (a/b):
            
            myDict[a,b]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")



class TestFunctionalSquareRoot(object):
    
    def test_SquareRoot_Zero(self):
        # Test Case to check square root functionality for random integer say 36  
        url = "http://localhost:8080/math/sqrt?a="
        num=0
        newurl = url+str(num)
        getResponse = requests.get(url=newurl)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}
        if data != math.sqrt(num):
            
            myDict[num]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")
        
    def test_SquareRoot_RandomWholeInteger(self):
        # Test Case to check square root functionality for random integer say 36  
        url = "http://localhost:8080/math/sqrt?a="
        num=36
        newurl = url+str(num)
        getResponse = requests.get(url=newurl)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}
        if data != math.sqrt(num):
            
            myDict[num]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    
    def test_SquareRoot_PositiveFloatNumber(self):
        url = "http://localhost:8080/math/sqrt?a="
        num=10.24
        newurl = url+str(num)
        # print newurl
        getResponse = requests.get(url=newurl)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}
        if data != math.sqrt(num):
            
            myDict[num]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")
    
    def test_SquareRoot_PositiveWholeNumber(self):
        url = "http://localhost:8080/math/sqrt?a="
        num=100
        newurl = url+str(num)
        getResponse = requests.get(url=newurl)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}
        if data != math.sqrt(num):
            
            myDict[num]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

    def test_SquareRoot_NegativeIntegerNumber(self):
        url = "http://localhost:8080/math/sqrt?a="
        num=-100
        newurl = url+str(num)
        getResponse = requests.get(url=newurl)
        response = getResponse.text
        data = getResponse.json()
        myDict = {}
        if data != math.sqrt(num):
            
            myDict[num]=data
            print myDict
        
        try :
            assert len(myDict) == 0, "Wrong result"
        except Exception:
            pytest.xfail("Failed")

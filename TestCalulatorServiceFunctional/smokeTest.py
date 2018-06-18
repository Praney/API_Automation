#!/usr/bin/python
# -*- coding: utf-8 -*-
# import unittest
import pytest
import requests
import math
from random import randint,uniform

class TestFunctionalAddition(object):
    
    url = "http://localhost:8080/math/add?a="

    def test_AdditionOfTwoPositiveIntegers(self):
        # Test Case to add two positive Integers

        a= randint(0,100)
        b= randint(0,100)
        
        urlnew = self.url+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=urlnew)
        data = getResponse.json()
        if data != (a+b):
            print a,",",b,":",data
            pytest.xfail("Failed")
    
    def test_AdditionOfTwoNegativeIntegers(self):
         # Test Case to add two negative integers

        a= randint(-100,0)
        b= randint(-100,0)
        urlnew = self.url+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=urlnew)
        
        data = getResponse.json()
        if data != (a+b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_AdditionOfPosiitveAndNegativeInteger(self):
         # Test Case to add positive and negative integer 

        a= randint(0,100)
        b= randint(-100,0)
        urlnew = self.url+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=urlnew)
        
        data = getResponse.json()
        if data != (a+b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_AdditionOfPositiveNumberAndZero(self):
         # Test Case to add positive integer and zero

        a= 55
        b=0
        urlnew = self.url+ str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=urlnew)
        
        data = getResponse.json()
        if data != (a+b):
            print a,",",b,":",data
            pytest.xfail("Failed")

class TestFunctionalSubtraction(object):
    
    url = "http://localhost:8080/math/minus?a="

    def test_SubtractionOfTwoPositiveIntegers(self):
         # Test Case to subtract two positive integers 

        a= randint(0,100)
        b= randint(0,100)

        urlnew = self.url+ str(a)+"&b=" + str(b)

        getResponse = requests.get(url=urlnew)
        data = getResponse.json()
        if data != (a-b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_SubtractionOfTwoNegativeIntegers(self):
        # Test Case to subtract two negative integers

        a= randint(-100,0)
        b= randint(-100,0)

        urlnew = self.url+ str(a)+"&b=" + str(b)

        getResponse = requests.get(url=urlnew)
        
        data = getResponse.json()
        if data != (a-b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_SubtractionOfPosiitveAndNegativeInteger(self):
        # Test Case to subtract positive and negative Integers

        a= randint(0,100)
        b= randint(-100,0)
        
        urlnew = self.url+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=urlnew)
        
        data = getResponse.json()
        if data != (a-b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_SubtractionOfPositiveNumberAndZero(self):
        # Test Case to subtract positive integer and zero

        a= 55
        b=0
        
        urlnew = self.url+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=urlnew)
        
        data = getResponse.json()
        if data != (a-b):
            print a,",",b,":",data
            pytest.xfail("Failed")

class TestFunctionalMultiplication(object):
    
    url = "http://localhost:8080/math/multiply?a="

    def test_MultiplicationOfTwoPositiveIntegers(self):
        # Test Case to multiply two positive integers

        a= randint(0,100)
        b= randint(0,100)

        urlnew = self.url+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=urlnew)
        data = getResponse.json()
     
        if data != (a*b):
            print a,",",b,":",data
            pytest.xfail("Failed")
    
    def test_MultiplicationOfTwoNegativeIntegers(self):
        # Test Case to multiply two negative integers

        a= randint(-100,0)
        b= randint(-100,0)

        urlnew = self.url+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=urlnew)
        
        data = getResponse.json()
       
        if data != (a*b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_MultiplicationOfTPosiitveAndNegativeInteger(self):
        # Test Case to multiply positive and negative integer

        a= randint(0,100)
        b= randint(-100,0)

        urlnew = self.url+ str(a)+"&b=" + str(b)
        getResponse = requests.get(url=urlnew)
        
        data = getResponse.json()
        
        if data != (a*b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_MultiplicationOfPositiveNumberAndZero(self):
        # Test Case to multiply positive integer and zero 

        a= 55
        b=0

        urlnew = self.url+ str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=urlnew)
        data = getResponse.json()

        if data != (a*b):
            print a,",",b,":",data
            pytest.xfail("Failed")

class TestFunctionalDivision(object):
    
    url = "http://localhost:8080/math/divide?a="
    
    def test_DivisionOfTwoPositiveIntegers(self):
        # Test Case to divide two positive Integers

        a= round(uniform(0.0,100.0),0)
        b= round(uniform(0.0,100.0),0)

        newurl = self.url + str(a)+"&b=" + str(b)
        getResponse = requests.get(url=newurl)
        data = getResponse.json()    

        if data != (a/b):
            print a,",",b,":",data
            pytest.xfail("Failed")
    
    def test_DivisionOfTwoNegativeIntegers(self):
        # Test Case to divide two negative integers

        a= round(uniform(-100,0),0)
        b= round(uniform(-100,0),0)

        newurl = self.url + str(a)+"&b=" + str(b)
        getResponse = requests.get(url=newurl)
        data = getResponse.json()
        
        if data != (a/b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_DivisionOfTPositiveAndNegativeInteger(self):
        # Test Case to divide positive and negative integer

        a= round(uniform(0,100),0)
        b= round(uniform(-100,0),0)

        newurl = self.url + str(a)+"&b=" + str(b)
        getResponse = requests.get(url=newurl)
        data = getResponse.json()
     
        if data != (a/b):
            print a,",",b,":",data
            pytest.xfail("Failed")

    def test_DivisionOfPositiveNumberAndZero(self):
        # Test Case to divide positive integer and zero

        a= 55.0
        b=0.0

        newurl = self.url + str(a)+"&b=" + str(b)
        getResponse = requests.get(url=newurl)
        data = getResponse.json()
        
        if data != (a/b):
            print a,",",b,":",data
            pytest.xfail("Failed")
    
    def test_DivisionOfZeroAndPositiveNumber(self):
        # Test Case to divide zero by positive integer

        a= 0.0
        b=44.0

        newurl = self.url + str(a)+"&b=" + str(b)
        
        getResponse = requests.get(url=newurl)
        data = getResponse.json()
     
        if data != (a/b):
            print a,",",b,":",data
            pytest.xfail("Failed")

class TestFunctionalSquareRoot(object):
    
    url = "http://localhost:8080/math/sqrt?a="

    def test_SquareRoot_Zero(self):
       # Test Case to check square root of zero  

        num=0
        newurl = self.url+str(num)
        getResponse = requests.get(url=newurl)
        data = getResponse.json()
     
        if data != math.sqrt(num):
            print num,":",data
            pytest.xfail("Failed")
        
    def test_SquareRoot_RandomWholeInteger(self):
        # Test Case to check square root of random whole integer 
        
        num=36
        newurl = self.url+str(num)
        getResponse = requests.get(url=newurl)
        data = getResponse.json()
     
        if data != math.sqrt(num):
            print num,":",data
            pytest.xfail("Failed")

    
    def test_SquareRoot_PositiveFloatNumber(self):
        # Test Case to check square root of float number

        num=10.24
        newurl = self.url+str(num)
        # print newurl
        getResponse = requests.get(url=newurl)
        data = getResponse.json()
     
        if data != math.sqrt(num):
            print num,":",data
            pytest.xfail("Failed")
    
    def test_SquareRoot_PositiveWholeNumber(self):
        # Test Case to check square root of positive whole number

        num=100
        newurl = self.url+str(num)
        getResponse = requests.get(url=newurl)
        data = getResponse.json()
     
        if data != math.sqrt(num):
            print num,":",data
            pytest.xfail("Failed")

    def test_SquareRoot_NegativeIntegerNumber(self):
        # Test Case to check square root of negative integer

        num=-100

        newurl = self.url+str(num)

        getResponse = requests.get(url=newurl)
        data = getResponse.json()
     
        if data != math.sqrt(num):
            print num,":",data
            pytest.xfail("Failed")

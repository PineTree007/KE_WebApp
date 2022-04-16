#!/usr/bin/env python
# coding: utf-8

from random import choice
from pyknow import *


class Property(Fact):
    """Info about the traffic Course."""
    pass

class PropertyRecommender(KnowledgeEngine):
    
   @Rule(Property(input='1000, 1, 1, 0, Downtown')) # LHS
   def HO01(self) :
        with open('./res.txt', 'w') as f:
            print("Condomium Studio", file=f)
        

   @Rule(Property(input='Buy, 4, 3, 1, NoDowntown')) #LHS
   def HO02(self) :
        with open('./res.txt', 'w') as f:
            print("Single-Family Detached house", file=f)
        

# Credential-Graduate,Bachelors,Adavanced Diploma
#  Area of interest-Health,Law,Business,IT
#  Semesters-2,3,4
#  Intake - September 2022,January 2023
#  Location - Oshawa,Whitby
# 
engine = PropertyRecommender()
engine.reset()
engine.get_rules()

# Declare a fact
engine.declare(Property(input='Buy, 4, 3, 1, NoDowntown'))

engine.run()
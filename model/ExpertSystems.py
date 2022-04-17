#!/usr/bin/env python
# coding: utf-8

from random import choice
from pyknow import *
from pyknow import L
from pyknow import W

class Property(Fact):
    pass

class PropertyRecommender(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find_property")
    
    
#    @Rule(Property(input='Rent,Investment,priceLow, smallYes, fam1, area2, downtownYes, expenseHigh, savingsLow')) # LHS
#    def HO01(self) :
#         with open('./res.txt', 'w') as f:
#             print("Rent a Condomium Studio Apartment", file=f)
        

#    @Rule(Property(input='Buy, 4, 3, 1, NoDowntown')) #LHS
#    def HO02(self) :
#         with open('./res.txt', 'w') as f:
#             print("Single-Family Detached house", file=f)
          
    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Rent"),
          Property(InvestOrLivein=W()), 
          Property(frequencyOfTravel=W()),
          Property(PriceRange="priceLow"),
          Property(bedroom=L("bed1")), 
          Property(area="area2"),
          Property(family=L("fam1")|L("fam2")),
          Property(location="downtownYes"),
          Property(social=W()),
          Property(dailyCommute=W())
         ) # LHS
    def HO01(self) :
        with open('./res.txt', 'w') as f:
            print("Rent a Condomium Studio Apartment", file=f)
      
engine = PropertyRecommender() 
engine.reset()
engine.get_rules() 
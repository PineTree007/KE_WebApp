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

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Rent"),
          Property(InvestOrLivein=W()), 
          Property(frequencyOfTravel=W()),
          Property(PriceRange="priceLow"),
          Property(bedroom=L("bed1")), 
          Property(area="area2"),
          Property(high="highYes"),
          Property(family=L("fam1")|L("fam2")),
          Property(location=L("downtownYes")|L("downtownSometimes")),
          Property(social=W()),
          Property(dailyCommute=W())
         ) 
    def HO01(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to rent a Condomium Studio/1BHK Apartment.\nA studio or 1BHK apartment is an excellent choice for someone who lives alone or as a family of 2, is looking to save money on rent, and appreciates an open, airy living space. Below are few suggestions for you!\nhttps://www.point2homes.com/CA/Apartment-Buildings/ON/Toronto/Cliffside/2550-Kingston/82282185.html\nhttps://www.point2homes.com/CA/Apartment-Buildings/ON/Toronto/Sherwood-Park/200-Roehampton/80880774.html\nhttps://www.point2homes.com/CA/Apartment-Buildings/ON/Toronto/Midtown-Toronto/Forest-Hill/600-Eglinton-Avenue-West/101732287.html"
            , file=f)

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Buy"),
          Property(InvestOrLivein="Investment"), 
          Property(frequencyOfTravel=W()),
          Property(PriceRange="priceLow"),
          Property(bedroom=L("bed1")), 
          Property(area="area2"),
          Property(high="highYes"),
          Property(family=L("fam1")|L("fam2")),
          Property(location=L("downtownYes")|L("downtownSometimes")),
          Property(social=W()),
          Property(dailyCommute=W())
         ) 
    def HO02(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to buy a Condomium Studio Apartment.\nA studio or 1BHK apartment is an excellent choice for someone who wants to invest low, and appreciates an open, airy living space. Below are few suggestions for you!\nhttps://www.point2homes.com/CA/Condo-For-Sale/ON/Toronto/Bayview-Village/Six99-Condos-699-Sheppard-Ave-E-North-York-ON-M2K-2P9/118918307.html\nhttps://www.point2homes.com/CA/Condo-For-Sale/ON/Toronto/Danforth-Village/Dawes-Condos/117618857.html", file=f)


    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Buy"),
          Property(InvestOrLivein="Livein"), 
          Property(frequencyOfTravel="Often"),
          Property(PriceRange="priceLow"),
          Property(bedroom="bed1"), 
          Property(area="area1"),
          Property(high=W()),
          Property(family=L("fam1")),
          Property(location=L("downtownSometimes")|L('downtownNo')),
          Property(social=W()),
          Property(dailyCommute=W())
         ) 
    def HO03(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to buy a Tiny Home.\nPeople are choosing to downsize the space they live in, simplify, and live with less. Especially for ones like you, who are frequent travellers, tiny home is the best choice. Below are few suggestions for you!\nhttps://www.kijiji.ca/v-house-for-sale/oshawa-durham-region/rent-to-own-laneway-garden-suites-and-micro-housing/1612812682\nhttps://www.kijiji.ca/v-house-for-sale/oakville-halton-region/2bdrm-tiny-house-mobile-home-addition-gazebo-shed-corner-lot/1612753159", file=f)

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Buy"),
          Property(InvestOrLivein=W()), 
          Property(frequencyOfTravel=W()),
          Property(PriceRange="priceMedium"),
          Property(bedroom="bed2"), 
          Property(area="area3"),
          Property(high="highYes"),
          Property(family=W()),
          Property(location=W()),
          Property(social="socialYes"),
          Property(dailyCommute=W())
         ) 
    def HO04(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to buy a Condomium 2BHK Apartment.\n Condominium 2BHK apartments are best suited for people like you who like living in high rise buildings and are socially active. Its a perfect option for you and your family. Below are few suggestions for you!\nhttps://www.realtor.ca/real-estate/24281277/3009-125-redpath-ave-toronto-mount-pleasant-west\nhttps://www.realtor.ca/real-estate/24281091/709-234-albion-rd-toronto-elms-old-rexdale", file=f)

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Rent"),
          Property(InvestOrLivein=W()), 
          Property(frequencyOfTravel="Often"),
          Property(PriceRange="priceMedium"),
          Property(bedroom="bed2"), 
          Property(area="area3"),
          Property(high="highYes"),
          Property(family=L("fam2")|L("fam3")),
          Property(location=L("downtownSometimes")|L('downtownYes')),
          Property(social="socialYes"),
          Property(dailyCommute=W())
         ) 
    def HO05(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to rent a Condomium 2BHK Apartment.\n Condominium 2BHK apartments are best suited for people like you who like living in high rise buildings and are socially active. Its a perfect option for you and your family, to live in a friendly neighborhood. Below are few suggestions for you!\nhttps://www.point2homes.com/CA/Condo-For-Rent/ON/Toronto/Armour-Heights/386-Yonge-St2316-Toronto-Ontario-M5B0A5/117122428.html\nhttps://www.point2homes.com/CA/Condo-For-Rent/ON/Toronto/Davisville-Village/2191-Yonge-St/112398459.html", file=f)


    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Buy"),
          Property(InvestOrLivein=W()), 
          Property(frequencyOfTravel=W()),
          Property(PriceRange="priceHigh"),
          Property(bedroom="bed3"), 
          Property(area="area3"),
          Property(high="highYes"),
          Property(family=W()),
          Property(location=W()),
          Property(social=W()),
          Property(dailyCommute=W())
         ) 
    def HO06(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to buy a Condomium 3BHK Apartment.\nCondominium 3BHK apartments are spacious and best suited for people like you who like living in high rise buildings and are socially active. Its a perfect option for you and your family, to live in a friendly neighborhood.\nhttps://www.point2homes.com/CA/Condo-For-Sale/ON/Toronto/Davisville-Village/5-SOUDAN-AVE/120246054.html\nhttps://www.point2homes.com/CA/Condo-For-Sale/ON/Toronto/Davisville-Village/68-MERTON-ST/120303327.html", file=f)


    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Rent"),
          Property(InvestOrLivein=W()), 
          Property(frequencyOfTravel=W()),
          Property(PriceRange="priceHigh"),
          Property(bedroom="bed3"), 
          Property(area="area4"),
          Property(high="highYes"),
          Property(family=L("fam2")|L("fam3")|L("fam4")),
          Property(location=L("downtownSometimes")|L('downtownYes')),
          Property(social="socialYes"),
          Property(dailyCommute=W())
         ) 
    def HO07(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to rent a Condomium 3BHK Apartment.\nCondominium 3BHK apartments are spacious and best suited for people like you who like living in high rise buildings and are socially active. Its a perfect option for you and your family, to live in a friendly neighborhood.\nhttps://www.point2homes.com/CA/Condo-For-Rent/ON/Toronto/Davisville-Village/89-DUNFIELD-AVE/118938002.html\nhttps://www.point2homes.com/CA/Condo-For-Rent/ON/Toronto/Davisville-Village/2221-YONGE-ST/120247998.html", file=f)

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Buy"),
          Property(InvestOrLivein="Livein"), 
          Property(frequencyOfTravel="Rare"),
          Property(PriceRange="priceHigh"),
          Property(bedroom=L("bed3")|L("bed4")), 
          Property(area="area4"),
          Property(high="highNo"),
          Property(family=L("fam2")|L("fam3")|L("fam4")),
          Property(location=L("downtownSometimes")|L('downtownNo')),
          Property(social="socialNo"),
          Property(dailyCommute=W())
         ) 
    def HO08(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to buy a Single-Family (Detached) Home. As you are person who loves to live in a peaceful environment and don't prefer living in high-rise buildings, single family home is the best option for you. Below are few suggestions!\n https://www.realtor.ca/real-estate/24281280/174-avondale-ave-toronto-willowdale-east\nhttps://www.realtor.ca/real-estate/24281050/58-hiscock-blvd-toronto-woburn", file=f)

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Rent"),
          Property(InvestOrLivein=W()), 
          Property(frequencyOfTravel="Rare"),
          Property(PriceRange=("priceHigh")),
          Property(bedroom=L("bed2")|L("bed3")|L("bed4")), 
          Property(area=L("area3")|L("area4")),
          Property(high="highNo"),
          Property(family=L("fam2")|L("fam3")|L("fam4")),
          Property(location=L("downtownSometimes")|L('downtownYes')),
          Property(social="socialNo"),
          Property(dailyCommute=W())
         ) 
    def HO09(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to Rent a Town home.\nAs you are person who loves to live in a peaceful environment and don't prefer living in high-rise buildings, Town home is the best option for you. Below are few suggestions!\nhttps://www.realtor.ca/real-estate/24078010/g21-16-capreol-crt-toronto-waterfront-communities-c1\nhttps://www.realtor.ca/real-estate/24093987/220-mcrae-dr-toronto-leaside ", file=f)

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Buy"),
          Property(InvestOrLivein="LiveIn"), 
          Property(frequencyOfTravel="Rare"),
          Property(PriceRange=("priceHigh")),
          Property(bedroom=L("bed2")|L("bed3")|L("bed4")), 
          Property(area=L("area3")|L("area4")),
          Property(high="highNo"),
          Property(family=L("fam2")|L("fam3")|L("fam4")),
          Property(location=L("downtownSometimes")|L('downtownYes')),
          Property(social="socialNo"),
          Property(dailyCommute=W())
         ) 
    def HO10(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to buy a Town home.\nAs you are person who loves to live in a peaceful environment and don't prefer living in high-rise buildings, Town home is the best option for you. Below are few suggestions!\nhttps://www.royallepage.ca/en/property/ontario/toronto/202-4064-lawrence-ave-e/17400400/mlse5579932/\nhttps://www.royallepage.ca/en/property/ontario/toronto/9-811-kennedy-rd/17398164/mlse5579385/", file=f)

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Buy"),
          Property(InvestOrLivein="Investment"), 
          Property(frequencyOfTravel=W()),
          Property(PriceRange=("priceHigh")),
          Property(bedroom=L("bed2")|L("bed3")|L("bed4")), 
          Property(area=L("area3")|L("area4")),
          Property(high="highNo"),
          Property(family=W()),
          Property(location=L("downtownSometimes")|L('downtownYes')),
          Property(social=W()),
          Property(dailyCommute=W())
         ) 
    def HO11(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to buy a Town home.\nAs you are an investor who wants to buy a house in a peaceful environment and don't prefer high-rise buildings, Town home is the best option for you. Below are few suggestions!\nhttps://www.royallepage.ca/en/property/ontario/toronto/202-4064-lawrence-ave-e/17400400/mlse5579932/\nhttps://www.royallepage.ca/en/property/ontario/toronto/9-811-kennedy-rd/17398164/mlse5579385/", file=f)

    @Rule(Fact(action='find_property'),
          Property(buyOrRent="Buy"),
          Property(InvestOrLivein="LiveIn"), 
          Property(frequencyOfTravel=W()),
          Property(PriceRange="priceLow"),
          Property(bedroom=L("bed1")), 
          Property(area="area2"),
          Property(high="highYes"),
          Property(family=L("fam1")|L("fam2")),
          Property(location=L("downtownYes")|L("downtownSometimes")),
          Property(social=W()),
          Property(dailyCommute=W())
         ) 
    def HO12(self) :
        with open('./res.txt', 'w') as f:
            print("I suggest you to buy a Condomium Studio/1BHK Apartment.\nA studio or 1BHK apartment is an excellent choice for someone who lives alone or as a family of 2, is looking to save money on rent, and appreciates an open, airy living space. Below are few suggestions for you!\nhttps://www.point2homes.com/CA/Apartment-Buildings/ON/Toronto/Cliffside/2550-Kingston/82282185.html\nhttps://www.point2homes.com/CA/Apartment-Buildings/ON/Toronto/Sherwood-Park/200-Roehampton/80880774.html\nhttps://www.point2homes.com/CA/Apartment-Buildings/ON/Toronto/Midtown-Toronto/Forest-Hill/600-Eglinton-Avenue-West/101732287.html", file=f)         
      
engine = PropertyRecommender() 
engine.reset()
engine.get_rules() 
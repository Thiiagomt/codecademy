# Best Fare Calculator

### Overview

If you’ve ever wondered if you chose the right fare option for riding the metro or bus, you’re not alone. In this 
project you will write a Java program that determines the best fare option for someone visiting New York City who plans 
to use the NYC transit system. The program should use constructors, methods, conditionals, loops, and arrays.

### TODO:

* Start by building a TransitCalculator class in TransitCalculator.java. The class should include
    * A main() method to run the code.
    * A field to keep track of the number of days a person will be using the transit system (up to 30 days).
    * A field to keep track of the number of individual rides the person expects to take in that time.

* Build a class constructor for TransitCalculator that accepts the number of days and rides and sets the values for the 
corresponding fields.

* The NYC transit system has three regular fare options:
    * Pay-per-ride (single ride): $2.75
    * 7-day Unlimited Rides: $33.00
    * 30-day Unlimited Rides: $127.00
    <p> Add variables or arrays to the class to keep track of these values.

* Create a method unlimited7Price() with a double return type. The method should return the overall price per ride of 
using the 7-day Unlimited option.
    * 20 rides over 19 days should return 4.95
    * 50 rides over 22 days should return 2.64
    * 14 rides over 6 days should return either 2.357142857142857 or 2.36
    <p> Make sure to account for all days the person might be riding public transit in NYC. For example, if a person 
    plans to use the train or bus over the course of 15 days, then three 7-day Unlimited purchases would be required.

* Build a method getRidePrices() that will return an array of doubles. Inside the method, you’ll need to calculate the 
price per ride for each fare option. You should use the unlimited7Price() method to determine this value for the 7-day 
Unlimited option.
    <p> The method should return an array of the price per ride for the three fare options.

* Create a String method called getBestFare().
  <p> Inside the method, you should use the array of ride prices calculated with getRidePrices() and at least one loop to determine:
  
    * the lowest price
    * the best (corresponding) fare method
  
  At the end of the method, you should return a String that communicates the findings.
  
  For example, for 54 rides over the course of 26 days, the method should return the following text:
  
        You should get the 30-day Unlimited option at $2.35 per ride.
  
  For 12 rides over the course of 5 days, the method should return:
  
        You should get the Pay-per-ride option at $2.75 per ride.

* #### Extra tools:
    - [X] The NYC transit system also offers reduced fare options for people with disabilities and people who are at 
    least 65 years old. Refactor the TransitCalculator class so that it checks if the rider qualifies for reduced fare 
    and calculates the best reduced fare option if they do.
        * Pay-per-ride (single ride): $1.35
        * 7-day Unlimited Rides: $16.50
        * 30-day Unlimited Rides: $63.50 
    
    - [ ] NYC isn’t the only city where there are several fare options available! Extend your TransitCalculator to work 
    for a different city. Pick your own, or choose from these below:
        * [Vancouver](https://www.translink.ca/Fares-and-Passes/Fare-Pricing.aspx)
        * [Mexico](https://mexicometro.org/about/fares/)
        * [Delhi](http://www.delhimetrorail.com/recharge_Info.aspx)
        * [Berlin](https://www.visitberlin.de/en/public-transport-berlin)
        * [Paris](https://www.ratp.fr/en/titres-et-tarifs)
        * [Seoul](http://www.seoulmetro.co.kr/en/page.do?menuIdx=348)
# Become A Pokémon Master

### Overview

In this project, you will be using Python Classes to create a game system similar to the popular game 
series Pokémon. If you’re unfamiliar with Pokémon, it is a game where creatures (Pokémon) battle against 
each other. Every Pokémon has statistics associated with it like health, level, type, and a name. In this 
project we’ll make several classes that interact with each other so you can create your own Pokémon battles!

### TODO:

* Create a Pokémon class. The __init__() method of our Pokémon class created variables to keep track of the Pokémon’s name, level, type (for example "Fire" or "Water"), maximum health, current health, and whether or not the Pokémon was knocked out. In our implementation, the maximum health was determined by the Pokémon’s level.

* Give your Pokémon class some functionality. Our Pokémon class had a variety of methods that changed the variables associated with a Pokémon. For example, it had a method the decreased the Pokémon’s health (we called this lose_health) and a method for regaining health. We also created a method that would officially “knock out” a Pokémon (when its health became 0) and another method to revive a knocked out Pokémon.<br>
All of these methods had print statements to let the user know what was happening. For example, we might print something like "Charmander now has 30 health" when healing.

* One of the trickier methods we created in the Pokémon class was the attack method. This method takes another Pokémon as an argument and deals damage to that Pokémon.<br>
The amount of damage dealt depends on the types of the attacking Pokémon and the Pokémon being attacked. If the attacking Pokémon has advantage over the other Pokémon (for example, a "Fire" Pokémon attacking a "Grass" Pokémon), we dealt damage equal to twice the attacking Pokémon’s level. If the attacking Pokémon was at a disadvantage (for example, a "Grass" Pokémon attacking a "Fire" Pokémon), we dealt damage equal to half the attacking Pokémon’s level.<br>
There are a [huge number of types](https://pokemondb.net/type) with advantages and disadvantages, but we only coded Fire, Water, and Grass.<br>
Make sure to put in appropriate print statements to let the user know what is happening when one Pokémon attacks another.

* Make a Trainer class. A Trainer can have up to 6 Pokémon, which we stored in a list. A trainer also has a name, and a number of potions they can use to heal their Pokémon. A trainer also has a “currently active Pokémon”, which we represented as a number.

* Give your Trainer class some functionality through methods. Our trainer is able to use a potion and attack another trainer. When a potion is used, it heals the trainer’s currently active Pokémon. Similarly, when a trainer attacks another trainer, the currently active Pokémon deals damage to the other trainer’s current Pokémon. Finally, the trainer is able to switch which Pokémon is currently active.<br>
Again, make sure to include print statements with all of these methods so the user can understand what is happening.

* After experimenting with your Classes, go back to your methods and add some logic to deal with edge cases that you might not have thought about. Here are a couple of examples that you could try to implement:
    - A potion should not be able to heal a Pokémon past its maximum health.
    - A Pokémon that is knocked out should not be able to attack another Pokémon.
    - A trainer should not be able to switch their active Pokémon to one that is knocked out

* #### Extra tools:
    - [ ] Give Pokémon experience for battling other Pokémon. A Pokémon’s level should increase once it gets enough experience points.
    - [ ] Create specific Classes that inherit from the general Pokémon class. For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
    - [ ] Let your Pokémon evolve once they hit a certain level.
    - [ ] Have more stats associated with a Pokémon. In the real game, every Pokémon has stats like Speed, Attack, Defense. All of those stats effect the way Pokemon battle with each other. For example, the Pokémon with the larger Speed stat will go first in the battle.


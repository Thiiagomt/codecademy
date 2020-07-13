# List of pokemon types
list_types_of_pokemon = ['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground',
                         'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']


# Pokemon Class
class Pokemon:
    def __init__(self, name, type, level):
        self.name = name
        self.level = level
        self.type = type
        if self.level <= 25:
            self.max_health = 100
        elif self.level <= 50:
            self.max_health = 500
        else:
            self.max_health = 1000
        self.current_health = self.max_health
        self.is_knocked_out = False

    def lose_health(self, lost_health):
        if not self.is_knocked_out:
            self.current_health -= lost_health

            print(self.name + ' suffered an attack and take it ' + str(lost_health) + ' points of damage.')

            if self.current_health <= 0:
                self.knock_out()
                print(
                    self.name + ' was knocked out and your current health is: ' + str(self.current_health) + ' points.')
            else:
                if self.current_health == 1:
                    print(self.name + ' current health is: ' + str(self.current_health) + ' point.')
                else:
                    print(self.name + ' current health is: ' + str(self.current_health) + ' points.')
        else:
            print(self.name + ' is knocked out. You need to revive him first.')

        return self.current_health

    def gain_health(self, gain_health):
        if not self.is_knocked_out:
            self.current_health += gain_health

            print(self.name + ' gain ' + str(gain_health) + ' health points!')

            if self.current_health > self.max_health:
                self.current_health = self.max_health

            print(self.name + ' current health is: ' + str(self.current_health) + ' points.')
        else:
            print(self.name + ' is knocked out. Revive is the only way to get back ' + self.name)

        return self.current_health

    def knock_out(self):
        self.is_knocked_out = True
        self.current_health = 0

    def revive(self):
        self.is_knocked_out = False
        self.current_health = self.max_health


pikachu = Pokemon('Pikachu', 'Electric', 30)

print()
print(pikachu.current_health)
print()
pikachu.lose_health(100)
print()
pikachu.gain_health(50)
print()


from pokemon_base import *
import inspect

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 45
        self.level = 1
        self.poketype = PokeType.GRASS
        self.battle_power = 14
        self.evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
        self.name = "Bulbasaur"
        self.experience = 0
        self.defence = 20
        self.speed = 4.5

class Charmander(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 39
        self.level = 1
        self.poketype = PokeType.FIRE
        self.battle_power = 22
        self.evolution_line = ["Charmander", "Charmeleon", "Charizard"]
        self.name = "Charmander"
        self.experience = 0
        self.defence = 10
        self.speed = 65

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 44
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 10
        self.evolution_line = ["Squirtle", "Wartortle", "Blastoise"]
        self.name = "Squirtle"
        self.experience = 0
        self.defence = 12
        self.speed = 43

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.level = 1
        self.poketype = PokeType.BUG
        self.battle_power = 7
        self.evolution_line = ["Caterpie", "Metapod", "Butterfree"]
        self.name = "Caterpie"
        self.experience = 0
        self.defence = 8
        self.speed = 30

class Weedle(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 25
        self.level = 1
        self.poketype = PokeType.BUG
        self.battle_power = 9
        self.evolution_line = ["Weedle", "Kakuna", "Beedrill"]
        self.name = "Weedle"
        self.experience = 0
        self.defence = 10
        self.speed = 50

class Pidgey(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.FLYING
        self.battle_power = 21
        self.evolution_line = ["Pidgey", "Pidgeotto", "Pidgeot"]
        self.name = "Pidgey"
        self.experience = 0
        self.defence = 8
        self.speed = 56

class Rattata(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 15
        self.evolution_line = ["Rattata", "Raticate"]
        self.name = "Rattata"
        self.experience = 0
        self.defence = 5
        self.speed = 72

class Spearow(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.FLYING
        self.battle_power = 19
        self.evolution_line = ["Spearow", "Fearow"]
        self.name = "Spearow"
        self.experience = 0
        self.defence = 9
        self.speed = 70

class Ekans(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 35
        self.level = 1
        self.poketype = PokeType.POISON
        self.battle_power = 15
        self.evolution_line = ["Ekans", "Arbok"]
        self.name = "Ekans"
        self.experience = 0
        self.defence = 8
        self.speed = 55

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 35
        self.level = 1
        self.poketype = PokeType.ELECTRIC
        self.battle_power = 30
        self.evolution_line = ["Pikachu", "Raichu"]
        self.name = "Pikachu"
        self.experience = 0
        self.defence = 15
        self.speed = 90

class Sandshrew(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.level = 1
        self.poketype = PokeType.GROUND
        self.battle_power = 30
        self.evolution_line = ["Sandshrew", "Sandslash"]
        self.name = "Sandshrew"
        self.experience = 0
        self.defence = 20
        self.speed = 40

class NidoranM(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 46
        self.level = 1
        self.poketype = PokeType.POISON
        self.battle_power = 23
        self.evolution_line = ["Nidoran(M)", "Nidorino", "Nidoking"]
        self.name = "Nidoran(M)"
        self.experience = 0
        self.defence = 7
        self.speed = 41

class NidoranF(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 55
        self.level = 1
        self.poketype = PokeType.POISON
        self.battle_power = 20
        self.evolution_line = ["Nidoran(F)", "Nidorina", "Nidoqueen"]
        self.name = "Nidoran(F)"
        self.experience = 0
        self.defence = 12
        self.speed = 56

class Clefairy(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 70
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 17
        self.evolution_line = ["Clefairy", "Clefable"]
        self.name = "Clefairy"
        self.experience = 0
        self.defence = 15
        self.speed = 35

class Vulpix(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 38
        self.level = 1
        self.poketype = PokeType.FIRE
        self.battle_power = 21
        self.evolution_line = ["Vulpix", "Ninetales"]
        self.name = "Vulpix"
        self.experience = 0
        self.defence = 8
        self.speed = 65

class Jigglypuff(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 67
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 13
        self.evolution_line = ["Jigglypuff", "Wigglytuff"]
        self.name = "Jigglypuff"
        self.experience = 0
        self.defence = 8
        self.speed = 20

class Zubat(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.POISON
        self.battle_power = 20
        self.evolution_line = ["Zubat", "Golbat"]
        self.name = "Zubat"
        self.experience = 0
        self.defence = 7
        self.speed = 80

class Oddish(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 45
        self.level = 1
        self.poketype = PokeType.GRASS
        self.battle_power = 18
        self.evolution_line = ["Oddish", "Gloom", "Vileplume"]
        self.name = "Oddish"
        self.experience = 0
        self.defence = 7
        self.speed = 30

class Paras(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 35
        self.level = 1
        self.poketype = PokeType.BUG
        self.battle_power = 23
        self.evolution_line = ["Paras", "Parasect"]
        self.name = "Paras"
        self.experience = 0
        self.defence = 10
        self.speed = 25

class Venonat(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.level = 1
        self.poketype = PokeType.BUG
        self.battle_power = 30
        self.evolution_line = ["Venonat", "Venomoth"]
        self.name = "Venonat"
        self.experience = 0
        self.defence = 15
        self.speed = 45

class Diglett(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 10
        self.level = 1
        self.poketype = PokeType.GROUND
        self.battle_power = 29
        self.evolution_line = ["Diglett", "Dugtrio"]
        self.name = "Diglett"
        self.experience = 0
        self.defence = 15
        self.speed = 95

class Meowth(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 20
        self.evolution_line = ["Meowth", "Persian"]
        self.name = "Meowth"
        self.experience = 0
        self.defence = 8
        self.speed = 90

class Psyduck(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 20
        self.evolution_line = ["Psyduck", "Golduck"]
        self.name = "Psyduck"
        self.experience = 0
        self.defence = 15
        self.speed = 55

class Mankey(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.FIGHTING
        self.battle_power = 35
        self.evolution_line = ["Mankey", "Primeape"]
        self.name = "Mankey"
        self.experience = 0
        self.defence = 20
        self.speed = 70

class Growlithe(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 55
        self.level = 1
        self.poketype = PokeType.FIRE
        self.battle_power = 24
        self.evolution_line = ["Growlithe", "Arcanine"]
        self.name = "Growlithe"
        self.experience = 0
        self.defence = 12
        self.speed = 60

class Poliwag(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 20
        self.evolution_line = ["Poliwag", "Poliwhirl", "Poliwrath"]
        self.name = "Poliwag"
        self.experience = 0
        self.defence = 8
        self.speed = 90

class Abra(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 25
        self.level = 1
        self.poketype = PokeType.PSYCHIC
        self.battle_power = 10
        self.evolution_line = ["Abra", "Kadabra", "Alakazam"]
        self.name = "Abra"
        self.experience = 0
        self.defence = 5
        self.speed = 90

class Machop(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 55
        self.level = 1
        self.poketype = PokeType.FIGHTING
        self.battle_power = 30
        self.evolution_line = ["Machop", "Machoke", "Machamp"]
        self.name = "Machop"
        self.experience = 0
        self.defence = 26
        self.speed = 35

class Bellsprout(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.level = 1
        self.poketype = PokeType.GRASS
        self.battle_power = 26
        self.evolution_line = ["Bellsprout", "Weepinbell", "Victreebel"]
        self.name = "Bellsprout"
        self.experience = 0
        self.defence = 13
        self.speed = 40

class Tentacool(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 25
        self.evolution_line = ["Tentacool", "Tentacruel"]
        self.name = "Tentacool"
        self.experience = 0
        self.defence = 15
        self.speed = 70

class Geodude(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.ROCK
        self.battle_power = 7
        self.evolution_line = ["Geodude", "Graveler", "Golem"]
        self.name = "Geodude"
        self.experience = 0
        self.defence = 35
        self.speed = 20

class Ponyta(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.level = 1
        self.poketype = PokeType.FIRE
        self.battle_power = 25
        self.evolution_line = ["Ponyta", "Rapidash"]
        self.name = "Ponyta"
        self.experience = 0
        self.defence = 12
        self.speed = 90

class Slowpoke(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 66
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 8
        self.evolution_line = ["Slowpoke", "Slowbro"]
        self.name = "Slowpoke"
        self.experience = 0
        self.defence = 20
        self.speed = 15

class Magnemite(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 25
        self.level = 1
        self.poketype = PokeType.ELECTRIC
        self.battle_power = 20
        self.evolution_line = ["Magnemite", "Magneton"]
        self.name = "Magnemite"
        self.experience = 0
        self.defence = 8
        self.speed = 45

class Farfetchd(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 52
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 17
        self.evolution_line = ["Farfetchd"]
        self.name = "Farfetchd"
        self.experience = 0
        self.defence = 12
        self.speed = 60

class Doduo(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 35
        self.level = 1
        self.poketype = PokeType.FLYING
        self.battle_power = 30
        self.evolution_line = ["Doduo", "Dodrio"]
        self.name = "Doduo"
        self.experience = 0
        self.defence = 15
        self.speed = 75

class Seel(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 65
        self.level = 1
        self.poketype = PokeType.ICE
        self.battle_power = 45
        self.evolution_line = ["Seel", "Dewgong"]
        self.name = "Seel"
        self.experience = 0
        self.defence = 25
        self.speed = 65

class Grimer(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 80
        self.level = 1
        self.poketype = PokeType.POISON
        self.battle_power = 30
        self.evolution_line = ["Grimer", "Muk"]
        self.name = "Grimer"
        self.experience = 0
        self.defence = 25
        self.speed = 25

class Shellder(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 20
        self.evolution_line = ["Shellder", "Cloyster"]
        self.name = "Shellder"
        self.experience = 0
        self.defence = 12
        self.speed = 40

class Gastly(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.level = 1
        self.poketype = PokeType.GHOST
        self.battle_power = 25
        self.evolution_line = ["Gastly", "Haunter", "Gengar"]
        self.name = "Gastly"
        self.experience = 0
        self.defence = 10
        self.speed = 80

class Onix(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 35
        self.level = 1
        self.poketype = PokeType.ROCK
        self.battle_power = 45
        self.evolution_line = ["Onix", "Steelix"]
        self.name = "Onix"
        self.experience = 0
        self.defence = 20
        self.speed = 30

class Drowzee(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.level = 1
        self.poketype = PokeType.PSYCHIC
        self.battle_power = 25
        self.evolution_line = ["Drowzee", "Hypno"]
        self.name = "Drowzee"
        self.experience = 0
        self.defence = 12
        self.speed = 42

class Krabby(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 22
        self.evolution_line = ["Krabby", "Kingler"]
        self.name = "Krabby"
        self.experience = 0
        self.defence = 8
        self.speed = 50

class Voltorb(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.ELECTRIC
        self.battle_power = 30
        self.evolution_line = ["Voltorb", "Electrode"]
        self.name = "Voltorb"
        self.experience = 0
        self.defence = 15
        self.speed = 100

class Exeggcute(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.level = 1
        self.poketype = PokeType.GRASS
        self.battle_power = 17
        self.evolution_line = ["Exeggcute", "Exeggutor"]
        self.name = "Exeggcute"
        self.experience = 0
        self.defence = 7
        self.speed = 20

class Cubone(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.level = 1
        self.poketype = PokeType.GROUND
        self.battle_power = 18
        self.evolution_line = ["Cubone", "Marowak"]
        self.name = "Cubone"
        self.experience = 0
        self.defence = 8
        self.speed = 35

class Hitmonlee(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.level = 1
        self.poketype = PokeType.FIGHTING
        self.battle_power = 25
        self.evolution_line = ["Hitmonlee"]
        self.name = "Hitmonlee"
        self.experience = 0
        self.defence = 15
        self.speed = 87

class Hitmonchan(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.level = 1
        self.poketype = PokeType.FIGHTING
        self.battle_power = 30
        self.evolution_line = [ "Hitmonchan"]
        self.name = "Hitmonchan"
        self.experience = 0
        self.defence = 20
        self.speed = 76

class Lickitung(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 90
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 55
        self.evolution_line = ["Lickitung"]
        self.name = "Lickitung"
        self.experience = 0
        self.defence = 35
        self.speed = 30

class Koffing(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.POISON
        self.battle_power = 35
        self.evolution_line = ["Koffing", "Weezing"]
        self.name = "Koffing"
        self.experience = 0
        self.defence = 25
        self.speed = 35

class Rhyhorn(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 80
        self.level = 1
        self.poketype = PokeType.GROUND
        self.battle_power = 45
        self.evolution_line = ["Rhyhorn", "Rhydon"]
        self.name = "Rhyhorn"
        self.experience = 0
        self.defence = 50
        self.speed = 25

class Chansey(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 150
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 5
        self.evolution_line = ["Chansey", "Blissey"]
        self.name = "Chansey"
        self.experience = 0
        self.defence = 5
        self.speed = 50

class Tangela(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 65
        self.level = 1
        self.poketype = PokeType.GRASS
        self.battle_power = 28
        self.evolution_line = ["Tangela"]
        self.name = "Tangela"
        self.experience = 0
        self.defence = 24
        self.speed = 30

class Kangaskhan(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 88
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 32
        self.evolution_line = ["Kangaskhan"]
        self.name = "Kangaskhan"
        self.experience = 0
        self.defence = 60
        self.speed = 70

class Horsea(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 10
        self.evolution_line = ["Horsea", "Seadra"]
        self.name = "Horsea"
        self.experience = 0
        self.defence = 10
        self.speed = 60

class Goldeen(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 45
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 11
        self.evolution_line = ["Goldeen", "Seaking"]
        self.name = "Goldeen"
        self.experience = 0
        self.defence = 15
        self.speed = 65

class Staryu(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 10
        self.evolution_line = ["Staryu", "Starmie"]
        self.name = "Staryu"
        self.experience = 0
        self.defence = 10
        self.speed = 85

class MrMime(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.PSYCHIC
        self.battle_power = 10
        self.evolution_line = ["Mr. Mime"]
        self.name = "Mr. Mime"
        self.experience = 0
        self.defence = 10
        self.speed = 30

class Scyther(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 70
        self.level = 1
        self.poketype = PokeType.BUG
        self.battle_power = 20
        self.evolution_line = ["Scyther"]
        self.name = "Scyther"
        self.experience = 0
        self.defence = 15
        self.speed = 105

class Jynx(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 65
        self.level = 1
        self.poketype = PokeType.ICE
        self.battle_power = 20
        self.evolution_line = ["Jynx"]
        self.name = "Jynx"
        self.experience = 0
        self.defence = 35
        self.speed = 95

class Electabuzz(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 65
        self.level = 1
        self.poketype = PokeType.ELECTRIC
        self.battle_power = 15
        self.evolution_line = ["Electabuzz"]
        self.name = "Electabuzz"
        self.experience = 0
        self.defence = 12
        self.speed = 100

class Magmar(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 65
        self.level = 1
        self.poketype = PokeType.FIRE
        self.battle_power = 20
        self.evolution_line = ["Magmar"]
        self.name = "Magmar"
        self.experience = 0
        self.defence = 10
        self.speed = 80

class Pinsir(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 65
        self.level = 1
        self.poketype = PokeType.BUG
        self.battle_power = 20
        self.evolution_line = ["Pinsir"]
        self.name = "Pinsir"
        self.experience = 0
        self.defence = 35
        self.speed = 85

class Tauros(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 75
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 15
        self.evolution_line = ["Tauros"]
        self.name = "Tauros"
        self.experience = 0
        self.defence = 10
        self.speed = 110

class Magikarp(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 5
        self.evolution_line = ["Magikarp", "Gyarados"]
        self.name = "Magikarp"
        self.experience = 0
        self.defence = 10
        self.speed = 80

class Lapras(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 90
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 12
        self.evolution_line = ["Lapras"]
        self.name = "Lapras"
        self.experience = 0
        self.defence = 10
        self.speed = 60

class Ditto(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 48
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 10
        self.evolution_line = ["Ditto"]
        self.name = "Ditto"
        self.experience = 0
        self.defence = 48
        self.speed = 50

class Eevee(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 55
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 10
        self.evolution_line = ["Eevee"]
        self.name = "Eevee"
        self.experience = 0
        self.defence = 35
        self.speed = 55

class Porygon(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 65
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 12
        self.evolution_line = ["Porygon"]
        self.name = "Porygon"
        self.experience = 0
        self.defence = 7
        self.speed = 60

class Omanyte(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 35
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 12
        self.evolution_line = ["Omanyte", "Omastar"]
        self.name = "Omanyte"
        self.experience = 0
        self.defence = 20
        self.speed = 40

class Kabuto(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.level = 1
        self.poketype = PokeType.ROCK
        self.battle_power = 10
        self.evolution_line = ["Kabuto", "Kabutops"]
        self.name = "Kabuto"
        self.experience = 0
        self.defence = 10
        self.speed = 55

class Aerodactyl(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 80
        self.level = 1
        self.poketype = PokeType.ROCK
        self.battle_power = 25
        self.evolution_line = ["Aerodactyl"]
        self.name = "Aerodactyl"
        self.experience = 0
        self.defence = 5
        self.speed = 130

class Snorlax(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 85
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 20
        self.evolution_line = ["Munchlax", "Snorlax"]
        self.name = "Snorlax"
        self.experience = 0
        self.defence = 10
        self.speed = 30

class Articuno(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 90
        self.level = 1
        self.poketype = PokeType.ICE
        self.battle_power = 30
        self.evolution_line = ["Articuno"]
        self.name = "Articuno"
        self.experience = 0
        self.defence = 20
        self.speed = 85

class Zapdos(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 90
        self.level = 1
        self.poketype = PokeType.ELECTRIC
        self.battle_power = 30
        self.evolution_line = ["Zapdos"]
        self.name = "Zapdos"
        self.experience = 0
        self.defence = 20
        self.speed = 100

class Moltres(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 90
        self.level = 1
        self.poketype = PokeType.FIRE
        self.battle_power = 25
        self.evolution_line = ["Moltres"]
        self.name = "Moltres"
        self.experience = 0
        self.defence = 10
        self.speed = 90

class Dratini(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 41
        self.level = 1
        self.poketype = PokeType.DRAGON
        self.battle_power = 12
        self.evolution_line = ["Dratini", "Dragonair", "Dragonite"]
        self.name = "Dratini"
        self.experience = 0
        self.defence = 10
        self.speed = 86

def get_all_pokemon_types():
    all_pokemon = ArrayR(77)
    i = 0
    for name, cls in inspect.getmembers(inspect.getmodule(inspect.currentframe()), inspect.isclass):
        if name not in ['ABC', 'PokeType', 'Pokemon', 'TypeEffectiveness', 'Enum', 'ArrayR']:
            all_pokemon[i] = cls
            i += 1
    return all_pokemon


if __name__ == '__main__':
    pass
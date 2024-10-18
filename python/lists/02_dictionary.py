character = {
    "pedofile" :" person sexually attracted to childern",
    "jirya" : "pervy sage",
    "tsunade" : "Source of anger",
    "sakura" : "dustbin",
    "obito" : "blindly fall in love with rin",
    "Madara" : "leader of devil masterminded",
    "pain" : "leader of akatsuki",
    "naruto" : "never give up",
    "itachi" : "Best legend",
    "hinata" : "Best girl in the universe"
}
print(character["hinata"])
for char in character:
    print(char,character[char], sep =' : ')

# multiple dictionary

anime = [
    {"name":"hinata", "character":"best girl in the universe","lover":"naruto"},
    {"name":"sakura", "character":"trash girl in the universe","lover":"sasuke"},
    {"name":"izume", "character":"one of the girl in uchiha clan","lover":"itachi"},
    {"name":"jirya", "character":"pervy and legendary sanin","lover":"tsunade"},
    {"name":"obito", "character":"declare war for one girl who even doesn't love him","lover":"rin"}#none keyword can also be used in python
]
for char in anime:
    print(char["name"],char["character"],char["lover"], sep=" : ")
print(anime["name"])
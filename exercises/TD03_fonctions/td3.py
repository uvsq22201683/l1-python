#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    temps_s = temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3]
    return temps_s

#temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    secondes_t = [0, 0, 0, 0]
    secondes_t[0] = seconde//86400
    seconde = seconde%86400

    secondes_t[1] = seconde//3600
    seconde = seconde%3600
    secondes_t[2] = seconde//60
    secondes_t[3] = seconde%60
    return secondes_t
    
#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def create_message_affiche(nb, unite):
    message = ''
    if nb ==1:
        message = str(int(nb)) + ' ' + unite+ ' '
    elif nb>1:
        message = str(int(nb)) + ' ' + unite+ 's '
    return message

def afficheTemps(temps):
    unites = ['jour','heure', 'minute', 'seconde']
    message = ''
    for i in range(4):
        message += create_message_affiche(temps[i], unites[i])
    print(message)
    
#afficheTemps((1,0,14,23))   

def demandeTemps():
    bonne_valeur = False
    temps = [0,0,0,0]
    valeurs_max = [0, 24, 60, 60]
    for i in range(4):
        bonne_valeur = False
        while bonne_valeur == False:
            temps[i] = int(input())
            if i==0:
                bonne_valeur = True
            elif temps[i] < valeurs_max[i]:
                bonne_valeur = True
    return temps

#afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    somme_temps = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    somme_temps = secondeEnTemps(somme_temps)
    print(somme_temps)
    return somme_temps

#sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(proportion, temps):
    proportion_temps = tempsEnSeconde(temps)*proportion
    proportion_temps = secondeEnTemps(proportion_temps)
    print(proportion_temps)
    return proportion_temps

#afficheTemps(proportionTemps(0.2, (2,0,36,0)))

def tempsEnDate(temps):
    date = []

def afficheDate(date = -1):
    pass
    
#temps = secondeEnTemps(1000000000)
#afficheTemps(temps)
#afficheDate(tempsEnDate(temps))
#afficheDate()
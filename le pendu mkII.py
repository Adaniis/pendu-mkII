import random
import string
import os
PINK = "\033[95;5m"
vert = "\033[92m"
BLUE = "\033[94m"
RED_FLASH = "\033[91;5m"
RESET = "\033[0m"
jeu = True 
C_1 = 0
C_2 = 0
C_3 = 0
lev_1 = ["chat","chien","oiseau","lapin","serpent"]
lev_2 = ["historiographie","tardigrade","revolutionnaire","archeologie","chronologique","historiquement"]
lev_3 = ["informatisation","developpement","cyber-securitee","telecommunication","intergouvernemental"]
def level(diff):
    if diff == "1" : 
        mot_a_trouver = random.choice(lev_1)
    if diff == "2" : 
        mot_a_trouver = random.choice(lev_2)
    if diff == "3" : 
        mot_a_trouver = random.choice(lev_3)
    return mot_a_trouver

def boucle(lettre,c_erreur,c_tent):
    
    if lettre in mot_trouver or lettre in erreur : 
        print(RED_FLASH+"La lettre a déjà été essayée "+RESET)
    if lettre in mot_a_trouver and lettre not in mot_trouver : 
        for i in range(len(mot_a_trouver)):
            if lettre == mot_a_trouver[i] : 
                mot_trouver[i] = lettre
        c_tent += 1
        return c_erreur, c_tent 
    if lettre not in erreur and lettre not in mot_a_trouver  : 
        erreur.append(lettre)
        c_erreur +=1
        c_tent +=1
    return c_erreur, c_tent

def pendu(c_erreur, matrice):
    match c_erreur:
        case 1:
            matrice[5][0] = matrice[5][1] = matrice[5][2] = matrice[5][3] = matrice[5][4] = "="
        case 2:
            matrice[4][0] = matrice[3][0] = matrice[2][0] = matrice[1][0] = matrice[0][0] = "|"
        case 3:
            matrice[0][1] = matrice[0][2] = matrice[0][3] = "-"
        case 4:
            matrice[1][3] = "|"
        case 5:
            matrice[2][3] = "O"
        case 6:
            matrice[3][3] = "|"
        case 7:
            matrice[3][2] = "-"
            matrice[1][2]=matrice[2][2]= " "
            matrice[1][4]=matrice[2][4]= " "
        case 8:
            matrice[3][4] = "-"
        case 9:
            matrice[4][4] = "\\"
        case 10:
            matrice[4][2] = "/"
    chaine = "\n".join(" ".join(ligne) for ligne in matrice)
    print(chaine)

def again (restart):
    while restart != "oui"  and restart != "non" :
        os.system('cls')
        restart = input("Pas si facile de le casser hein \n Rejouer oui | non  ").lower()
    if restart == "oui" : 
        jeu = True 
    if restart == "non":
        jeu = False
    return jeu 



while jeu : 
    erreur = []*10
    c_erreur = 0 
    matrice = [["" for i in range(5)] for i in range(6)]
    c_tent = 1
    print(BLUE+ f"|============================================|"+RESET)
    print(vert+ f"|facile entre 4 et 7 lettres = 1  gagnée {C_1}/5 |"+RESET)
    print(BLUE+ f"|============================================|"+RESET)
    print(PINK+ f"|moyen entre 10 et 15 lettres = 2 gagnée {C_2}/6 |"+RESET)
    print(BLUE+ f"|============================================|"+RESET)
    print(RED_FLASH+ f'|difficile entre 15 et 25 lettres = 3 {C_3}/5    |'+RESET)
    print(BLUE+"|============================================|"+RESET)
    diff = input()
    os.system('cls')
    if diff == "1" and C_1 !=5 or diff =="2" and C_2 != 6 or diff == "3" and C_3 != 5 :
        mot_a_trouver = level(diff)
        if diff == "1" :
            indice_mot = lev_1.index(mot_a_trouver)
        if diff == "2" : 
            indice_mot = lev_2.index(mot_a_trouver)
        if diff == "3":
            indice_mot = lev_3.index(mot_a_trouver)
        mot_trouver = ["_"]*len(mot_a_trouver)
        mot_a_trouver = list(mot_a_trouver)
        while c_erreur < 10 and mot_a_trouver != mot_trouver:           
            print(f"Les lettres non présentes = {erreur}, nombre d'essaie restant {10 - c_erreur}")
            mot_trouver_1 = ''.join(mot_trouver)
            print(mot_trouver_1,len(mot_trouver_1), "lettres dans le mot")
            pendu(c_erreur, matrice)
            print("proposition n°",c_tent)
            lettre = input(f"Entrez votre lettre  ").lower()
            l = len(lettre)
            os.system("cls")
            if lettre in string.ascii_lowercase or lettre == "-" and l == 1:
                c_erreur,c_tent = boucle(lettre,c_erreur,c_tent)                
            if l != 1 and lettre in string.ascii_lowercase : 
                print("Une seule lettre idiot")
            if lettre not in  string.ascii_lowercase and lettre != "-" : 
                print("On a dit une lettre idiot")
        if mot_a_trouver == mot_trouver : 
            print(vert + "Bravo vous avez gagner en,", c_tent,"tentative" + RESET)
            restart = input(" Une petite der  ? \n rejouer ? oui | non ? ").lower()
            match diff :
                case "1" :  
                    C_1 += 1
                    lev_1.pop(indice_mot)
                case "2" :
                    C_2 += 1 
                    lev_2.pop(indice_mot)
                case "3" : 
                    C_3 += 1 
                    lev_3.pop(indice_mot)
        jeu = again(restart)
        os.system('cls')
        if c_erreur == 10 : 
            pendu(c_erreur,matrice)
            mot_a_trouver = ''.join(mot_a_trouver)
            print(RED_FLASH + f"Perdu le mot etait : {mot_a_trouver}", "et vous avez utilisée ",c_tent,"tentative"+RESET )
            restart = input(" On vas pas terminer sur un echec si ? \n Rejouer ? oui | non ? ").lower() 
            jeu = again(restart)
            os.system('cls')
    if diff != "1" and diff != "2" and diff != "3" :
        print ("On à dit entre 1 et 3 ")
    if diff == "1" and C_1 == 5 or diff == "2" and C_2 == 6 or diff == "3" and C_3 == 5:
        print(f"le niveau {diff} est terminée")
        
   





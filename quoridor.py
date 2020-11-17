#Affiche du damier de jeu

def afficher_damier_ascii(etat):
    """Afficher damier sert à afficher le jeu"""
    joueur1 = etat['joueurs'][0]['nom']
    joueur2 = etat['joueurs'][1]['nom']
    header = f'Légende: 1={joueur1}, 2={joueur2}\n' + ' ' * 3 + '-' * 35
    footer = ('-' * 2 + '|' + '-' * 35 + '\n' + ' ' * 2
              + '|' + '  '.join([f' {i}' for i in range(1, 10)]))

    #création du damier vide
    rangees = ''
    for rangee in range(19, 2, -1):
        if rangee % 2 == 0:
            rangees += ' ' * 2 + '|' + ' ' * 35 + '|\n'
        else:
            rangees += f'{rangee // 2} ' + '|' + ' .  ' * 8 + ' . ' + '|\n'
    rangees = list(rangees)

    #ajout des joueurs
    rangees[-1 * (80 * (etat['joueurs'][0]['pos'][1] - 1)
                  + 40 - etat['joueurs'][0]['pos'][0] * 4)] = '1'
    rangees[-1 * (80 * (etat['joueurs'][1]['pos'][1] - 1)
                  + 40 - etat['joueurs'][1]['pos'][0] * 4)] = '2'

    #Murs horizontaux
    for mur in etat['murs']['horizontaux']:
        rangees[-1 * (80 * (mur[1] - 1) + 1 - mur[0] * 4): - 1
                * (80 * (mur[1] - 1) + 1 - mur[0] * 4) + 7] = ['-' for _ in range(7)]

    #Murs verticaux
    for mur in etat['murs']['verticaux']:
        rangees[-1 * (80 * (mur[1] - 1) + 42 - mur[0] * 4)] = '|'
        rangees[-1 * (80 * (mur[1] - 1) + 82 - mur[0] * 4)] = '|'
        rangees[-1 * (80 * (mur[1] - 1) + 122 - mur[0] * 4)] = '|'

    #affichage
    print(header)
    print(''.join(rangees), end='')
    print(footer)

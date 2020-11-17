import argparse
import api

def analyser_commande():
    """permet d'analyser la commande entrée par le joueur"""

    parser = argparse.ArgumentParser(
        description = "Quoridor - Phase 1"
    )

    parser.add_argument(
        # Argument obligatoire 
        'idul',  help='IDUL du joueur.', type = str
    )

    parser.add_argument(
        #Argument optionel 
        '-p', '--parties',
        help = 'Lister les identifiants de vos 20 dernières parties', action = 'store_true'
    )   

    args = parser.parse_args()
    # permet de retourner les arguments
    return args


if __name__ == "__main__":
    cd = analyser_commande()
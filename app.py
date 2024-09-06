from contact import Contact
from livrecontact import Livrecontact

def menu():
    print("\nBienvenue dans votre annuaire téléphonique!")
    print("Que souhaitez vous faire aujourd'hui ?")
    print("1. Ajouter un nouveau contact")
    print("2. Voir tous les contacts")
    print("3. Chercher un contact")
    print("4. Modifier un contact")
    print("5. Supprimer un contact")
    print("6. Quitter")

def run():
    contacts = Livrecontact()
    contacts.charger_fichier()
    while True:
        menu()
        choix = input("Entrez votre choix : ")

        if choix == "1":
            nom1 = input("Entrer un nom: ")
            email1 = input("Entrer un compte mail: ")
            mobile1 = input("Entrer un numero mobile: ")
            contact = Contact(nom1, email1, mobile1)
            contacts.ajouter(contact)
            print("Contact ajouté avec succès !")
            contacts.sauvegarder()

        elif choix == "2":
            print("Vos contacts:")
            contacts.voir()

        elif choix == '3':
            nom = input("Entrer le nom du contact que vous souhaitez chercher: ")
            contact = contacts.chercher(nom)
            if contact:
                print(f"\nContact : {contact}")
            else:
                print("Contact non trouvé !")

        elif choix == '4':
            nom = input("Entrer le nom du contact que vous souhaitez modifier: ")
            contact = Contact.chercher(nom)

        elif choix == '5':
            nom = input("Entrer le nom du contact que vous souhaitez supprimer: ")
            contacts.supprimer(nom)

        elif choix == '6':
            print("Au revoir ! A bientot")
            break

        else:
            print("Choix non valide , veuillez réessayer!")

if __name__ == "__main__":
    run()
            
from contact import Contact
import json

class Livrecontact:
    def __init__(self):
        self.contacts = []

    def ajouter(self,contact):
        self.contacts.append(contact)

    def voir(self):
        for contact in self.contacts:
            print("Nom: " + contact.nom, "- Email: " + contact.email, "- Mobile: " + contact.mobile)

    def chercher(self, nom):
        for contact in self.contacts:
            if contact.nom.lower() == nom.lower():
                return contact
        return None

    def modifier(self, nom):
        contact = self.chercher(nom)
        if contact:
            print(f"modifier le contact de {nom}")
            nouveau_nom = input(f"Entrer un nouveau nom name ({contact.nom}): ")
            nouveau_email = input(f"Entrer un nouveau nom name ({contact.email}): ")
            nouveau_mobile = input(f"Entrer un nouveau nom name ({contact.mobile}): ")
            contact.nom = nouveau_nom
            contact.email = nouveau_email
            contact.mobile = nouveau_mobile
            print("Contact modifié !")
        else:
            print("Contact non trouvé !")
    
    def supprimer(self, nom):
        contact = self.chercher(nom)
        if contact:
            self.contacts.remove(contact)
            print("Contact supprimé !")
        else:
            print("Contact non trouvé !")

    def sauvegarder(self, fichier="contacts.json"):
        with open(fichier, "w") as fichier:
            json.dump([contact.__dict__ for contact in self.contacts], fichier)
            print(f"Contacts sauvegarder dans {fichier}.")

    def charger_fichier(self, fichier="contacts.json"):
        try:
            with open(fichier, "r") as f:
                contacts_data = json.load(f)
                self.contacts = [Contact(**data) for data in contacts_data]
            print(f"Contacts chargé à partir de {fichier}.")
        except FileNotFoundError:
            print(f"Fichier {fichier} non trouvé !")



# if __name__ == "__main__": 
#     livre_contact = Livrecontact()

#     contact1 = Contact("Mamadou", "mamadou@gmail.com", "123456000")
#     contact2 = Contact("Diakha", "diakha@gmail.com", "123456895")
    
#     livre_contact.ajouter(contact1)
#     livre_contact.ajouter(contact2)
    
#     livre_contact.voir()

#     Chercher = input("tapez le nom du contact que vous souhaitez voir: ")
#     resultat = livre_contact.chercher(Chercher)

#     if resultat:
#         print("Nom: " + resultat.nom, "- Email: " + resultat.email, "- Mobile" + resultat.mobile)
#     else:
#         print("Aucun contact trouvé avec ce nom"

# contact1 = input("Entrez le nom du contact à modifier: ")
# livre_contact.modifier(contact1) 

# suppression = input("Entrer le nom du contact à supprimer")
# livre_contact.supprimer(suppression)# Appel de la méthode modifier() avec le nom

if __name__ == "__main__":
    book = Livrecontact()

    # Load contacts from a file
    book.charger_fichier()

    # Add a contact
    contact1 = Contact("John Doe", "john@example.com", "123")
    book.ajouter(contact1)

    # View contacts
    print("Contacts in the book:")
    book.voir()

    # Save contacts to a file
    book.sauvegarder()
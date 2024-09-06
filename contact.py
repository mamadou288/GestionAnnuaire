class Contact:
    def __init__(self, nom, email, mobile):
        self.nom = nom
        self.email = email
        self.mobile = mobile

    def __str__(self):
        return f"Nom : {self.nom} - Email : {self.email} - mobile : {self.mobile}"

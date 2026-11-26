from models.composant import Composant

class Composite(Composant):

    def __init__(self, id: int, nom: str, description: str, prix: float,
                 nb_ventes: int, image_url: str):
        super().__init__(id, nom, description, prix, nb_ventes, image_url)
        self._enfants: list[Composant] = []
        
        
    
    def ajouter(self, enfant: Composant) -> None:
        self._enfants.append(enfant)

    def retirer(self, enfant: Composant) -> None:
        self._enfants.remove(enfant)

     
    def prix_total(self) -> float:
        return sum(e.prix_total() for e in self._enfants)

  
    def nb_items(self) -> int:
        return sum(e.nb_items() for e in self._enfants)

    
    def est_bundle(self) -> bool:
        return False


        

class Bundle(Composite):
    
    def est_bundle(self) -> bool:
        return True


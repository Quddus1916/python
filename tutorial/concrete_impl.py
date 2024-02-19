class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
        
    def localize(self, msg):
        return self.translations.get(msg)
    

class SpanishLocalizer:
    """it simply returns the spanish version"""
 
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg)
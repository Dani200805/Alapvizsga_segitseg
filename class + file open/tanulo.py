class Tanulo:
    def __init__(self,row: str) -> None:
        # Név	Osztály	Matematika	Magyar	Történelem	Informatika	Angol
        splitted = row.split('\t')
        self.nev = splitted[0]
        self.osztaly = splitted[1]
        self.matek = splitted[2]
        self.magyar = splitted[3]
        self.tori = splitted[4]
        self.info = splitted[5]
        self.angol = splitted[6]




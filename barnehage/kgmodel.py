# kgmodel module

# For å unngå å skrive konstruktører (se [1])
from dataclasses import dataclass

# ----- Definerer modellen ------
"""
Empty DataFrame
Columns: [foresatt_id, foresatt_navn, foresatt_adresse, foresatt_tlfnr, foresatt_pnr]
Index: []
"""
@dataclass
class Foresatt:
    foresatt_id: int
    foresatt_navn: str
    foresatt_adresse: str
    foresatt_tlfnr: str
    foresatt_pnr: str


"""
Empty DataFrame
Columns: [barn_id, barn_pnr]
Index: []
"""
@dataclass
class Barn:
    barn_id : int
    barn_pnr : str
    
"""
Index(['barnehage_id', 'barnehage_navn', 'barnehage_antall_plasser',
       'barnehage_ledige_plasser'],
      dtype='object')
"""
@dataclass
class Barnehage:
    barnehage_id: int
    barnehage_navn: str
    barnehage_antall_plasser: int
    barnehage_ledige_plasser: int
    
"""
Empty DataFrame
Columns: [foresatt_1, foresatt_2, barn_1, fr_barnevern, fr_sykd_familie,
fr_sykd_barn, fr_annet, barnehager_prioritert, sosken__i_barnehagen,
tidspunkt_oppstart, brutto_inntekt]
Index: []
"""
@dataclass
class Soknad:
    sok_id: int
    foresatt_1: Foresatt
    foresatt_2: Foresatt
    barn_1: Barn
    fr_barnevern: str
    fr_sykd_familie: str
    fr_sykd_barn: str
    fr_annet: str
    barnehager_prioritert: str
    sosken__i_barnehagen: str
    tidspunkt_oppstart: str
    brutto_inntekt: int
    svar: str
    
    


"""
Kontrakter:
repr(object) funksjon (kan også bruke !r i utskriftsfunksjoner, f.eks. foresatt_id={foresatt.id!r})
Fra [2]: "Python repr() Function returns a printable representation of an object in Python.
In other words, we can say that the Python repr() function returns a printable
representation of the object by converting that object to a string."

"""

"""
Referanser
[1] https://docs.python.org/3/library/dataclasses.html
[2] https://www.geeksforgeeks.org/python-repr-function/


"""
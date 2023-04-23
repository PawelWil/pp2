# tu teraz robimy sobie 2 importy
# 1. pakietu 'package1', za pomocą importu modułu 1, ale ważne jest to, że nie importujemy funkcji introduce
# (ona zawiera tekst: Jestem fukncją z modułu), ale tylko przy takim sposobie importu zostanie pobrana zawartość pliku '__init__',
#bo nie wywołujemy funkcji, która jest zawarta w module1, czyli funkcji 'introduce'.
# Więc reasumując dostajemy dane z __init__.py:
#####################
# Pakiety są super#
#####################


# 2.Import podpakietu 'subpackage1'. To się robi poprzez ścieżkę, która jest dzielona kropką, czyli:
# from package1.(i teraz po tej kropce podaje jeszcze niższy podpakiet,czyli subpackage1)subpackage1
# i mimo że mamy module 1, to wywołujemy dane tylko z __init__.py,

#czyli wpierw muszę zaimportować pakiet 'package1' - następnie z package1 importuje jego podpakiet, czyli 'subpackage1'
import package1
from package1 import module1
from package1.subpackage1 import module1 as m


# print(dir()) # pokazujemy jak wyswietlamy sobie tą funkcje za pomocą dir - czyli jakie mamy dostępne elementy
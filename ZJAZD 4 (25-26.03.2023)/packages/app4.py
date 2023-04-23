# pakiet może być też pakietem spakowanym/skompresowanym do zipa, również dostępnym poza projktem PyCharm.
# Czyli najeżdzam na ten pakiet 'package2' - prawym myszki - wyslij do zipa, albo skompresuj do zip(tu w zależności od systemu, różnie
# się to może nazywać, jak to kompresować.

# import czegoś z zewnątrz, robimy za pomocą modułu systemowego 'sys' oraz podaniu konkretnej ścieżki, gdzie ten plik się znajduje
import sys

# ta poniższa sciezka, której kopiowanie wytłumaczone jest w app3, musimy dodać jeszcze dokładny adres do tego pakietu,
# czyli '\\package.zip --> czyli podaje adres do konkretnie spakowanego folderu: package2.zip

sys.path.append("C:\\Users\\Dell\\OneDrive\\Desktop\\package2.zip")

from package2 import module1
module1.introduce()
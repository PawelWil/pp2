# TEKS ZADAnIA
#Wyznacz zysk z 3 letniej lokaty bankowej wg założeń:
#• inwestowane środki 46 567,00 zł (own_funds - tak to można nazwać po angielsku)
#• stałe oprocentowanie roczne 7.5%
#• coroczna kapitalizacja odsetek
#• w obliczeniach zastosuj złożony operator przypisania


# Zadanie zrobione przez Pana Marcina

inwestowane_srodki = 46_567.
deposit = inwestowane_srodki
oprocentowanie = 1.075

#inwestowane_srodki = inwestowane_srodki * oprocentowanie
#inwestowane_srodki = inwestowane_srodki * oprocentowanie
#inwestowane_srodki = inwestowane_srodki * oprocentowanie

deposit *= oprocentowanie # tu z wykorzystaniem przypisania
deposit *= oprocentowanie
deposit *= oprocentowanie

print("Zysk z inwesycji wynosi", round(deposit - inwestowane_srodki ,2), "zl.")

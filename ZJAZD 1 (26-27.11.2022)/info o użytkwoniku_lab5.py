name = "Robert"
wiek = 35
city = "Cracow"

print(name, str(wiek), city)


# spróboiwać zrobić z cncatenacją
print ("Mam na imię", name)
print  ("Mam" +" " + str(wiek))
print("pochodzę z " + city + ".")
# KONKATENACJA  - łaczymy tylko string ze stringiem, nie da się mieszać tyów , np string z intiger.
#   Jak jest int to trza dać przed nim string - tak zrobiłem w przypadku zmiennej wiek, która jest równa 35, czyli jest integerem,
# więc trza było z niej zrobić stringa (czyli nie cyfra, ale znaki)
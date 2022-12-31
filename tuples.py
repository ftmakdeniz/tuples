####  Tuples(Demetler) : Sabit liste  ###
## Listelerden farkı DEĞİŞTİRİLEMEZ ##
#Demetlerin ne olduğunu açıklarsak;
# Demetler birden fazla veri türünü bir arada bulundurabilen virgüllerle veya parantez ile gösterilen
# immutable(değiştirilemeyen) veri tipleridir.

#Veri tabanında detaylı inceleyeceğiz. şimdilik kısa bilgi olarak üzerinden geçeceğiz.

"""
sabit_liste = ()  # 1) Boş bir tuple oluşturma yöntemi
sabit_liste2 = tuple()  # 2) Boş bir tuple olşturma yöntemi
"""
tercihler = (1,2,3,4,5,6, "Ali", 2.26, False)
print(tercihler)
for tercih in tercihler:
    print(tercih)

print(tercihler.index("Ali"))
print(tercihler[5])
print(tercihler[tercihler.index("Ali")])

tuple2 = [1,2,[3,4]]
print(tuple2[2][1])
print(len(tercihler))
print(tercihler.count("Mehmet"))

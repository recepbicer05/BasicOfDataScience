# Uygulama - Mülakat Sorusu
# divide_students fonksiyonunu yazınız
# Çift indexte yer alan öğrenciler bir listeye, tek listede olanlar bir listeye gelsin
# Fakat bu iki liste, tek bir liste olarak return olsun

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)

    print(groups)
    return groups

divide_students(students)
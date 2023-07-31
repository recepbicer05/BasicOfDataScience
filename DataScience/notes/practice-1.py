# Uygulama: Mülakat Sorusu
# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
# çift indekstekiler büyümüş, diğerleri küçük kalmış

# sentence = "hi my name is john and i am learning python"

def interview(string):
    new_string = ""
    #girilen stringin indexlerinde geziyoruz
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()

    print(new_string)

interview("hi my name is john and i am learning python")

# with enumerate

def alternative(string):
    alt_string = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            alt_string += letter.upper()
        else:
            alt_string += letter.lower()

    print(alt_string)

alternative("hi my name is john and i am learning python")



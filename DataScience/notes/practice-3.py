# Uygulama - Mülakat Sorusu
# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir
# Keyler orjinal değerler, valuelar ise değiştirilmiş değerler olacak

"""numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

print(new_dict)

print({n: n**2 for n in numbers if n % 2 == 0}) # dict compeheresion ile



# list & dic comprehension uygulamaları
# Bir veri setindeki isimleri değiştirmek

# before ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
#print(df)

for col in df.columns:
    print(col.upper())

A = []

for i in df.columns:
    A.append(i.upper())

print(A)

# list compherension ile
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

print(df.columns)

# Ismınde "INS" olan değişkenlerin başına FLAG diğerlerine N0_FLAG eklemek istiyoruz.

df.columns = (["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns])

print(df.columns)"""


# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
num_cols = [col for col in df.columns if df[col].dtype != "O"] # != "O" ile numeric tip olanları aldık O= objective
soz = {}
agg_list =["mean","min","max","sum"]

for col in num_cols:
    soz[col] = agg_list

print(soz)

#kısa yol

print({col: agg_list for col in num_cols})

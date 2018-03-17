## 2. Sets ##

gender = [legislator[3] for legislator in legislators]
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

col_idx = 6
party = [legislator[col_idx] for legislator in legislators]
party = set(party)
print(party)
print(legislators)

## 4. Missing Values ##

for legislator in legislators:
    gender = legislator[3]
    if gender == "":
        legislator[3] = "M"

## 5. Parsing Birth Years ##

birth_years = []

for legislator in legislators:
    birthday = legislator[2]
    parts = birthday.split('-')
    birth_years.append(parts[0])


## 6. Try/except Blocks ##

try:
    float("hello")
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []

for year in birth_years:
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert Birth Years to Integers ##

for legislator in legislators:
    birth = legislator[2].split('-')
    try:
        birth_year = int(birth[0])
    except Exception:
        birth_year = 0
    legislator.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for legislator in legislators:
    if legislator[7] == 0:
        legislator[7] = last_value
    last_value = legislator[7]
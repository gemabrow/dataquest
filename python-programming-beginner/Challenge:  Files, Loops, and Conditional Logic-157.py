## 3. Read the File Into a String ##

f = open("dq_unisex_names.csv", 'r')
names = f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = names_list[:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for name in names_list:
    comma_list = name.split(',')
    nested_list.append(comma_list)
print(nested_list)

## 6. Convert Numerical Values ##

numerical_list = []
for _list in nested_list:
    uni_name = _list[0]
    num_name = float(_list[1])
    name_list = [uni_name, num_name]
    numerical_list.append(name_list)
print(numerical_list[:5])

## 7. Filter the List ##

thousand_or_greater = []
# The last value is ~100 people
numerical_list[len(numerical_list)-1]
for name_data in numerical_list:
    uni_name, num_name = name_data
    if num_name >= 1000:
        thousand_or_greater.append(uni_name)
print(thousand_or_greater[:10])
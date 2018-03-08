## 1. Opening Files ##

f = open("crime_rates.csv", "r")

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows[:5])

## 5. Practice - Loops ##

ten_rows = rows[0:10]
for row in ten_rows:
    print(row)

## 7. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
final_data = []
for row in rows:
    final_data.append(row.split(','))
print(final_data[:5])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
cities_list = [elem[0] for elem in five_elements]

## 9. Looping Through a List of Lists ##

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
cities_list = [row[0] for row in final_data]

## 10. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

int_crime_rates = []
for elem in rows:
    row = elem.split(',')
    row[1] = int(row[1])
    int_crime_rates.append(row[1])
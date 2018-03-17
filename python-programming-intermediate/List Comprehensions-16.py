## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for idx, ship in enumerate(ships):
    print(ship)
    print(cars[idx])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for idx, row in enumerate(things):
    row.append(trees[idx])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [apple_price * 2 for apple_price in apple_prices]
apple_prices_lowered = [apple_price - 100 for apple_price in apple_prices]

## 5. Counting Female Names ##

name_counts = dict()
idx_gender = 3
idx_year = 7
idx_first = 1

for legislator in legislators:
    gender = legislator[idx_gender]
    year = legislator[idx_year]
    if gender == 'F' and year > 1940:
        name = legislator[idx_first]
        count = name_counts.get(name, 0)
        name_counts[name] = count + 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for value in values:
    check = value is not None and value > 30
    checks.append(check)

## 8. Highest Female Name Count ##

max_value = None

for count in name_counts.values():
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for name, plant_type in plant_types.items():
    print(name)
    print(plant_type)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for name, count in name_counts.items():
    if count == 2:
        top_female_names.append(name)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = dict()

for legislator in legislators:
    gender = legislator[3]
    year = legislator[7]
    if gender == 'M' and year > 1940:
        name = legislator[1]
        count = male_name_counts.get(name, 0)
        male_name_counts[name] = count + 1

highest_male_count = max(male_name_counts.values())

for name, count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)
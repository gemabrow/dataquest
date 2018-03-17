## 2. Array Comparisons ##

countries_canada = world_alcohol[:, 2] == "Canada"
years_1984 = world_alcohol[:, 0] == "1984"

## 3. Selecting Elements ##

# filtering numpy arrays
country_is_algeria = world_alcohol[:,2] == "Algeria"
country_algeria = (world_alcohol[country_is_algeria, :])

## 4. Comparisons with Multiple Conditions ##

# using multiple conditions for dataset filtration
is_algeria_and_1986 = (world_alcohol[:,0] == "1986")  \
                    & (world_alcohol[:,2] == "Algeria")

rows_with_algeria_and_1986 = (world_alcohol[is_algeria_and_1986, :])

## 5. Replacing Values ##

# replacing values in a numpy array
is_1986 = world_alcohol[:, 0] == "1986"
world_alcohol[is_1986,0] = "2014"

is_wine = world_alcohol[:, 3] == "Wine"
world_alcohol[is_wine,3] = "Grog"

## 6. Replacing Empty Strings ##

# initializing all empty year values to 0
is_value_empty = world_alcohol[:, 4] == ''
world_alcohol[is_value_empty,4] = "0"

## 7. Converting Data Types ##

# converting column to floats
alcohol_consumption = world_alcohol[:,4].astype(float)
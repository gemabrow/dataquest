## 1. Introduction ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Wildcards in Regular Expressions ##

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

## 3. Searching the Beginnings And Endings Of Strings ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b....r"

## 5. Reading and Printing the Data Set ##

import csv

f = open("askreddit_2015.csv", 'r')
askreddit_2015_data = csv.reader(f)

posts_with_header = list(askreddit_2015_data)
posts = posts_with_header[1:]

for post in posts[:10]:
    print(post)

## 6. Counting Simple Matches in the Data Set with re() ##

import re

of_reddit_count = 0

for post in posts[:1000]:
    if re.search("of Reddit", post[0]) is not None:
        of_reddit_count += 1

## 7. Using Square Brackets to Match Multiple Characters ##

import re

of_reddit_count_old = 0
of_reddit_count = 0

# include posts with upper or lowercase "Reddit" in count
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count_old += 1
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1

## 8. Escaping Special Characters ##

import re

serious_count = 0

# count the number of posts with tag '[Serious]'
for post in posts:
    if re.search("\[Serious\]", post[0]) is not None:
        serious_count += 1

## 9. Combining Escaped Characters and Multiple Matches ##

import re

serious_count_old = 0
serious_count     = 0

# include posts with lowercase and uppercase tags
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count_old += 1
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count     += 1

## 10. Adding More Complexity to Your Regular Expression ##

import re

serious_count_old = 0
serious_count     = 0

# include posts with tags inside parens for serious_count
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count_old += 1
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_count     += 1

## 11. Combining Multiple Regular Expressions ##

import re

serious_start_count = 0
serious_end_count   = 0
serious_count_final = 0

start_regex = r'^[\[\(][Ss]erious[\]\)]'
end_regex   = r'[\[\(][Ss]erious[\]\)]$'
final_regex = "|".join([start_regex, end_regex])

for post in posts:
    if re.search(start_regex, post[0]) is not None:
        serious_start_count += 1
    if re.search(end_regex, post[0]) is not None:
        serious_end_count += 1
    if re.search(final_regex, post[0]) is not None:
        serious_count_final += 1

## 12. Using Regular Expressions to Substitute Strings ##

import re

repl = "[Serious]"
pattern = r'\([Ss]erious\)|\[serious\]'

for post in posts:
    post[0] = re.sub(pattern, repl, post[0])

## 13. Matching Years with Regular Expressions ##

import re

year_strings = []
for string in strings:
    if re.search('[12][0-9][0-9][0-9]', string):
        year_strings.append(string)

## 14. Repeating Characters in Regular Expressions ##

import re

year_strings = []

for string in strings:
    if re.search('[12][0-9]{3}', string):
        year_strings.append(string)

## 15. Challenge: Extracting all Years ##

import re

# generate all substrings from years_string
# matching years 1000-2999
years = re.findall('[12][0-9]{3}', years_string)
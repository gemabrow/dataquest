## 1. Overview ##

f = open("movie_metadata.csv", 'r')
movie_metadata = f.read()
movie_metadata = movie_metadata.split('\n')
movie_data = []
for element in movie_metadata:
    row = element.split(',')
    movie_data.append(row)
print(movie_data[:5])

## 3. Writing Our Own Functions ##

def first_elts(nested_lists):
    list_heads = []
    for n_list in nested_lists:
        list_heads.append(n_list[0])
    return list_heads

movie_names = first_elts(movie_data)
print(movie_names)

## 4. Functions with Multiple Return Paths ##

def is_usa(movie):
    origin_idx = 6
    return True if movie[origin_idx] == "USA" else False
        
wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
wonder_woman_usa = is_usa(wonder_woman)

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
def index_equals_str(input_lst, index, input_str):
    return input_lst[index] == input_str

wonder_woman_in_color = index_equals_str(wonder_woman, 2, "Color")

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False

def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_lst, index, input_str, header_row=False):
    num_feature = 0
    if header_row == True:
        input_lst = input_lst[1:]
    for row in input_lst:
        num_feature += 1 if row[index] == input_str else 0
    return num_feature

num_of_us_movies = feature_counter(movie_data, 6, "USA", True)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst, index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:]
    for each in input_lst:
        if each[index] == input_str:
            num_elt += 1
    return num_elt

def summary_statistics(input_lst):
    input_lst = input_lst[1:]
    num_japan_films = feature_counter(input_lst, 6, "Japan")
    num_color_films = feature_counter(input_lst, 2, "Color")
    num_films_in_english = feature_counter(input_lst, 5, "English")
    summary_dict = {"japan_films": num_japan_films,
                    "color_films": num_color_films,                 
                    "films_in_english": num_films_in_english}
    return summary_dict

summary = summary_statistics(movie_data)
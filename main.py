from operator import le
import requests

FILM_LIST_PATH = "http://api.themoviedb.org/3/discover/movie"
CREDITS_LIST_PATH = "http://api.themoviedb.org/3/movie"
PERSON_PATH = "http://api.themoviedb.org/3/search/person"
RELEASE_DATE = "2018-01-01"
BACON_ID = "4724"
PAUL_ID = "781"
WHALB_ID = "13240"

API_KEY = "75a267515cba7bac9bb4de32e9e6d42f"


def get_film_list(actor_id):
    params = {"api_key": API_KEY, "with_people": actor_id,
              "primary_release_date.gte": RELEASE_DATE}

    print(FILM_LIST_PATH + "?api_key=" + API_KEY + "&with_people" + actor_id +
          "&primary_release_date.gte=" + RELEASE_DATE)
    r = requests.get(url=FILM_LIST_PATH, params=params)
    data = r.json()
    return data


# end def get_film_list(actor_id):

def data_to_set(data):
    film_set = set()
    for res in data["results"]:  # For each element in results array
        film_set.add(res["title"])  # put film in set
    return film_set


# end def data_to_set(data):

def get_cast_list(film_id):
    url = CREDITS_LIST_PATH + "/" + film_id + "/credits"
    params = {"api_key": API_KEY}
    r = requests.get(url=url, params=params)
    data = r.json()
    return data


# end def get_cast_list(film_id):

def main():
    # bacon_data = get_film_list(BACON_ID)
    # beacon_films = get_film_list(BACON_ID)
    # print("kevin Bacon films since", RELEASE_DATE, ":", bacon_films)

    # get credits data for a film id and take out the cast
    cast = get_cast_list("514593")["cast"]
    person = cast[0]
    print(str(person["id"]) + " " + person["name"])


# def main():


def assignment():
    # Prompt and receive actor's ID from Users. I used names since the User won't know how to get the ID.
    search_input = input(
        "Please enter the first name of two artist to search. \n. Please sepearate names with comma.\n ============================\n")
    search_terms = search_input.split(",", maxsplit=1)

    actor_movies = []

    for term in search_terms:
        r = requests.get(url=PERSON_PATH, params={"query": term, "api_key": API_KEY})
        data = r.json()['results']
        titles = data[0]['known_for']

        movies = [movie_title["original_title"] for movie_title in titles if "original_title" in movie_title]

        actor_movies.append(set(movies))
# Find the common films between two actors.
    same = actor_movies[0].intersection(actor_movies[1])
    if len(same) > 0:
        print(same)
    else:
        print("No current films in common")


if __name__ == "__main__":
    assignment()

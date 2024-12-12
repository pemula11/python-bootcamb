from bs4 import BeautifulSoup
import lxml, requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = (response.text)

soup = BeautifulSoup(web_page, "html.parser")
gallery = soup.find(class_="gallery")

movie_list = gallery.find_all(name="section", class_="gallery__content-item")
movie_title = [movie.find(class_="title").getText() for movie in movie_list]
movies = movie_title[::-1]  # reverse list

print(movies)


with open(f'movieList.txt', 'w') as file:
    for movie in movies:
     file.write(f"{movie.encode('latin1').decode('utf-8')}\n")
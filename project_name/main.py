import requests
from bs4 import BeautifulSoup


class HundredMoviesToWatch:
    def __init__(self):
        self.URL = (
            "https://web.archive.org/web/20200518073855/"
            "https://www.empireonline.com/movies/features/best-movies-2/"
        )

    def make_soup(self):
        rspns = requests.get(self.URL).text
        soup = BeautifulSoup(rspns, "html.parser")
        title_soup = soup.findAll(class_="article-title-description__text")
        return title_soup

    def clean_up_text(self, text, chars):
        for char in chars:
            text = text.replace(char, '')
        return text

    def title_list(self, soup):
        title_list = []
        for title in soup:
            title_list.append(str(title.find(name="h3").get_text()))
        return title_list

    def titles_cleanup(self, titles):
        titles_clean = []
        unwanted_chars = ['\n', '\t', '\xa0', 'â\x80\x93', '\xc3', '©', 'Ã']
        for title in titles:
            title = self.clean_up_text(title, unwanted_chars)
            titles_clean.append(title)
        titles_clean.reverse()
        return titles_clean

    def create_file(self, titles):
        with open("movies.txt", "w") as file:
            for movie in titles:
                file.write(f'{movie}\n')


def main():
    hmtw = HundredMoviesToWatch()
    title_soup = hmtw.make_soup()
    titles = hmtw.title_list(title_soup)
    titles_clean = hmtw.titles_cleanup(titles)
    hmtw.create_file(titles_clean)


if __name__ == '__main__':
    main()

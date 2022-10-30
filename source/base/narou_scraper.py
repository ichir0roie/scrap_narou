import os
import random
import time
from base.constants import *
from bs4 import BeautifulSoup
from urllib import request


class NarouScraper:
    def __init__(self, n_code: str = None) -> None:
        self.target_n_code = n_code
        pass

    def scrap_from_to(self, range_: range):
        for episode in range_:
            print(f"start scraping : {self.target_n_code}/{str(episode)}")
            text = self.get_page_text(episode)
            self.save_text(text, episode)
            time.sleep(random.randint(5, 10))  # this is conscience

    def save_text(self, text: str, episode: int):
        output_path = f"output/scrap/{self.target_n_code}/{int(episode)}.txt"
        os.makedirs("/".join(output_path.split("/")[:-1]), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

    def get_page_text(self, episode: int = 1):
        url = base_url.format(
            n_code=self.target_n_code,
            episode=episode
        )

        req = request.urlopen(url)
        doc = req.read()

        soup = BeautifulSoup(doc, "html.parser")
        main_text = soup.find_all("div", {"id": "novel_honbun"})
        if len(main_text) > 1:
            raise Exception("hit two")
        return main_text[0].text

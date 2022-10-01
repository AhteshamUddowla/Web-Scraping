!pip install requests-html

from requests_html import HTMLSession
session = HTMLSession()

def hadith_book_scraping(url, book_name, total_chapter):
  for i in range(1, total_chapter+1):
    chapter_url = url + book_name + "/chapter/" + str(i)
    r = session.get(chapter_url)
    
    no_pattern = "h3.hidden-print"
    arabic_text_pattern = "p.hadith-des2"
    bangla_text_pattern = ".hadith-des"
    narrator_pattern = ".narrated-by"
    hadith_status_pattern = ".label.validity"

    numbers = [i.text for i in r.html.find(no_pattern)]
    arabic_text = [i.text for i in r.html.find(arabic_text_pattern)]
    bangla_text = [i.text for i in r.html.find(bangla_text_pattern)]
    narrator = [i.text for i in r.html.find(narrator_pattern)]
    hadith_status = [i.text for i in r.html.find(hadith_status_pattern)]

    print("Charter :", i, len(numbers), len(arabic_text), len(bangla_text), len(narrator), len(hadith_status))

    with open(f"{book_name}/{book_name}_chapter_{i}", "w") as f:
      f.write("No., Arabic Text, Bangla Text, Narrator, Hadith Status\n")
      for n, a, b, na, hs in zip(numbers, arabic_text, bangla_text, narrator, hadith_status):
        f.write(f"{n}, {a}, {b}, {na}, {hs}")
        f.write("\n")

url = "http://ihadis.com/books/"
books = {"bukhari":97, "muslim":56, "nasayi":50, "abi-dawud":43, "tirmidi":46, "ibn-majah":37, "muatta-malik":61}
#start_time = time.time()
for book_name, total_chapter in books.items():
  hadith_book_scraping(url, book_name, total_chapter)
#end_time = time.time()
#print(end_time-start_time)
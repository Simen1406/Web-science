import csv
import requests
from bs4 import BeautifulSoup
import spacy

# Loading English model
nlp = spacy.load('en_core_web_sm')
new_link = ["information from next link:" + "\n"]
# Opening downloaded csv file and creating new csv file for output
with open('20230324090000.export.CSV', newline='') as input_file, \
     open ('oblig4_output.csv', 'w', newline='') as output_file:

        # reader and writer for input and output file. since columns in the input file are divided by tab we use delimiter
        csv_reader = csv.reader(input_file, delimiter= '\t')
        csv_writer = csv.writer(output_file, delimiter= ',')
        # writes the column names in the new file
        csv_writer.writerow(['URL', 'Named entities'])

        #Cunter, because it took a lot of time running the code.
        url_counter = 0
        # to check for already visited urls
        visited_url = []
        for row in csv_reader:
            if url_counter > 10:
                print(f"more than 10 urls have been visited ")
                break
            url = row[-1]
            if url in visited_url:
                (print("already visited"))
                continue
            # gives each url 5 sec to open the link. runs an exception if there is something wrong
            try:
                response = requests.get(url, timeout=5)
            except requests.exceptions.RequestException as e:
                print(f"Error while requesting {url}: {e}")
                continue

            soup = BeautifulSoup(response.content, 'html.parser')
            article_text = soup.get_text()

            # Spcay to collect the named entities
            doc = nlp(article_text)
            named_entities = []
            for entity in doc.ents:
                if entity.label_ == 'PERSON' or entity.label_ == 'ORG':
                    named_entities.append(entity.text)

            # writes the collected information into the output file
            csv_writer.writerow([url] + list(named_entities))
            csv_writer.writerow(new_link)
            url_counter += 1
            visited_url.append(url)

print("finished with urls")
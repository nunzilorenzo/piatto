import sys
import csv
import io

from bs4 import BeautifulSoup

#leggo i file csv del menu li decodifico utf

css = open('style.css').read()
csv = csv.DictReader(io.open(sys.argv[1], "r", encoding = "utf-8-sig"))
#####

categories = []
rawItems = []
for item in csv:
    rawItems.append(item)
    category = item["categoria_piatto"]
    if category not in categories:
        categories.append(category)


list = dict()
for category in categories:
    categoryItems = []
    for item in rawItems:
        itemCategory = item["categoria_piatto"]
        if category == itemCategory:
            categoryItems.append(item)
    list[category] = categoryItems

#inserisco su html insieme ai file parsati del menu csv
html = "<style>" + css + "</style>"
html += "<div class=\"menu-body\">"
#da fixare immagine non và

#html += "<img src="/officinadelsolelogo.png>""

for category in categories:
    items = list[category]

    html+= "<div class=\"menu-section\"><h2 class=\"menu-section-title\">" + category + "</h2>"

    for item in items:
        description = item["descrizione_piatto"]
        if item["piatto_vegano"] == "TRUE":
            description += "(Vegano/Vegetariano)"
        if item["piatto_noglutine"] == "TRUE":
            description += "(Senza-Glutine)"


        html += "<div class=\"menu-item\">"

        html += "<div class=\"menu-item-name\">" + item["nome_piatto"] + "</div>"
        html += "<div class=\"menu-item-price\">€" + item["prezzo_piatto"] + "</div>"
        html += "<div class=\"menu-item-description\">" + description + "</div>"

        html += "</div>"


    html += "</div>"

html += "</div>"

soup = BeautifulSoup(html, "html.parser")

html = soup.prettify()


html_file = open(sys.argv[2], "w")
html_file.write(html)

print("menu creato con successo ^__^")

print("")

print("si trova nel file .html sulla stessa cartella")



html_file.close()


 

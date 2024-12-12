
with open('website.html') as f:
    content = f.read()

soup = BeautifulSoup(content, 'lxml')

# print(soup.title)
# print(soup.prettify())
all_anchor_tag = (soup.find_all(name="a"))

# for anchor in all_anchor_tag:
#     print(anchor)

heading = soup.find(name="h1", id='name')
# print(heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)
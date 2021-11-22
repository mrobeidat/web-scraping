import requests
import json
from bs4 import BeautifulSoup as bs

data_url = "https://en.wikipedia.org/wiki/History_of_association_football"

def get_citations_needed_count(url):

    response = requests.get(url)

    b_soup = bs(response.content,'html.parser').find(id = "bodyContent")

    results = b_soup.find_all('a',title="Wikipedia:Citation needed")

    return len(results)




def get_citations_needed_report(url):

    citation_count = []

    res = requests.get(url)      

    bt_soup = bs(res.text,"html.parser").find(id='bodyContent')

    results = bt_soup.find_all('a', title="Wikipedia:Citation needed")

    for result in results:
        citation_count.append(result.parent.parent.parent.text)

    break_point = '\n\n'.join(citation_count)
    return break_point
    
# def get_citations_needed_by_section(self,url):
#     for p in self.results:
#         if p.find('a', title = 'Wikipedia:Citation needed'):
#             text = p.text
#             count_citation = text.count("[citation needed]")
#             

    # json_file = json.dumps(citation_count, indent = 3)
    # with open('scraper.json', 'w') as f:
    #  f.write(json_file)

  
    

print(f"\n\n The number of needed citations is : {get_citations_needed_count(data_url)} \n\n")

print(f"\n Data need citation : \n\n {get_citations_needed_report(data_url)}\n\n")

# print(f"\n Data  : \n\n {get_citations_needed_by_section(data_url)}\n\n")

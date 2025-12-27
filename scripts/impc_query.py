import requests
import json 
import os 


#Base IMPC solr endpoint 

BASE_URL = "https://www.ebi.ac.uk/mi/impc/solr/genotype-phenotype/select"

#Example gene

GENE = "Mbp"
params = {
    "q": f"marker_symbol:{GENE}",
    "rows": 10, #small for exploration
    "wt":"json"
}
response = requests.get(BASE_URL, params=params)
data = response.json()

#save raw JSON 
os.makdirs("../data/raw", exist_ok =True)
with open(f"/data/raw/{GENE}_phenotypes.json", "w") as f:
    json.dump(data, f, indent=2)

    #inspect first hit
    first_hit = data["response"] ["docs"][0]
    print("Available fields:", first_hit.keys())
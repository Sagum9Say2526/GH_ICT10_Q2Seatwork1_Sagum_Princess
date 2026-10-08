
from pyscript import document

nicknames = {
    "brunei": "The Abode of Peace",
    "cambodia": "The Kingdom of Wonder",
    "indonesia": "The Emerald of the Equator",
    "laos": "The Land of a Million Elephants",
    "malaysia": "The Golden Peninsula",
    "myanmar": "The Golden Land",
    "philippines": "The Pearl of the Orient Seas",
    "singapore": "The Lion City",
    "thailand": "The Land of Smiles",
    "timor-leste": "The Land of the Rising Sun",
    "vietnam": "The Land of the Blue Dragon"
}

def nickname(event=None):
    country = document.getElementById("country").value.lower().strip()

    if country in nicknames:
        document.getElementById("result").innerText = nicknames[country]
    else:
        document.getElementById("result").innerText = "Country not identified."

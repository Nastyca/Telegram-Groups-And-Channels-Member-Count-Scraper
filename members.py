import random
import requests
import concurrent.futures
from bs4 import BeautifulSoup
from colorama import Fore, init

INPUT_FILE = "groupes.txt"
OUTPUT_FILE = "groupes_100+.txt"
        
liste_proxies = [
    "be-bru-wg-socks5-103.relays.mullvad.net:1080",
    "be-bru-wg-socks5-101.relays.mullvad.net:1080",
    "fr-par-wg-socks5-004.relays.mullvad.net:1080",
    "fr-mrs-wg-socks5-001.relays.mullvad.net:1080",
    "fr-par-wg-socks5-002.relays.mullvad.net:1080",
    "fr-par-wg-socks5-005.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-404.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-202.relays.mullvad.net:1080",
    "de-ber-wg-socks5-003.relays.mullvad.net:1080",
    "de-ber-wg-socks5-002.relays.mullvad.net:1080",
    "de-dus-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-501.relays.mullvad.net:1080",
    "de-fra-wg-socks5-004.relays.mullvad.net:1080",
    "fr-par-wg-socks5-101.relays.mullvad.net:1080",
    "fr-par-wg-socks5-102.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-002.relays.mullvad.net:1080",
    "de-dus-wg-socks5-002.relays.mullvad.net:1080",
    "fr-par-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-505.relays.mullvad.net:1080",
    "de-ber-wg-socks5-005.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-201.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-503.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-506.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-003.relays.mullvad.net:1080",
    "de-fra-wg-socks5-001.relays.mullvad.net:1080",
    "de-fra-wg-socks5-006.relays.mullvad.net:1080",
    "de-fra-wg-socks5-008.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-401.relays.mullvad.net:1080",
    "de-dus-wg-socks5-003.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-004.relays.mullvad.net:1080",
    "de-fra-wg-socks5-005.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-502.relays.mullvad.net:1080",
    "de-fra-wg-socks5-101.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-507.relays.mullvad.net:1080",
    "de-fra-wg-socks5-103.relays.mullvad.net:1080",
    "us-nyc-wg-socks5-605.relays.mullvad.net:1080",
    "de-fra-wg-socks5-403.relays.mullvad.net:1080",
    "de-fra-wg-socks5-402.relays.mullvad.net:1080",
    "be-bru-wg-socks5-102.relays.mullvad.net:1080",
    "de-fra-wg-socks5-304.relays.mullvad.net:1080",
    "de-fra-wg-socks5-302.relays.mullvad.net:1080",
    "de-fra-wg-socks5-401.relays.mullvad.net:1080",
    "de-fra-wg-socks5-301.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-403.relays.mullvad.net:1080",
    "de-fra-wg-socks5-007.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-504.relays.mullvad.net:1080",
    "fr-par-wg-socks5-003.relays.mullvad.net:1080",
    "de-fra-wg-socks5-303.relays.mullvad.net:1080",
    "at-vie-wg-socks5-001.relays.mullvad.net:1080",
    "be-bru-wg-socks5-101.relays.mullvad.net:1080",
    "at-vie-wg-socks5-003.relays.mullvad.net:1080",
    "bg-sof-wg-socks5-002.relays.mullvad.net:1080",
    "fr-par-wg-socks5-004.relays.mullvad.net:1080",
    "ca-mtr-wg-socks5-001.relays.mullvad.net:1080",
    "ca-mtr-wg-socks5-003.relays.mullvad.net:1080",
    "sk-bts-wg-socks5-001.relays.mullvad.net:1080",
    "fi-hel-wg-socks5-103.relays.mullvad.net:1080",
    "rs-beg-wg-socks5-102.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-001.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-001.relays.mullvad.net:1080",
    "au-adl-wg-socks5-302.relays.mullvad.net:1080",
    "se-mma-wg-socks5-002.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-404.relays.mullvad.net:1080",
    "de-ber-wg-socks5-002.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-202.relays.mullvad.net:1080",
    "ro-buh-wg-socks5-002.relays.mullvad.net:1080",
    "se-mma-wg-socks5-102.relays.mullvad.net:1080",
    "se-mma-wg-socks5-003.relays.mullvad.net:1080",
    "no-osl-wg-socks5-002.relays.mullvad.net:1080",
    "se-got-wg-socks5-101.relays.mullvad.net:1080",
    "au-syd-wg-socks5-002.relays.mullvad.net:1080",
    "fr-par-wg-socks5-102.relays.mullvad.net:1080",
    "de-fra-wg-socks5-004.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-102.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-105.relays.mullvad.net:1080",
    "au-bne-wg-socks5-302.relays.mullvad.net:1080",
    "no-svg-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-002.relays.mullvad.net:1080",
    "de-dus-wg-socks5-002.relays.mullvad.net:1080",
    "fi-hel-wg-socks5-102.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-505.relays.mullvad.net:1080",
    "au-syd-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-201.relays.mullvad.net:1080",
    "se-sto-wg-socks5-005.relays.mullvad.net:1080",
    "de-ber-wg-socks5-005.relays.mullvad.net:1080",
    "mk-skp-wg-socks5-001.relays.mullvad.net:1080",
    "pl-waw-wg-socks5-102.relays.mullvad.net:1080",
    "se-sto-wg-socks5-009.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-103.relays.mullvad.net:1080",
    "ee-tll-wg-socks5-002.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-503.relays.mullvad.net:1080",
    "lu-lux-wg-socks5-001.relays.mullvad.net:1080",
    "se-sto-wg-socks5-004.relays.mullvad.net:1080",
    "se-got-wg-socks5-003.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-003.relays.mullvad.net:1080",
    "us-uyk-wg-socks5-102.relays.mullvad.net:1080",
    "hr-zag-wg-socks5-001.relays.mullvad.net:1080",
    "fi-hel-wg-socks5-001.relays.mullvad.net:1080",
    "de-fra-wg-socks5-001.relays.mullvad.net:1080",
    "de-fra-wg-socks5-008.relays.mullvad.net:1080",
    "no-svg-wg-socks5-003.relays.mullvad.net:1080",
    "de-dus-wg-socks5-003.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-104.relays.mullvad.net:1080",
    "se-sto-wg-socks5-001.relays.mullvad.net:1080",
    "pl-waw-wg-socks5-101.relays.mullvad.net:1080",
    "se-sto-wg-socks5-002.relays.mullvad.net:1080",
    "no-osl-wg-socks5-004.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-004.relays.mullvad.net:1080",
    "pl-waw-wg-socks5-201.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-502.relays.mullvad.net:1080",
    "se-sto-wg-socks5-012.relays.mullvad.net:1080",
    "de-fra-wg-socks5-101.relays.mullvad.net:1080",
    "gb-lon-wg-socks5-302.relays.mullvad.net:1080",
    "ee-tll-wg-socks5-003.relays.mullvad.net:1080",
    "nl-ams-wg-socks5-005.relays.mullvad.net:1080",
    "no-osl-wg-socks5-001.relays.mullvad.net:1080",
    "pt-lis-wg-socks5-101.relays.mullvad.net:1080",
    "gb-lon-wg-socks5-001.relays.mullvad.net:1080",
    "gb-lon-wg-socks5-004.relays.mullvad.net:1080",
    "br-sao-wg-socks5-001.relays.mullvad.net:1080",
    "hr-zag-wg-socks5-002.relays.mullvad.net:1080",
    "nl-ams-wg-socks5-201.relays.mullvad.net:1080",
    "no-svg-wg-socks5-002.relays.mullvad.net:1080",
    "ua-iev-wg-socks5-002.relays.mullvad.net:1080",
    "gb-mnc-wg-socks5-007.relays.mullvad.net:1080",
    "nl-ams-wg-socks5-006.relays.mullvad.net:1080",
    "us-rag-wg-socks5-105.relays.mullvad.net:1080",
    "cz-prg-wg-socks5-102.relays.mullvad.net:1080",
    "us-uyk-wg-socks5-103.relays.mullvad.net:1080",
    "de-fra-wg-socks5-106.relays.mullvad.net:1080",
    "gb-mnc-wg-socks5-005.relays.mullvad.net:1080",
    "us-nyc-wg-socks5-503.relays.mullvad.net:1080",
    "gb-mnc-wg-socks5-006.relays.mullvad.net:1080",
    "us-qas-wg-socks5-002.relays.mullvad.net:1080",
    "se-sto-wg-socks5-011.relays.mullvad.net:1080",
    "gb-lon-wg-socks5-203.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-507.relays.mullvad.net:1080",
    "us-atl-wg-socks5-202.relays.mullvad.net:1080",
    "us-rag-wg-socks5-102.relays.mullvad.net:1080",
    "us-chi-wg-socks5-002.relays.mullvad.net:1080",
    "de-fra-wg-socks5-103.relays.mullvad.net:1080",
    "us-nyc-wg-socks5-605.relays.mullvad.net:1080",
    "ro-buh-wg-socks5-001.relays.mullvad.net:1080",
]

def obtenir_proxy():
    proxy = random.choice(liste_proxies)
    return {
        "http": f"socks5://{proxy}",
        "https": f"socks5://{proxy}"
    }

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

def telegram(groupe):
    tentatives = 0
    max = 5
    succes = False

    while not succes and tentatives < max:
        try:
            tentatives += 1
            proxy = obtenir_proxy()
            tentatives += 1
            proxy = obtenir_proxy()
            requete = requests.get(f"https://t.me/{groupe}", headers=headers, proxies=proxy, timeout=5)
            requete.raise_for_status()
                
            soup = BeautifulSoup(requete.text, "html.parser")

            membres__ = soup.find("div", class_="tgme_page_extra")
            membres_ = membres__.get_text(strip=True)
            membres = membres_.split(' members')[0].replace(' ', '')
            en_ligne = membres_.split(' members, ')[1].split(' online')[0]

            print(f"{Fore.GREEN}Groupe : {Fore.RESET}{groupe} {Fore.BLUE}| {Fore.GREEN}Membres : {Fore.RESET}{membres} {Fore.BLUE}| {Fore.GREEN}En ligne : {Fore.RESET}{en_ligne}")

            with open(OUTPUT_FILE, "a") as ff:
                ff.write(f"{groupe}\n")

            succes = True
        except:
            pass
            if tentatives >= max:
                pass

with open(INPUT_FILE, "r") as f:
    lignes = f.read().splitlines()

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(telegram, lignes)

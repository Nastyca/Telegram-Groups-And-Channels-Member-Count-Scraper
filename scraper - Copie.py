import os
import json
import time
import ctypes
import random
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch, Channel, Chat
from telethon.errors import ChatAdminRequiredError
from colorama import Fore
from socks import SOCKS5
from sys import stdout

api_id = ''
api_hash = ''
phone_number = ''

#-

b = Fore.WHITE
v = Fore.GREEN
r = Fore.RESET

nombre = 0
groupes = 0
numeros = 0

proxies = [
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

selected_proxy = random.choice(proxies)
proxy_addr, proxy_port = selected_proxy.split(':')
proxy_type = 'socks5'
client = TelegramClient('session_name', api_id, api_hash, proxy=(proxy_type, proxy_addr, int(proxy_port)))

async def main():
    global nombre, groupes, numeros
    await client.start(phone=phone_number)

    with open('groupes.txt', 'r', encoding='utf-8') as file:
        group_names = [line.strip() for line in file.readlines()]

    for group_name in group_names:
        groupes += 1
        print(f"\n{r}----------------------------------------------------------------------")
        print(f"{Fore.BLUE}Groupe : {r}{group_name}")

        try:
            group = await client.get_entity(group_name)

            if not isinstance(group, (Channel, Chat)):
                print(f"{Fore.RED}[!] Type de groupe inconnu. Ignoré.{r}")
                continue

            users_data = []
            offset = 0
            limit = 200

            while True:
                participants = await client(GetParticipantsRequest(
                    group,
                    ChannelParticipantsSearch(''),
                    offset=offset,
                    limit=limit,
                    hash=0
                ))

                users = getattr(participants, 'users', getattr(participants, 'participants', []))
                if not users:
                    break

                for user in users:
                    users_data.append({
                        "id": user.id,
                        "username": user.username or "N/A",
                        "phone": user.phone or "N/A",
                        "first_name": user.first_name or "N/A",
                        "last_name": user.last_name or "N/A",
                        "bio": user.bot_info_version or "N/A",
                        "status": str(user.status) or "N/A",
                        "lang_code": user.lang_code or "N/A"
                    })

                    print(f"{v}[{b}ID : {user.id}{v}] {b}> {v}[{b}Pseudo : {user.username or 'N/A'}{v}] {b}> {v}[{b}Numéro : {user.phone or 'N/A'}{v}]{r}")

                    if not user.phone:
                        pass
                    else:
                        numeros += 1

                    nombre += 1

                offset += limit

            filename = f"data/{group_name.replace(' ', '_').replace('/', '_')}.json"
            os.makedirs("data", exist_ok=True)
            with open(filename, 'w', encoding='utf-8') as f:
                for user in users_data:
                    json.dump(user, f, ensure_ascii=False)
                    f.write(',\n')

            print(f"\n{v}[+] Données sauvegardées dans -> {r}{filename}")
            print(f"{Fore.CYAN}[i] Total des membres : {r}{len(users_data)}")
            ctypes.windll.kernel32.SetConsoleTitleW(f"Groupes : {groupes} | Utilisateurs : {nombre} | Numéros : {numeros}")

        except ChatAdminRequiredError:
            print(f"{Fore.YELLOW}[!] Pas de privilèges : {r}{group_name}")
        except Exception as e:
            print(f"{Fore.RED}[-] Erreur ({group_name}) : {r}{e}")

        time.sleep(1)

with client:
    client.loop.run_until_complete(main())

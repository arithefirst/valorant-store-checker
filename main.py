import asyncio
import sys
import requests
import riot_auth
import os
from dotenv import load_dotenv

load_dotenv()
UNAME = os.getenv("USERNAME")
PASSWD = os.getenv("PASSWORD")
WEHBOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
CREDS = UNAME, PASSWD

riot_auth.RiotAuth.RIOT_CLIENT_USER_AGENT = f"RiotClient/{requests.get('https://valorant-api.com/v1/version').json()['data']['riotClientBuild']} %s (Windows;10;;Professional, x64)"
print(f'Using User Agent "{riot_auth.RiotAuth.RIOT_CLIENT_USER_AGENT}"')
print("Getting Tokens....")
auth = riot_auth.RiotAuth()
asyncio.run(auth.authorize(*CREDS))

print(f"Access Token Type: {auth.token_type}\n")
print(f"Access Token: {auth.access_token}\n")
print(f"Entitlements Token: {auth.entitlements_token}\n")
print(f"User ID: {auth.user_id}")

# Reauth using cookies. Returns a bool indicating whether the reauth attempt was successful.
asyncio.run(auth.reauthorize())

headers = {
    'Authorization': f'{auth.token_type} {auth.access_token}',
    'X-Riot-ClientPlatform': 'ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9',
    'X-Riot-ClientVersion': f'{requests.get("https://valorant-api.com/v1/version").json()["data"]["riotClientVersion"]}',
    'X-Riot-Entitlements-JWT': f'{auth.entitlements_token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}

response = requests.get(f"https://pd.na.a.pvp.net/store/v2/storefront/{auth.user_id}", headers=headers)

shop_items = [0,1,2,3]

for i in shop_items:
    itemdata = requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{response.json()["SkinsPanelLayout"]["SingleItemOffers"][i]}")
    print(f'Got data for {itemdata.json()["data"]["displayName"]}')

    # Set Data for Webhook
    webhook_data = {
        "embeds": [
            {
            "title": f'{itemdata.json()["data"]["displayName"]} - {response.json()["SkinsPanelLayout"]["SingleItemStoreOffers"][i]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]}VP',
            "color": 13346551,
            "author": {
                "name": "arithefirst 2024",
                "url": "https://arithefirst.com",
                "icon_url": "https://arithefirst.com/images/pfp.png"
            },
            "image": {
                "url": f'{itemdata.json()["data"]["displayIcon"]}'
            }
            }
        ],
        "attachments": []
    }

    # Send Webhook
    print('Sending Webhook....')

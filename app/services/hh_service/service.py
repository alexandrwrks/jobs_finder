import asyncio

import httpx

from app.utils.settings import settings


CODE = "Q6F91PQNSETA86CNBTQE2OAUA1UMJ781JQLQD240PIRCH7LA4EVSFA285BL8B7UQ"

MAIN_URL = (
    "https://hh.ru/oauth/authorize?response_type=code&client_id=V1QO6KKP0496KHGAT6RAEJQA084FSGLK81CHFDKE3DC9LQSIEOVJ2SGODSAR85FJ&redirect_uri=http://localhost:8000/callback")


class HHService:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client
        self.CLIENT_ID = settings.CLIENT_ID
        self.CLIENT_SECRET = settings.CLIENT_SECRET
        self.BASE_API = "https://api.hh.ru/"
        self.BASE_AUTH = "https://hh.ru/"
        self.CODE = "K2GMNBFDEHSOMTAUH289JBF6SONL55EQDTDMVSTKPEBSPM9EMDCT9ORD9C3KJMH8"

    def _headers(self, access_token: str):
        return {
            "Authorization": f"Bearer {access_token}",
            "HH-User-Agent": "Jobs Finder Telegram Bot/1.0 (alexandrwrks@gmail.com)"
        }

    async def me(self, access_token: str):
        response = await self.client.get(
            url=f"{self.BASE_API}me",
            headers=self._headers(access_token)
        )
        response.raise_for_status()
        print(response.json())

    async def update_access_token(self, refresh_token: str):
        response = await self.client.post(
            url=f"{self.BASE_AUTH}oauth/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
                "client_id": self.CLIENT_ID,
                "client_secret": self.CLIENT_SECRET,
            }
        )
        response.raise_for_status()
        print(response.json())

    async def get_vacancies(self, access_token: str):
        response = await self.client.get(
            url="https://api.hh.ru/vacancies",
            params={
                "text": "Python",
                "per_page": 50,
            },
            headers=self._headers(access_token)
        )
        if response.status_code != 200:
            print(response.status_code)
            print(response.json())
            return

        print(response.json())

    async def func(self):
        response = await self.client.post(
            url=f"{self.BASE_AUTH}oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": self.CLIENT_ID,
                "client_secret": self.CLIENT_SECRET,
                "code": self.CODE,
                "redirect_uri": "http://localhost:8000/callback",
            },
        )
        response.raise_for_status()

        print(response.json())
        # await self.me(response.json()["access_token"])
        # await self.get_vacancies(response.json()["access_token"])

async def main():
    async with httpx.AsyncClient() as client:
        hh_service = HHService(client)
        # refresh_token USERVT8U675U6I1TF2H5RD65J7PIGC4RNA90NMA42N9UK7NUMQFPCU9RNQ3CKBQJ
        await hh_service.get_vacancies(access_token="USERIC122E9NG7SEOOAL7ET951JUARSD0Q3T9RVAHDOT5UN6NL5TDNDJRPF0DD88")

if __name__ == "__main__":
    asyncio.run(main())
from bs4 import BeautifulSoup
from httpx import AsyncClient

from bot.html_parser import html_to_telegram
from bot.main import bot


async def job_info(link: str, client: AsyncClient):
    try:
        response = await client.get(url=link)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        description_div = soup.find("div", class_="article-body")
        clean_description = html_to_telegram(str(description_div))

        text = (
            f"{clean_description}\n"
            f"<a href='{link}'>"
            f"Открыть вакансию:"
            f"</a>"
        )

        try:
            await bot.send_message(
                chat_id=1918881124,
                text=text,
                parse_mode="HTML",
            )

        except Exception as e:
            print(str(e))

    except Exception as e:
        print(str(e))
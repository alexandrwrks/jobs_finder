import asyncio

from httpx import AsyncClient

from bot.html_parser import html_to_telegram
from utils.bot_settings import bot
from perfectly_parsers.perfectly_job import job_info

async def send_job_info_to_telegram(link: str, telegram_id: int, client: AsyncClient) -> None:
    try:
        info_of_job = await job_info(
            link=link,
            client=client,
        )

        salary = None
        if info_of_job.salary:
            salary = (
                f"{info_of_job.salary.min_value} - {info_of_job.salary.max_value} "
                f"{info_of_job.salary.currency}"
                # / {info_of_job.salary.unit}"
            )

        # description = html_to_telegram(info_of_job.job.description)
        # if len(description) > 500:
        #     description = description[:500] + "..."

        busyness = None
        if isinstance(info_of_job.job.busyness, list):
            busyness = ", ".join(info_of_job.job.busyness)
        elif isinstance(info_of_job.job.busyness, str):
            busyness = info_of_job.job.busyness

        text = (
            f"💼 {info_of_job.job.title}\n\n"
            f"🏢 Компания: {info_of_job.company.name or "Не указана"}\n"
            f"📍 Локация: {busyness or "Не указана"}\n"
            f"💻 Формат: {info_of_job.job.location_work}\n"
            f"🕒 Тип занятости: {info_of_job.job.type_of_work if info_of_job.job.type_of_work is not None else "Не указано"}\n"
            f"💰 Зарплата\n{salary if salary else "Не указана"}\n\n"
            f"🛠 Навыки\n{", ".join(info_of_job.skills) if info_of_job.skills else ""}\n\n"
            # f"📄 Описание\n{description}\n\n"
            f"🔗<a href='{info_of_job.job.url}'>Открыть вакансию</a>"
        )

        await bot.send_message(
            chat_id=telegram_id,
            text=text,
            parse_mode="HTML",
        )

    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":
    asyncio.run(send_job_info_to_telegram("https://talanto.work/jobs/972ec5de-9635-4b55-9f46-6a665144d5c8", None))
import asyncio
from playwright.async_api import async_playwright


async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://localhost:8000")

        assert 'Congratulations!' in await page.title(), await page.title()


asyncio.run(test())
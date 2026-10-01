# Rigenera i PDF delle presentazioni · Regenerates the presentation PDFs
#
#   python esporta-pdf.py                                  -> tutte le presentazioni / all presentations
#   python esporta-pdf.py presentazione-classe-IT.html     -> una sola / just one
#
# Requisiti / Requirements: pip install playwright  &&  playwright install chromium
# I PDF vengono salvati nella cartella pdf/ · PDFs are saved in the pdf/ folder.
import asyncio
import glob
import os
import sys

from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pdf")


async def export(browser, name):
    page = await browser.new_page(viewport={"width": 1280, "height": 720})
    await page.goto("file://" + os.path.join(HERE, name))
    await page.evaluate("document.fonts.ready")
    await page.wait_for_timeout(400)
    target = os.path.join(OUT, os.path.splitext(name)[0] + ".pdf")
    await page.pdf(path=target, width="1280px", height="720px", print_background=True,
                   margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    await page.close()
    print("Creato / Created:", os.path.relpath(target, HERE))


async def main():
    names = sys.argv[1:] or sorted(os.path.basename(p) for p in glob.glob(os.path.join(HERE, "presentazione-classe-*.html")))
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name in names:
            await export(browser, name)
        await browser.close()


asyncio.run(main())

import markdown
import asyncio
from playwright.async_api import async_playwright
import os

with open("entrega_tp1.md", "r", encoding="utf-8") as f:
    text = f.read()

html = markdown.markdown(text, extensions=['fenced_code', 'tables'])

css = """
<style>
body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; padding: 20px; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; }
h1, h2, h3 { border-bottom: 1px solid #ddd; padding-bottom: 5px; color: #111; }
code { background-color: #f4f4f4; padding: 2px 4px; border-radius: 4px; font-family: 'Courier New', Courier, monospace; }
pre code { background-color: transparent; padding: 0; }
pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; font-family: 'Courier New', Courier, monospace; }
img { max-width: 100%; border: 1px solid #ddd; border-radius: 4px; margin-top: 10px; }
blockquote { border-left: 4px solid #ccc; padding-left: 10px; color: #666; margin-left: 0; }
</style>
"""

full_html = f"<html><head><meta charset='utf-8'>{css}</head><body>{html}</body></html>"

with open("temp.html", "w", encoding="utf-8") as f:
    f.write(full_html)

async def convert_to_pdf():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_path = "file:///" + os.path.abspath("temp.html").replace('\\', '/')
        await page.goto(file_path)
        import time
        time.sleep(1)
        await page.pdf(path="Entrega_TP1.pdf", format="A4", print_background=True, margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"})
        await browser.close()

asyncio.run(convert_to_pdf())

if os.path.exists("temp.html"):
    os.remove("temp.html")
print("PDF generado con exito en Entrega_TP1.pdf")

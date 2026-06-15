from playwright.sync_api import sync_playwright
import os


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("screenshots", exist_ok=True)
        screenshot_name = scenario.name.replace(" ", "_").lower()
        context.page.screenshot(path=f"screenshots/{screenshot_name}.png")

    context.page.close()
    context.browser.close()
    context.playwright.stop()
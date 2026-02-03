from pytest_playwright.pytest_playwright import browser
from playwright.sync_api import Page

#! way to create context, browser and page ( use this in customer requirement)
def test_plawyrightBasics(playwright):
        browser = playwright.chromium.launch(headless=False) # Initiate the browser
        context = browser.new_context() # Create a context fresh one
        page = context.new_page() # creating a page
        page.goto("https://www.google.com") # navigating
        print("Navigating to Google...")


# playwright shortcut
def test_playwrightBasicsShortcut(page:Page):
        page.goto("https://www.google.com")
        print("Navigating to Google...")



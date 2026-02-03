from pytest_playwright.pytest_playwright import browser


#! way to create context, browser and page
def test_plawyrightBasics(playwright):
        browser = playwright.chromium.launch(headless=False) # Initiate the browser
        context = browser.new_context() # Create a context fresh one
        page = context.new_page() # creating a page
        page.goto("https://www.google.com") # navigating
        print("Navigating to Google...")



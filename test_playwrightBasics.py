from pytest_playwright.pytest_playwright import browser
from playwright.sync_api import Page, expect,Playwright


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


#locators in playwright
# css selectors --> if id then use #id and class then use .className
def test_coreLocators(page:Page):
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        print("Navigating to Rahul shetty academy...")
        print("Filling Username...")
        page.get_by_label("username").fill("Hitesh")
        print("Filling Password...")
        page.get_by_label("password").fill("Learning")
        page.get_by_role("combobox").select_option("consult") # combobox is for select class and option is the value from HTML
        page.locator("#terms").check() #--> To just check the checkbox
        page.get_by_role("button",name="Sign In").click()
        expect(page.get_by_text("Incorrect username/password.")).to_be_visible()



def test_firefoxbrowser(playwright : Playwright):
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com")

from playwright.sync_api import Page
# check the price of rice is equal to 37
# identify the price column
#identify the rice column
# extract the price


# my solution

def test_webTables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    with (page.expect_popup() as newPageDeals):   # stating that we might have a new window or page
        page.get_by_text("Top Deals").click() # using same page fixture we are clicking on deals, that will open new window
        dealsPage= newPageDeals.value # getting that new page value into new page value
        dealsPage.wait_for_timeout(2000)
        for index in range(dealsPage.locator("th").count()):
            if dealsPage.locator("th").nth(index).filter(has_text="Price").count()>0:
                colVal =index
                print(f"Price columne Value is : {colVal}")
                break
        riceRow = dealsPage.locator("tr").filter(has_text="Rice")
        priceVal = riceRow.locator("td").nth(colVal).text_content()
        assert priceVal =='37'
#mouseHover

def test_mouseHover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()

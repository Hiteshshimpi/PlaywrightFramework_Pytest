from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from apiBase import ApiUtils


def test_e2e_web_api(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context =browser.new_context()
    page =context.new_page()

    #create order - orderId
    api_Utils = ApiUtils() # creating object of that class
    responseody = api_Utils.createOrder(playwright)
    orderId = responseody["orders"][0]
    print(orderId)

    # login to verify the order=
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("hiteshshi@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("LearnApi@123")
    page.locator("#login").click()
    page.wait_for_timeout(2000)

    #goit to order history page and check it the order id present or not
    page.locator("//*[contains(@class,'btn-custom')]//i[contains(@class,'fa-handshake-o')]").click()
    page.wait_for_timeout(1000)

    # now check if the order is present or not
    orderIdColum = page.locator("//tbody//tr").filter(has_text=orderId)
    orderIdColum.get_by_role("button",name="View").click()
    page.wait_for_timeout(1000)
    print(f"Order id for new order is : {orderIdColum}")
    expect(page.locator("p").filter(has_text="Thank you for Shopping With Us")).to_be_visible()








from playwright.sync_api import Page,Playwright ,expect

import apiBase


#Login with correct credentails and add Item to cart

def  test_login(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("hiteshshi@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("LearnApi@123")
    page.locator("#login").click()
    page.wait_for_timeout(2000)
    productList =page.locator(".card-body").nth(1)
    productList.get_by_role("button", name=" Add To Cart").click()
    page.wait_for_timeout(3000)
    page.locator("//*[contains(@class,'btn-custom')]//i[contains(@class,'fa-shopping-cart')]").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button",name="Checkout").click()
    page.get_by_placeholder("Select Country").type("INDIA",delay=200)
    page.wait_for_timeout(1000)
    countrySelect = page.locator("//*[contains(@class,'list-group-item')]")
    countrySelect.locator("span").nth(1).click()
    page.wait_for_timeout(1000)
    page.locator("a").filter(has_text="Place Order ").click()
    page.wait_for_timeout(3000)

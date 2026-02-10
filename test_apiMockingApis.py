import pytest
from playwright.sync_api import Page, Playwright

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

# api call from broswer -> api call contact with server and returns back response -> browsewr use the response to generate html
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69875355dc40b48f32c4e1sfd9a")


def test_Network1(page:Page):

    # login to verify the order=
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    # Routing provides the capability to modify network requests that are made by a page.
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)

    page.get_by_placeholder("email@example.com").fill("hiteshshi@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("LearnApi@123")
    page.locator("#login").click()
    page.wait_for_timeout(2000)
    # goit to order history page and check it the order id present or not
    page.locator("//*[contains(@class,'btn-custom')]//i[contains(@class,'fa-handshake-o')]").click()
    page.wait_for_timeout(1000)
    noOrderMessage =page.locator(".mt-4").text_content()
    print(noOrderMessage)

def  test_Network2(page:Page):
    # login to verify the order=
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)
    page.get_by_placeholder("email@example.com").fill("hiteshshi@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("LearnApi@123")
    page.locator("#login").click()
    page.wait_for_timeout(2000)
    # goit to order history page and check it the order id present or not
    page.locator("//*[contains(@class,'btn-custom')]//i[contains(@class,'fa-handshake-o')]").click()
    page.wait_for_timeout(1000)
    orderIdColum = page.locator("//tbody//tr").nth(1)
    orderIdColum.get_by_role("button", name="View").click()
    page.wait_for_timeout(1000)
    error   =page.locator(".blink_me").text_content()
    print(error)
import pytest
from playwright.sync_api import Page

def test_ChildWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        #building a closure  expect_popup  and take that info new object .. this is for popup new window
    with page.expect_popup() as newPage_info: # opening the new page operations should be wrapped in here only
        page.locator(".blinkingText").click()  #new page
        childPage = newPage_info.value  # it is getting all the values , and child page will work as the page with all functionality
        content = childPage.locator(".red").text_content() # retieve content
        print(content) #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words =content.split("at")
        eamil = words[1].lstrip().split(" ")[0]
        assert  eamil == "mentor@rahulshettyacademy.com"
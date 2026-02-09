import json

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from apiBase import ApiUtils
from pageObjects.dashboard import DashboardPage
from pageObjects.login import LoginPage

#json file -- > utils --> access in test
with open('data/credentails.json') as json_file:
    json_data = json.load(json_file)
    userCredentialsList = json_data['user_Credentials']


@pytest.mark.parametrize('usercred',userCredentialsList)
def test_e2e_web_api(playwright:Playwright,usercred):
    browser=playwright.chromium.launch(headless=False)
    context =browser.new_context()
    page =context.new_page()

    #create order - orderId
    api_Utils = ApiUtils() # creating object of that class
    responseody = api_Utils.createOrder(playwright)
    orderId = responseody["orders"][0]
    print(orderId)

    # login to verify the order=
    userName =usercred["userEmail"]
    userPassword = usercred["userPassword"]
    #create object for login class
    loginPage =LoginPage(page)
    loginPage.navigate_to_login_page()
    dashboardPage = loginPage.login(userName,userPassword)

    #goit to order history page and check it the order id present or not
    #dashboardPage = DashboardPage(page) skipping this as this is handled in login method
    orderHistoryPage = dashboardPage.selectOrderNavLink()

    # now check if the order is present or not
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.verifyMessage()









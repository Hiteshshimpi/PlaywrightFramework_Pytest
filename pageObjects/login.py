from pageObjects.dashboard import DashboardPage


class LoginPage:
    def __init__(self,page):
        self.page = page


    def navigate_to_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def login(self, userName,userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userName)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.locator("#login").click()
        self.page.wait_for_timeout(2000)
        dashboardPage = DashboardPage(self.page)
        return dashboardPage
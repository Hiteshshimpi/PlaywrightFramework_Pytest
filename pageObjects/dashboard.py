from pageObjects.orderHistory import OrdersHistoryPage


class DashboardPage:
    def __init__(self,page):
        self.page = page

    def selectOrderNavLink(self):
        self.page.locator("//*[contains(@class,'btn-custom')]//i[contains(@class,'fa-handshake-o')]").click()
        self.page.wait_for_timeout(1000)
        orderHistoryPage = OrdersHistoryPage(self.page)
        return orderHistoryPage
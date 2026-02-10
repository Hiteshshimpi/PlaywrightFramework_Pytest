from pageObjects.orderDetails import OrderDetailsPage


class OrdersHistoryPage:
    def __init__(self, page):
        self.page = page

    def selectOrder(self,orderId):
        orderIdColum = self.page.locator("//tbody//tr").filter(has_text=orderId)
        orderIdColum.get_by_role("button", name="View").click()
        self.page.wait_for_timeout(1000)
        print(f"Order id for new order is : {orderIdColum}")
        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage
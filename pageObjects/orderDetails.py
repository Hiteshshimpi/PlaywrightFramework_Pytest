from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self, page):
        self.page = page

    def verifyMessage(self):
        expect(self.page.locator("p").filter(has_text="Thank you for Shopping With Us")).to_be_visible()

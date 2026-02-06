from tkinter import dialog

from playwright.sync_api import Page, expect

# hideen and visible
def test_UIchecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

#handling alerts
# lamba keywrod can be use dto create functiions , ananomus
def  test_AlertBoxes(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    page.wait_for_timeout(4000)
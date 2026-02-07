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


def test_frameHandling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    page.wait_for_timeout(4000)
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")

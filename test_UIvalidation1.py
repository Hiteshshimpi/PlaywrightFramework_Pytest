from playwright.sync_api import Page, expect, Playwright


phoneItems =['Iphone X','Nokia Edge']
# iphonex and Nokia edge add to cart and --> verify 2 items are showing in cart
def test_UIvalidation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print("Navigating to Rahul shetty academy...")
    print("Filling Username...")
    page.get_by_label("username").fill("rahulshettyacademy")
    print("Filling Password...")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")  # combobox is for select (dropdown) class and option is the value from HTML
    page.locator("#terms").check()  # --> To just check the checkbox
    page.get_by_role("button", name="Sign In").click()
    # using ccs selctor for tagName

#adding items to the card
    for item in phoneItems:
        product = page.locator("app-card").filter(has_text=item)  # this will return the value if matching to iphone X
        page.wait_for_timeout(5000)
        product.get_by_role("button").click()# this will limit the scope for that block whwere Iphone X is present
        page.wait_for_timeout(5000)

    page.locator("//a[contains(@class,'btn-primary')]").click() #checkout btn
    #or page.get_by_text("checkout)
    page.wait_for_timeout(5000)
    itemCount = page.locator("//*[@class='media-body']")
    print(f"Item count: {itemCount.count()}  and  length: {len(phoneItems)}")
    expect(itemCount).to_have_count(2)
    page.wait_for_timeout(5000)
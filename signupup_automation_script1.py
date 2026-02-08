from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Launch browser
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    
    page.goto("https://authorized-partner.vercel.app/")
    page.wait_for_timeout(1500)

     Click Login
    page.locator("text=Login").click()
    page.wait_for_timeout(1500)

     Click Sign Up
    page.locator("text=Sign Up").click()
    page.wait_for_timeout(1500)

     Agree checkbox
    page.locator("#remember").click()
    page.wait_for_timeout(800)

     Continue
    page.locator("text=Continue").click()
    page.wait_for_timeout(2000)

     Wait for form
    form = page.locator("form")
    form.wait_for()

    inputs = form.locator("input")

     Fill form like a human (important for React validation)
    data = [
        "Diwas",
        "Kushwaha",
        "diwas@example.com",
        "982964746",
        "TestPassword123",
        "TestPassword123"
    ]

    for i, value in enumerate(data):
        field = inputs.nth(i)
        field.click()
        field.type(value, delay=50)  # human typing
        page.keyboard.press("Tab")   # trigger validation
        page.wait_for_timeout(500)

    # Final validation trigger
    page.locator("body").click()
    page.wait_for_timeout(1000)

     Submit form (same as clicking Next)
    form.evaluate("form => form.requestSubmit()")

    print(" Next step triggered!")

    # Confirm navigation
    page.wait_for_timeout(3000)
    print("Current URL:", page.url)

    browser.close()


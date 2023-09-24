from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://playwright.dev/')
        page.wait_for_timeout(3000)


if __name__ == '__main__':
    main()
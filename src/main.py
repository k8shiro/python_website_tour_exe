from playwright.sync_api import sync_playwright

def main():
    chromium_executable_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium_executable_path, headless=False)
        page = browser.new_page()
        page.goto('https://playwright.dev/')
        page.wait_for_timeout(3000)


if __name__ == '__main__':
    main()
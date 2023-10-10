from playwright.sync_api import sync_playwright
import json

def load_urls_from_json():
    with open('urls.json', 'r') as file:
        url_list = json.load(file)
    return url_list

def load_settings_from_json():
    with open('settings.json', 'r') as file:
        url_list = json.load(file)
    return url_list

def main():
    urls = load_urls_from_json()
    settings = load_settings_from_json()
    chromium_executable_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    # スクロールの単位ピクセル数
    scroll_step = 200

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium_executable_path, headless=False)
        page = browser.new_page()

        for url in urls:
            page.goto(url)
            page.wait_for_timeout(3000)
            pre_scroll_position = -1

            while True:
                # 現在のスクロール位置を取得
                scroll_position = page.evaluate('window.scrollY')
                
                # スクロールが下部に到達した場合、ループを終了
                print(scroll_position, pre_scroll_position)
                if scroll_position == pre_scroll_position:
                    break
                else:
                    pre_scroll_position = scroll_position
                
                # ページを指定したステップ数分だけスクロール
                page.evaluate('window.scrollBy(0, {})'.format(scroll_step))
                
                # スクロール完了まで待機（必要に応じて適切な待機時間を設定）
                page.wait_for_timeout(1000)  # 1秒待機（適宜調整）

        browser.close()


if __name__ == '__main__':
    main()
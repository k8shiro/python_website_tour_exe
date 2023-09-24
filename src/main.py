from playwright.sync_api import sync_playwright
import json

def load_urls_from_json(json_file):
    with open(json_file, 'r') as file:
        url_list = json.load(file)
    return url_list

def main():
    urls = load_urls_from_json('urls.json')
    chromium_executable_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    # スクロールの単位ピクセル数
    scroll_step = 200

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium_executable_path, headless=False)
        page = browser.new_page()

        for url in urls:
            page.goto(url)
            page.wait_for_timeout(3000)

            while True:
                # ページの高さを取得
                page_height = page.evaluate('document.body.scrollHeight')
                
                # 現在のスクロール位置を取得
                scroll_position = page.evaluate('window.scrollY')
                
                # スクロールが下部に到達した場合、ループを終了
                if scroll_position >= page_height:
                    break
                
                # ページを指定したステップ数分だけスクロール
                page.evaluate('window.scrollBy(0, {})'.format(scroll_step))
                
                # スクロール完了まで待機（必要に応じて適切な待機時間を設定）
                page.wait_for_timeout(1000)  # 1秒待機（適宜調整）

        browser.close()


if __name__ == '__main__':
    main()
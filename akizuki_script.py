from playwright.sync_api import sync_playwright

def scrape_akizuki_product(url):
    # Playwrightの起動
    with sync_playwright() as p:
        # ブラウザを起動
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ユーザーエージェントを設定（任意）
        # page.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

        # 指定URLを開く
        page.goto(url)

        # 商品名と価格を取得
        try:
            # 商品名をid="spec_number"から取得する
            product_name = page.locator("#spec_number").inner_text()

            # 価格をclass="block-goods-price--price price js-enhanced-ecommerce-goods-price"から取得する
            # price = page.locator(".block-goods-price--price price js-enhanced-ecommerce-goods-price").first.inner_text().strip()
            price = page.locator(".block-goods-price--price.price.js-enhanced-ecommerce-goods-price").first.inner_text().strip()

        except Exception as e:
            print(f"データの取得に失敗しました: {e}")
            product_name, price = None, None

        # ブラウザを閉じる
        browser.close()

        return product_name, price


# サンプル実行
if __name__ == "__main__":
    # url = "https://www.akizuki.co.jp/dp/B09G9F5C5K"  # 対象商品のURLを設定
    url = "https://akizukidenshi.com/catalog/g/g109837/"
    product_name, price = scrape_akizuki_product(url)

    if product_name and price:
        print(f"商品名: {product_name}")
        print(f"価格: {price}")
    else:
        print("情報を取得できませんでした。")

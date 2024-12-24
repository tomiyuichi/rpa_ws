from playwright.sync_api import sync_playwright
import pandas as pd
import time

# スクレイピングするURLのリスト
urls = [
    "https://www.digikey.jp/en/products/detail/xxxxxx",
    "https://www.digikey.jp/en/products/detail/yyyyyy",
]

def scrape_digikey(url):
    """Digi-Keyの製品情報をスクレイピングする"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        
        # 商品名を取得
        product_name = page.query_selector("h1.product-title").inner_text()
        
        # 価格情報を取得
        price_elements = page.query_selector_all(".price-breaks-table tr")
        prices = [
            {
                "Quantity": row.query_selector("td:nth-child(1)").inner_text(),
                "Price": row.query_selector("td:nth-child(2)").inner_text(),
            }
            for row in price_elements
        ]
        
        # 在庫情報を取得
        stock_info = page.query_selector(".stock-details").inner_text()
        
        browser.close()
        return {
            "Product Name": product_name,
            "Prices": prices,
            "Stock Info": stock_info
        }

# 全URLに対してデータを収集
data = []
for url in urls:
    try:
        print(f"Scraping: {url}")
        product_data = scrape_digikey(url)
        data.append(product_data)
        time.sleep(2)  # サーバー負荷を避けるために待機
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# データをDataFrameに変換して保存
df = pd.DataFrame(data)
df.to_csv("digikey_products.csv", index=False)
print("データを保存しました: digikey_products.csv")
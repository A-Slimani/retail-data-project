import requests
import duckdb

SERVER = "http://10.0.0.216:8081"
TOPIC = "wrestling-shoes"

def under_150():
    conn = duckdb.connect("dev.duckdb")
    df = conn.execute(f"""
        SELECT *  
        FROM feed_mmafightstore_wrestlingshoes 
        WHERE price <= 100;
     """).fetchdf()


    for index, row in df.iterrows():
        message = f"name: {row['name']}\nprice: {row['price']}"

        headers = {
            "Title": ">=100 Wrestling Shoe Alert",
            "Priority": "default",
            "Click": row['product_link'],
            "Content-Type": "text/markdown"
        }

        requests.post(f"{SERVER}/{TOPIC}", data=message, headers=headers)

if __name__ == "__main__":
    under_150()

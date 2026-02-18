import requests
import duckdb

SERVER = "http://10.0.0.216:8081"
TOPIC = "wrestling-shoes"

def wrestlingshoes_under_100():
    try:
        print("Starting 'Wrestling shoes under 100' Alert")
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
        print("Successfully fetched 'Wrestling shoes under 100'")

    except Exception as e:
        headers = {
            "Title": ">=100 Wrestling Shoe Alert",
            "Priority": "default",
            "Content-Type": "text/markdown"
        }
        error_message = f"Fetching 'Wrestling shoes under 100' failed: {e}"
        requests.post(f"{SERVER}/{TOPIC}", data=error_message, headers=headers)
        print(error_message)



if __name__ == "__main__":
    wrestlingshoes_under_100()

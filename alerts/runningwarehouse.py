import requests
import duckdb

SERVER = "http://10.0.0.216:8081"
TOPIC = "running-shoes"

def runningwarehouse_under_100():
    try:
        print("Starting 'running shoes under 100' Alert")
        conn = duckdb.connect("dev.duckdb")
        df = conn.execute(f"""
            SELECT *  
            FROM feed_runningwarehouse
            WHERE price <= 100;
         """).fetchdf()

        for index, row in df.iterrows():
            message = f"name: {row['name']}\nprice: {row['price']}"

            headers = {
                "Title": ">=100 Running Shoe Alert",
                "Priority": "default",
                "Click": row['product_link'],
                "Content-Type": "text/markdown"
            }

            requests.post(f"{SERVER}/{TOPIC}", data=message, headers=headers)
        print("Successfully fetched 'running shoes under 100'")

    except Exception as e:
        headers = {
            "Title": ">=100 Running Shoe Alert",
            "Priority": "default",
            "Content-Type": "text/markdown"
        }
        error_message = f"Fetching 'running shoes under 100' failed: {e}"
        requests.post(f"{SERVER}/{TOPIC}", data=error_message, headers=headers)
        print(error_message)



if __name__ == "__main__":
    paceathletic_under_100()

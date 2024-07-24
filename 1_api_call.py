import requests

# 1. Get the data from the API
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
api_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=6PT406YTUPE5LSV0'
r = requests.get(api_url)
data = r.json()
print(data)

# 2. Get a Raw CSV file from GitHub
def download_csv_from_github(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"CSV file downloaded to {save_path}.")

url = "https://raw.githubusercontent.com/turingplanet/web-data-extraction-intro/main/sample_stock_data.csv"
file_path = "github_sample_data.csv"
download_csv_from_github(url, file_path)
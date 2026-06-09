from datetime import datetime


def fetch_data():
    try:
        import requests
    except ImportError:
        print("Install requests to fetch API data.")
        return {}

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=10,
        )
    except requests.RequestException:
        return {}

    if response.status_code == 200:
        return response.json()
    return {}


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Log data must be provided as a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    generate_log(log_data)

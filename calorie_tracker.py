from datetime import datetime

def get_datestamp():
    """
    Get current datestamp
    :return: String  of current date in YYYY-MM-DD format
    """
    return datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":
    formatted_date = get_datestamp()

    print(formatted_date)

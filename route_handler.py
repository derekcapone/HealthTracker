from datetime import datetime
import json


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_people():
    """
    Reads json file
    :return: dict of json file
    """
    f = open("people.json")
    file_text = f.read()
    return json.loads(file_text)


# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    people_dict = get_people()
    return people_dict


if __name__ == "__main__":
    people_d = read()
    print(people_d)

from datetime import datetime
import mongo_interface as mng

def get_datestamp():
    """
    Get current datestamp
    :return: String  of current date in YYYY-MM-DD format
    """
    return datetime.now().strftime("%Y-%m-%d")


def get_person_calories(name):
    """
    Gets calorie data for the given person
    :param name: Name of person to get calorie data for
    :return: Object containing all info in calorie data query
    """
    # connect to collection
    col = mng.connect_to_collection("PeopleData")

    dict_query = {"name": name}
    cal_data = mng.find_populated_field(col, dict_query)

    if len(cal_data) == 0:
        print("Cannot find entry in database")

    return cal_data


if __name__ == "__main__":
    formatted_date = get_datestamp()

    cal_d = get_person_calories("Peter")

    print(cal_d)

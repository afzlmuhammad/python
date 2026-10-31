import json
from datetime import datetime

from tripdata import get_trip


def main():
    # Build a list of trip dictionaries
    trips = [
        get_trip("Lisbon", "15-05-2023", "Tram rides and custard tarts."),
        get_trip("Mumbai", "02-08-2023", "Street food and sea breeze at Marine Drive."),
        get_trip("Istanbul", "27-12-2023", "Ferry across the Bosphorus at sunset."),
    ]

    for trip in trips:
        # Convert the date string into a date object
        visit_date = datetime.strptime(trip["date"], "%d-%m-%Y").date()

        # Format it as "Month Day, Year" (e.g. "May 15, 2023")
        trip["date"] = visit_date.strftime("%B %d, %Y")

    # Convert the list of trip dictionaries to a JSON string and print it
    print(json.dumps(trips, indent=2))


if __name__ == "__main__":
    main()
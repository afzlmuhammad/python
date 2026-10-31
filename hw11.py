import json
from datetime import datetime

from tracker import get_travel_record

def to_readable(date_str: str) -> str:
    return datetime.strptime(date_str, "%d-%m-%Y") .strftime("%B, %d, %Y")

def main():
    records = [
        get_travel_record("Paris", "Loved the Eiffel Tower at night.", "05-06-2022"),
        get_travel_record("Kyoto", "Peaceful temples and great tea.", "14-11-2022"),
        get_travel_record("Kochi", "Amazing seafood by the backwaters.", "21-01-2024"),   
    ]
    
    for record in records:
        record["date"] = to_readable(record["date"])
        
    json_string = json.dumps(records, indent=2)
    print("JSON string:")
    print(json_string)
    
    parsed = json.loads(json_string)
    print("\nParsed records:")
    for record in parsed:
        print(f"{record['city']} | {record['comment']} | {record['date']}")
        
        
if __name__ == "__main__":
    main()

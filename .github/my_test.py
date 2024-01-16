pip install androidusage
from androidusage.usagestats import UsageStats

def get_android_usage_stats():
    # Set the start and end dates for the query
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)  # Usage stats for the last 7 days

    # Query usage stats
    stats = UsageStats(start_date, end_date)

    for event in stats.get_events():
        print(f"Package: {event.package_name}, Time in Foreground: {event.time_in_foreground} seconds")

if __name__ == "__main__":
    from datetime import datetime, timedelta
    get_android_usage_stats()

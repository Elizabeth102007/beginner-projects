total_attempts = 0
total_success = 0
failure_counts = {}
retries = []
import logging
import random
logging.basicConfig(
    filename = "error.log",
    level = logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )
def fetch_weather(city):
    results = random.choices(["success", "connection", "timeout", "valueerror", "keyerror"],
              weights = [40, 20, 15, 15, 10], k=1
            )[0]
    
    if results == "success":
        data = {"city": city,
                "temperature": 24,
                "condition": "Windy",
                "humidity": 0.2}
        return data
    
    elif results == "connection":
        raise ConnectionError("Could not connect to the weather service")

    elif results == "timeout":
        raise TimeoutError("Weather server is too slow")
    
    elif results == "valueerror":
        raise ValueError("Invalid data recieved")
    
    elif results == "keyerror":
        raise KeyError("There is a missing field")



def get_weather_with_retry(city):

    global total_attempts
    global total_success

    retry_count = 0

    for w in range(1, 4):

        total_attempts += 1

        try:
            results = fetch_weather(city)

            total_success += 1

            retries.append(retry_count)

            return results

        except (ConnectionError, TimeoutError) as e:

            failure_type = type(e).__name__

            failure_counts[failure_type] = (
                failure_counts.get(failure_type, 0) + 1
            )

            logging.error(
                f"Attempt {w} - {failure_type}: {e}"
            )

            print(f"Attempt {w} failed. Retrying...")

            retry_count += 1

        except (ValueError, KeyError) as e:

            failure_type = type(e).__name__

            failure_counts[failure_type] = (
                failure_counts.get(failure_type, 0) + 1
            )

            logging.error(
                f"{failure_type}: {e}"
            )

            print("Process failed due to a data error.")

            return None

    print("There is an error with the server.")

    return None



def display_weather(data):
    print("----------Weather Forecast-----------")
    for key, value in data.items():
        print(f"{key.capitalize()} : {value}")

def show_session_report():

    print("\n--------- Session Report ---------")

    if total_attempts == 0:
        print("No weather requests made.")
        return

    success_rate = (total_success / total_attempts) * 100

    if retries:
        avg_retries = sum(retries) / len(retries)
    else:
        avg_retries = 0

    if failure_counts:
        most_common_failure = max(
            failure_counts,
            key=failure_counts.get
        )
    else:
        most_common_failure = "None"

    print(f"Total API Calls: {total_attempts}")
    print(f"Successful Requests: {total_success}")
    print(f"Success Rate: {success_rate:.2f}%")
    print(f"Average Retries Before Success: {avg_retries:.2f}")
    print(f"Most Common Failure Type: {most_common_failure}")

    print("\nFailure Breakdown:")
    for error, count in failure_counts.items():
        print(f"{error}: {count}")
    
def run_cli():
    print("========Weather Fetch Simulator=======")
    while True:
        city = input("Enter the city name (q to quit): ")
        
        if city.lower() == "q":
            break
        data = get_weather_with_retry(city)
        
        if data is not None:
            display_weather(data)
        else:
            print("Unable to get weather details")
        
    show_session_report()

if __name__ == "__main__":
   run_cli()
        
        






    
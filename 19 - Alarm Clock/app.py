import datetime
import time
import winsound

def set_alarm():
    while True:
        alarm_time = input("Enter the alarm time in HH:MM format (e.g., 07:30): ")
        try:
            hour, minute = map(int, alarm_time.split(":"))
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                break
            else:
                print("Invalid time format. Please try again.")
        except ValueError:
            print("Invalid time format. Please try again.")
    return hour, minute

def play_alarm_sound():
    frequency = 2500  # Frequency of the alarm sound (in Hz)
    duration = 5000  # Duration of the alarm sound (in milliseconds)
    winsound.Beep(frequency, duration)

def main():
    print("Welcome to the Alarm Clock!")
    while True:
        hour, minute = set_alarm()
        current_time = datetime.datetime.now()
        alarm_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if alarm_time < current_time:
            alarm_time += datetime.timedelta(days=1)
        time_diff = alarm_time - current_time
        print(f"Alarm set for {alarm_time.strftime('%Y-%m-%d %H:%M:%S')}. Sleeping for {time_diff.total_seconds()} seconds.")
        time.sleep(time_diff.total_seconds())
        print("Wake up! It's time for the alarm!")
        play_alarm_sound()
        choice = input("Do you want to set another alarm? (yes/no): ").lower()
        if choice != "yes":
            break
    print("Alarm Clock exiting...")

if __name__ == "__main__":
    main()
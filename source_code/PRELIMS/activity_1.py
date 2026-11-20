total_seconds = int(input("Enter the elapsed time in seconds: ")) #ask the user

hours = int(total_seconds / 3600) #converting the total seconds into hrs
remaining_seconds = total_seconds % 3600 #getting the remaining seconds after calculating the hrs
minutes = int(remaining_seconds / 60) #converting the remaining seconds into minutes
seconds = remaining_seconds % 60 #getting the remaining seconds after calculating the minutes

print(f"Elapsed time: {hours}:{minutes:02d}:{seconds:02d}")

while True:
    try:
        user_input = input("Enter the elapsed time in seconds (or stop to quit): ")

        if user_input.upper() == "stop":
            print("Program stopped.")
            break

        elapsed_sec = int(user_input)

        hours = elapsed_sec // 3600

        remaining_sec = elapsed_sec % 3600

        minutes = remaining_sec // 6
        seconds = remaining_sec % 60

        print("Elapsed time:")
        print(hours, ":", minutes, ":", seconds)

    except ValueError:
        print("Invalid input. Please enter a number or stop.")



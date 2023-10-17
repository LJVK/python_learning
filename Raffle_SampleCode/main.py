import random
import uuid


def generate_random_numbers_with_shared_userid(count):
    # Generate a single unique user ID
    user_id = str(uuid.uuid4())

    user_id_to_numbers = {user_id: []}

    for _ in range(count):
        # Generate a 16 digit random number
        random_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
        # Append the random number to the list associated with the User ID
        user_id_to_numbers[user_id].append(random_number)
    return user_id_to_numbers


if __name__ == '__main__':
    # Input Parameters : specify how many random numbers you want to generate
    count = int(input("Enter the number of random 16 digit numbers to generate: "))

    user_id_to_numbers = generate_random_numbers_with_shared_userid(count)

    # Print the generated user ID and corresponding random numbers
    for user_id, numbers in user_id_to_numbers.items():
        print(f"User ID: {user_id}, Random Numbers: {', '.join(numbers)}")


    # Save the data to a file
    with open("user_numbers_mapping.txt", "a") as file:
        for user_id, numbers in user_id_to_numbers.items():
            file.write(f"User ID: {user_id}, Random Numbers: {', '.join(numbers)}\n")

    # Select and display a random number along with corresponding User ID from the file
    with open("user_numbers_mapping.txt", "r") as file:
        lines = file.readlines()
        selected_line = random.choice(lines)
        selected_user_id = selected_line.split(",")[0].strip().replace("User ID: ", "")
        selected_random_number = selected_line.split(",")[1].strip().replace("Random Number: ", "")

    print(f"Selected User ID: {selected_user_id}, Selected Random Number: {selected_random_number}")
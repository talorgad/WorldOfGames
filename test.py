import csv

def get_and_save_user_input(filename):
  """
  This function prompts the user for input, collects it in a list, and writes it to a CSV file.

  Args:
      filename (str): The name of the CSV file to write to.

  Returns:
      None
  """
  user_data = []
  while True:
    user_input = input("Enter data (or 'q' to quit): ")
    if user_input.lower() == "q":
      break
    user_data.append(user_input)

  # Write data to CSV file
  with open(filename, "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(user_data)

  print(f"Data saved successfully to {filename}")

# Example usage:
get_and_save_user_input("user_data.csv")

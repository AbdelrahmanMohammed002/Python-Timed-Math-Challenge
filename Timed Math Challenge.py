import random
import time

# Constants
OPERATORS = ["+", "-", "*"]  # Supported mathematical operators
MIN_OPERAND = 3              # Minimum value for operands
MAX_OPERAND = 12             # Maximum value for operands
TOTAL_PROBLEMS = 10          # Total number of problems in the quiz

def generate_problem():
    """
    Generates a random arithmetic problem using two random operands and a random operator.
    
    Returns:
        expression (str): A string representing the arithmetic expression (e.g., "5 + 7").
        answer (int or float): The correct answer to the generated arithmetic problem.
    """
    left = random.randint(MIN_OPERAND, MAX_OPERAND)   # Randomly select the first operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Randomly select the second operand
    operator = random.choice(OPERATORS)               # Randomly choose an operator

    # Create an arithmetic expression (e.g., "5 + 7")
    expression = f"{left} {operator} {right}"
    
    # Evaluate the expression to get the correct answer
    answer = eval(expression)  # `eval` safely used here since input is controlled
    return expression, answer

# Start the quiz
input("Press Enter to Start!")
print("=====================")

# Record the start time
start_time = time.time()

# Loop through and present a total of `TOTAL_PROBLEMS` arithmetic problems
for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()  # Generate a new problem

    # Keep prompting the user for an answer until the correct answer is provided
    while True:
        guess = input(f"Problem Number #{i + 1}:\n{expression} = ")
        
        if guess == str(answer):
            break  # Exit the loop when the correct answer is given
        else:
            print("Incorrect, try again.")

# Record the end time and calculate total duration
end_time = time.time()
total_time = round(end_time - start_time, 2)

# Display results
print("=====================")
print(f"Nice work! Your total time is: {total_time} seconds")

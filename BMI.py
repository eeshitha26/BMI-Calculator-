def calculate_bmi():
    print("--- Oasis Infobyte BMI Calculator ---")
    try:
        # Prompt user for input
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")

        # Categorize results
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
            
        print(f"Health Category: {category}")
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_bmi()
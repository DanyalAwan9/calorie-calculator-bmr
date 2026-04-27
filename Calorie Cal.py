def calculate_bmr(weight, height, age):
    # Assuming male (you can extend later)
    return 10 * weight + 6.25 * height - 5 * age + 5


def get_activity_multiplier(workout_days):
    if workout_days == 0:
        return 1.2
    elif workout_days <= 2:
        return 1.375
    elif workout_days <= 4:
        return 1.55
    elif workout_days <= 6:
        return 1.725
    else:
        return 1.9


def main():
    print("=== Calorie Calculator ===")

    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))
    age = int(input("Enter age: "))
    workout_days = int(input("Workout days per week (0-7): "))

    bmr = calculate_bmr(weight, height, age)
    activity_multiplier = get_activity_multiplier(workout_days)

    daily_calories = bmr * activity_multiplier

    print("\n=== Results ===")
    print(f"BMR: {round(bmr, 2)} calories/day")
    print(f"Daily Maintenance Calories: {round(daily_calories, 2)}")

    print("\nGoals:")
    print(f"Fat Loss: {round(daily_calories - 300, 2)} kcal")
    print(f"Muscle Gain: {round(daily_calories + 300, 2)} kcal")


if __name__ == "__main__":
    main()
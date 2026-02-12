def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters

    Returns:
        float: BMI value
    """
    # Check for invalid input
    if height_m <= 0:
        raise ValueError("Height must be greater than 0.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0.")

    bmi = weight_kg / (height_m ** 2)
    return bmi

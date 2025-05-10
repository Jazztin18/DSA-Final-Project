# Pseudocode for HealthTrack

## START PROGRAM

1. Initialize the GUI window (title: HealthTrack)
2. Display the "Login" tab:
    - Ask user for Name and Age
    - Validate:
        - Name must not be empty
        - Age must be a number between 1 and 119
3. IF valid:
    - Store name and age
    - Switch to "Main Menu" tab

## MAIN MENU

4. Show greeting with user’s name and age
5. Show menu options:
    - BMI Calculator
    - Calorie Needs (BMR) Calculator
    - Blood Sugar Checker
    - Urinalysis Interpretation
    - Exit
6. Show previously generated results (if any)

---

### IF user selects "BMI Calculator"
1. Ask for height in cm and weight in kg
2. Convert height to meters
3. Calculate BMI = weight / (height * height)
4. Determine BMI category:
    - <18.5: Underweight
    - 18.5–24.9: Normal
    - 25–29.9: Overweight
    - 30+: Obese
5. Save and display result

---

### IF user selects "Calorie Needs (BMR) Calculator"
1. Ask for gender, weight, height, and age
2. Calculate BMR:
    - Male: `10*weight + 6.25*height - 5*age + 5`
    - Female: `10*weight + 6.25*height - 5*age - 161`
3. Ask for fitness goal: lose, maintain, or gain weight
4. Adjust calorie needs:
    - Lose: BMR - 500
    - Maintain: BMR
    - Gain: BMR + 500
5. Save and display result with advice

---

### IF user selects "Blood Sugar Checker"
1. Ask for fasting blood sugar level (mg/dL)
2. Determine status:
    - <70: Low (Hypoglycemia)
    - 70–99: Normal
    - 100–125: Prediabetes
    - 126+: Diabetes
3. Save and display result

---

### IF user selects "Urinalysis Interpretation"
1. Ask for:
    - Pus cells (WBC)
    - Red blood cells (RBC)
    - Urine transparency
    - Squamous cells
    - Amorphous urates
    - Presence of UTI symptoms
2. Analyze values:
    - Evaluate normal/abnormal ranges for each
3. Compile findings based on input
4. Save and display result

---

### IF user selects "Exit"
- Close the program

## END PROGRAM

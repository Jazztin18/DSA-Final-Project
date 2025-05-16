START PROGRAM
1. Initialize GUI Window
    - Set title: HealthTrack: Wellness Dashboard
    - Set dimensions and background color
    - Load design styles (fonts, colors, themes)

2. Define Input Variables
    - Patient Info: Name, Age, Gender, Date
    - BMI: Weight, Height, Result
    - BMR: Weight, Height, Goal, Result
    - Blood Sugar: Value, Result
    - Urinalysis: Pus Cells, RBC, Transparency, Squamous Cells, Urates, Symptoms, Result

DISPLAY MAIN INTERFACE
3. Sidebar Menu with Buttons:
    - BMI Calculator
    - BMR Calculator
    - Blood Sugar
    - Urinalysis
    - Save Summary
    - Exit Program

4. Main Content Layout
    - Header with App Title and Tagline
    - Patient Information Form (Name, Age, Gender, Date)
    - Summary Results Display Area

BMI CALCULATOR MODULE
5. Show BMI Calculator Window
    - Input: Weight (kg) and Height (cm)
    - On "Calculate":
        - Convert height to meters
        - Calculate BMI using:
        - BMI = Weight / (Height_in_meters)^2
        - Determine status: Underweight, Normal, Overweight, Obese
        - Provide personalized advice
        - Store result and update summary panel

BMR CALCULATOR MODULE
6. Show BMR Calculator Window
    - Input: Weight, Height, Age, Gender, Goal
    - On "Calculate":
        - Calculate base BMR using Harris-Benedict formula:
        - BMR = 10*W + 6.25*H - 5*A + (5 if Male, -161 if Female)
    - Adjust BMR based on goal:
        - Lose → BMR - 500
        - Gain → BMR + 500
        - Maintain → base BMR
    - Display result and advice
    - Store result and update summary panel

🩸 BLOOD SUGAR ANALYZER MODULE
7. Show Blood Sugar Input Window
    - Input: Blood Sugar (mg/dL)
    - On "Analyze":
        - Classify value:
        - < 70 → Low
        - 70–99 → Normal
        - 100–125 → Prediabetes
        - >125 → High
    - Show interpretation and advice
    - Store result and update summary panel

URINALYSIS INTERPRETATION MODULE
8. Show Urinalysis Input Window
    - Input via dropdowns:
        - Pus Cells, RBC, Transparency, Squamous Cells, Urates, Symptoms
    - On "Interpret":
        - Evaluate indicators for UTI or abnormality
        - List flagged findings
        - State whether UTI is detected
        - Display final advice
        - Store result and update summary panel
        
SAVE SUMMARY FUNCTION
9. Export Summary
    - When "Save Summary" is clicked:
        - Open file dialog
        - Save results and patient info in .txt file format
        - Display success message

END PROGRAM
10. User exits app via sidebar "Exit" button

PSEUDOCODE – HealthTrackApp: Wellness Dashboard

START PROGRAM

1. Initialize GUI Window
   - Set window title: "HealthTrack: Wellness Dashboard"
   - Set dimensions and background color
   - Load and apply design styles (fonts, colors, themes)

2. Define Input Variables
   - Patient Info:
     - Name
     - Age
     - Gender
     - Date
   - BMI:
     - Weight
     - Height
     - BMI Result
   - BMR:
     - Weight
     - Height
     - Goal (lose, maintain, gain)
     - BMR Result
   - Blood Sugar:
     - Sugar Value
     - Sugar Result
   - Urinalysis:
     - Pus Cells
     - RBC
     - Transparency
     - Squamous Cells
     - Urates
     - Symptoms
     - Urinalysis Result

DISPLAY MAIN INTERFACE

3. Sidebar Menu with Buttons:
   - BMI Calculator
   - BMR Calculator
   - Blood Sugar
   - Urinalysis
   - Save Summary
   - Exit Program

4. Main Content Layout
   - Display header with application title and tagline
   - Display patient information form (Name, Age, Gender, Date)
   - Display summary results panel (scrollable text box)

BMI CALCULATOR MODULE

5. Show BMI Calculator Window
   - Prompt user for:
     - Weight (kg)
     - Height (cm)
   - On "Calculate":
     - Convert height to meters
     - Compute BMI: BMI = weight / (height_in_meters ^ 2)
     - Determine health status based on BMI:
       - Underweight
       - Normal
       - Overweight
       - Obese
     - Provide health advice based on status
     - Store BMI result
     - Update summary panel

BMR CALCULATOR MODULE

6. Show BMR Calculator Window
   - Prompt user for:
     - Weight
     - Height
     - Age
     - Gender
     - Goal
   - On "Calculate":
     - Compute base BMR using Harris-Benedict formula:
       - BMR = 10 * weight + 6.25 * height - 5 * age + (5 if male, -161 if female)
     - Adjust BMR based on goal:
       - Lose → BMR - 500
       - Gain → BMR + 500
       - Maintain → base BMR
     - Provide personalized advice
     - Store BMR result
     - Update summary panel

BLOOD SUGAR ANALYZER MODULE

7. Show Blood Sugar Input Window
   - Prompt user for Blood Sugar (mg/dL)
   - On "Analyze":
     - Classify value:
       - < 70 → Low
       - 70–99 → Normal
       - 100–125 → Prediabetes
       - > 125 → High
     - Provide interpretation and advice
     - Store Blood Sugar result
     - Update summary panel

URINALYSIS INTERPRETATION MODULE

8. Show Urinalysis Input Window
   - Prompt user for dropdown selections:
     - Pus Cells
     - RBC
     - Transparency
     - Squamous Cells
     - Urates
     - Symptoms
   - On "Interpret":
     - Check for abnormalities:
       - High WBC (Pus Cells) → possible infection
       - Non-transparent urine → possible infection
       - Symptoms present → potential UTI
       - Elevated RBC → irritation or infection
     - Detect UTI status
     - Display findings and recommendation
     - Store Urinalysis result
     - Update summary panel

SAVE SUMMARY FUNCTION

9. Export Summary
   - On "Save Summary" button click:
     - Open file dialog for save location
     - Export all client information and health results to a .txt file
     - Show confirmation message on success

END PROGRAM

10. User exits application by clicking the "Exit" button

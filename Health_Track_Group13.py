import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext

results = {}

class HealthTrackApp:
    def __init__(self, master):
        self.master = master
        master.title("HealthTrack")
        master.geometry("650x520")
        master.resizable(False, False)

        self.user_name = ""
        self.user_age = ""

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 11), padding=6)
        self.style.configure("Title.TLabel", font=("Arial", 22, "bold"))

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.login_frame = ttk.Frame(self.notebook, padding=20)
        self.main_menu_frame = ttk.Frame(self.notebook, padding=20)

        self.notebook.add(self.login_frame, text="Login")
        self.notebook.add(self.main_menu_frame, text="Main Menu", state="hidden")

        self.login_screen()

    def login_screen(self):
        for widget in self.login_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.login_frame, text="HealthTrack", style="Title.TLabel").grid(row=0, column=0, columnspan=2, pady=20)

        ttk.Label(self.login_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.name_entry = ttk.Entry(self.login_frame, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)

        ttk.Label(self.login_frame, text="Age:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.age_entry = ttk.Entry(self.login_frame, width=30)
        self.age_entry.grid(row=2, column=1, pady=5)

        submit_btn = ttk.Button(self.login_frame, text="Submit", command=self.save_user_info)
        submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

    def save_user_info(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()

        if name and age.isdigit() and 0 < int(age) < 120:
            self.user_name = name
            self.user_age = age
            self.notebook.tab(1, state="normal")
            self.update_main_menu()
            self.notebook.select(1)
        else:
            messagebox.showerror("Input Error", "Please enter a valid name and age (0 < age < 120).")

    def update_main_menu(self):
        for widget in self.main_menu_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.main_menu_frame, text=f"Welcome {self.user_name}, Age {self.user_age}",
                  font=("Arial", 14, "bold"), foreground="blue").grid(row=0, column=0, columnspan=2, pady=10)

        buttons = [
            ("BMI Calculator", self.calculate_bmi),
            ("Calorie Needs (BMR) Calculator", self.calculate_bmr),
            ("Blood Sugar Checker", self.check_blood_sugar),
            ("Urinalysis Interpretation", self.analyze_urinalysis),
            ("Exit", self.master.quit)
        ]

        for i, (text, cmd) in enumerate(buttons):
            ttk.Button(self.main_menu_frame, text=text, width=35, command=cmd).grid(
                row=i + 1, column=0, columnspan=2, pady=5)

        ttk.Label(self.main_menu_frame, text="Results:", font=("Arial", 12, "bold"), foreground="green").grid(
            row=len(buttons) + 1, column=0, columnspan=2, pady=(15, 5))

        self.result_box = scrolledtext.ScrolledText(self.main_menu_frame, height=10, width=70, wrap=tk.WORD)
        self.result_box.grid(row=len(buttons) + 2, column=0, columnspan=2, pady=5)
        self.refresh_results()

    def refresh_results(self):
        self.result_box.delete("1.0", tk.END)
        if not results:
            self.result_box.insert(tk.END, "No results available yet.\n")
        else:
            for key, value in results.items():
                self.result_box.insert(tk.END, f"{key} Result:\n{value}\n\n")

    def calculate_bmi(self):
        try:
            height_cm = float(simpledialog.askstring("BMI Calculator", "Enter your height in cm:"))
            weight_kg = float(simpledialog.askstring("BMI Calculator", "Enter your weight in kg:"))

            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"

            result_text = f"Height: {height_cm} cm\nWeight: {weight_kg} kg\nBMI: {bmi:.2f} ({category})"
            results["BMI"] = result_text
            self.refresh_results()

        except (TypeError, ValueError):
            messagebox.showerror("Input Error", "Please enter valid numeric values for height and weight.")

    def calculate_bmr(self):
        try:
            gender = simpledialog.askstring("BMR Calculator", "Enter your gender (male/female):").strip().lower()
            weight = float(simpledialog.askstring("BMR Calculator", "Enter your weight in kg:"))
            height = float(simpledialog.askstring("BMR Calculator", "Enter your height in cm:"))
            age = int(simpledialog.askstring("BMR Calculator", "Enter your age:"))

            if gender == "male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            elif gender == "female":
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
            else:
                messagebox.showerror("Input Error", "Invalid gender.")
                return

            goal = simpledialog.askstring("BMR Calculator", "What is your goal? (lose/maintain/gain):").strip().lower()

            if goal == "lose":
                calories = bmr - 500
                advice = "To lose weight, consume about 500 calories less than your daily needs."
            elif goal == "maintain":
                calories = bmr
                advice = "To maintain your weight, consume about the same as your BMR."
            elif goal == "gain":
                calories = bmr + 500
                advice = "To gain weight, consume about 500 calories more than your daily needs."
            else:
                messagebox.showerror("Input Error", "Invalid goal.")
                return

            result_text = f"Daily Calorie Needs for your goal ({goal}): {calories:.2f} calories/day\n{advice}"
            results["BMR"] = result_text
            self.refresh_results()

        except (ValueError, TypeError):
            messagebox.showerror("Input Error", "Please enter valid values.")

    def check_blood_sugar(self):
        try:
            sugar = float(simpledialog.askstring("Blood Sugar Checker", "Enter your fasting blood sugar level (mg/dL):"))

            if sugar < 70:
                status = "Low blood sugar (Hypoglycemia)"
            elif 70 <= sugar <= 99:
                status = "Normal"
            elif 100 <= sugar <= 125:
                status = "Prediabetes"
            else:
                status = "Diabetes (Consult a healthcare professional)"

            result_text = f"Blood Sugar: {sugar} mg/dL - {status}"
            results["Blood Sugar"] = result_text
            self.refresh_results()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a number.")

    def analyze_urinalysis(self):
        findings = []

        try:
            wbc = int(simpledialog.askstring("Urinalysis", "Enter number of pus cells (WBC) per HPF:"))
            rbc = int(simpledialog.askstring("Urinalysis", "Enter number of red blood cells (RBC) per HPF:"))
            transparency = simpledialog.askstring("Urinalysis", "Enter urine transparency (Clear / Slightly Turbid / Turbid):").strip().lower()
            squamous = int(simpledialog.askstring("Urinalysis", "Enter number of squamous epithelial cells per HPF:"))
            urates = simpledialog.askstring("Urinalysis", "Enter description of amorphous urates (None / Few / Many):").strip().lower()
            symptoms = simpledialog.askstring("Urinalysis", "Are you experiencing UTI symptoms? (Yes/No):").strip().lower()
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input. Please enter correct values.")
            return

        if wbc > 5:
            findings.append("High WBC (Possible infection)")
        elif wbc > 0:
            findings.append("Mild WBC presence")
        else:
            findings.append("Normal WBC")

        if rbc > 3:
            findings.append("High RBC (Possible bleeding or inflammation)")
        elif rbc > 0:
            findings.append("Mild RBC presence")
        else:
            findings.append("Normal RBC")

        if transparency != "clear":
            findings.append("Urine not clear")
        else:
            findings.append("Clear urine")

        if squamous > 5:
            findings.append("High squamous cells (Possible contamination)")
        elif squamous > 0:
            findings.append("Few squamous cells")
        else:
            findings.append("Normal squamous cells")

        if urates == "few":
            findings.append("Few amorphous urates (Normal)")
        elif urates == "many":
            findings.append("Many amorphous urates (Crystallization possible)")

        if symptoms == "yes":
            findings.append("UTI symptoms reported")
        else:
            findings.append("No UTI symptoms")

        result_text = "\n".join(findings)
        results["Urinalysis"] = result_text
        self.refresh_results()

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthTrackApp(root)
    root.mainloop()

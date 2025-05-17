# HealthTrackApp - GROUP 13

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import datetime

# ---------- STYLE CONFIGURATION ----------
# This dictionary centralizes the app’s color scheme and fonts for easy updates
style_config = {
    "bg_color": "#f5f5f5",         # Main background color
    "card_bg": "#ffffff",          # Background for cards (content blocks)
    "accent_color": "#1976d2",     # Primary color for buttons and headers
    "accent_light": "#e3f2fd",     # Light accent for sidebar
    "section_bg": "#eaf4fb",       # Background for input sections
    "font_main": ("Segoe UI", 12), # Default font
    "font_title": ("Segoe UI", 20, "bold") # Font for titles
}

# Global dictionaries to store results and client info
results = {}
client_info = {}

# ---------- MAIN APPLICATION CLASS ----------
class HealthTrackApp:
    def __init__(self, root):
        # Set up main window
        self.root = root
        self.root.title("HealthTrack: Wellness Dashboard")
        self.root.geometry("1080x720")
        self.root.configure(bg=style_config["bg_color"])

        # Apply style using ttk
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background=style_config["bg_color"])
        style.configure("Sidebar.TFrame", background=style_config["accent_light"])
        style.configure("Card.TFrame", background=style_config["card_bg"])
        style.configure("Section.TLabelframe", background=style_config["section_bg"], padding=12)
        style.configure("Accent.TButton", background=style_config["accent_color"],
                        foreground="white", font=style_config["font_main"], relief="flat")
        style.map("Accent.TButton", background=[('active', '#1565c0')],
                  foreground=[('active', 'white')])
        style.configure("TLabel", background=style_config["bg_color"], font=style_config["font_main"])
        style.configure("TEntry", font=style_config["font_main"], padding=6)
        style.configure("TCombobox", font=style_config["font_main"], padding=6)

        # Variables for user input
        self.name = tk.StringVar()
        self.age = tk.IntVar()
        self.gender = tk.StringVar()
        self.date = tk.StringVar(value=datetime.date.today().strftime('%Y-%m-%d'))

        # Variables for BMI
        self.bmi_weight = tk.DoubleVar()
        self.bmi_height = tk.DoubleVar()
        self.bmi_result = tk.StringVar()

        # Variables for BMR
        self.bmr_weight = tk.DoubleVar()
        self.bmr_height = tk.DoubleVar()
        self.bmr_goal = tk.StringVar()
        self.bmr_result = tk.StringVar()

        # Variables for Blood Sugar
        self.sugar_value = tk.DoubleVar()
        self.sugar_result = tk.StringVar()

        # Variables for Urinalysis
        self.pus_cells = tk.StringVar()
        self.rbc = tk.StringVar()
        self.transparency = tk.StringVar()
        self.squamous_cells = tk.StringVar()
        self.urates = tk.StringVar()
        self.symptoms = tk.StringVar()

        # List to store feature buttons (for enabling/disabling)
        self.feature_buttons = []

        # Build interface
        self.build_layout()

    # ---------- LAYOUT SETUP ----------
    def build_layout(self):
        # Split screen into sidebar and main content
        container = ttk.Frame(self.root)
        container.pack(fill='both', expand=True)

        self.sidebar = ttk.Frame(container, width=200, style="Sidebar.TFrame")
        self.sidebar.pack(side='left', fill='y')

        self.main_content = ttk.Frame(container, style="TFrame")
        self.main_content.pack(side='left', fill='both', expand=True)

        # Sidebar title
        ttk.Label(self.sidebar, text="☰ Menu", font=style_config["font_title"],
                  foreground=style_config["accent_color"],
                  background=style_config["accent_light"]).pack(pady=10)

        # Sidebar feature buttons (initially disabled)
        for text, command in [
            ("🧮 BMI Calculator", self.create_bmi_content),
            ("🔥 BMR Calculator", self.create_bmr_content),
            ("🩸 Blood Sugar", self.create_sugar_content),
            ("🧪 Urinalysis", self.create_urinalysis_content),
            ("🖨️ Save Summary", self.download_summary),
        ]:
            btn = ttk.Button(self.sidebar, text=text, width=20, style="Accent.TButton",
                             command=lambda c=command: self.safe_launch(c))
            btn.pack(pady=6, padx=10)
            self.feature_buttons.append(btn)
            btn.state(["disabled"])  # Lock until patient info is entered

        # Exit button (always enabled)
        ttk.Button(self.sidebar, text="🚪 Exit", width=20, style="Accent.TButton",
                   command=self.root.quit).pack(pady=6, padx=10)

        # Load header, form, and summary panel
        self.create_header()
        self.create_main_form()
        self.create_summary_panel()

    # ---------- HEADER DISPLAY ----------
    def create_header(self):
        header = ttk.Frame(self.main_content, style="Card.TFrame")
        header.pack(fill='x', padx=20, pady=(20, 10))
        ttk.Label(header, text="HealthTrack", font=style_config["font_title"],
                  foreground=style_config["accent_color"],
                  background=style_config["card_bg"]).pack(anchor='w')
        ttk.Label(header,
                  text="\"Your health, tracked simply.\" Empowering wellness through clear and easy-to-understand assessments.",
                  font=("Segoe UI", 10), wraplength=800, justify="left", background=style_config["card_bg"]).pack(anchor='w', pady=2)

    # ---------- PATIENT INFO FORM ----------
    def create_main_form(self):
        form = ttk.Labelframe(self.main_content, text="Patient Information", style="Section.TLabelframe")
        form.pack(fill='x', padx=20, pady=(5, 5))

        # Create fields
        self.create_labeled_entry(form, "Name:", self.name)
        self.create_labeled_entry(form, "Age:", self.age)
        self.create_labeled_entry(form, "Gender:", self.gender)
        self.create_labeled_entry(form, "Date:", self.date)

        # Confirm button to unlock the rest of the app
        ttk.Button(form, text="✅ Confirm Patient Info", style="Accent.TButton",
                   command=self.enable_features).pack(pady=10)

    # ---------- SUMMARY PANEL ----------
    def create_summary_panel(self):
        summary = ttk.Labelframe(self.main_content, text="Summary Results", style="Section.TLabelframe")
        summary.pack(fill='both', expand=True, padx=20, pady=(5, 20))
        self.results_display = scrolledtext.ScrolledText(summary, height=20, font=("Consolas", 10), background="#ffffff")
        self.results_display.pack(fill='both', expand=True)

    # ---------- HELPER TO CREATE LABELED ENTRY ----------
    def create_labeled_entry(self, parent, label, variable):
        frame = ttk.Frame(parent)
        frame.pack(fill='x', pady=6)
        ttk.Label(frame, text=label, width=20, anchor='w').pack(side='left')
        ttk.Entry(frame, textvariable=variable).pack(side='right', fill='x', expand=True)

    # ---------- VALIDATE PATIENT INFO ----------
    def validate_patient_info(self):
        return all([
            self.name.get().strip(),
            self.age.get() > 0,
            self.gender.get().strip(),
            self.date.get().strip()
        ])

    # ---------- ENABLE FEATURES IF INFO COMPLETE ----------
    def enable_features(self):
        if self.validate_patient_info():
            for btn in self.feature_buttons:
                btn.state(["!disabled"])
            messagebox.showinfo("Success", "Patient info saved. Features unlocked!")
        else:
            messagebox.showerror("Error", "Please complete all fields (Name, Age, Gender, Date).")

    # ---------- SAFETY WRAPPER TO CHECK INFO BEFORE LAUNCH ----------
    def safe_launch(self, func):
        if not self.validate_patient_info():
            messagebox.showwarning("Missing Info", "Please fill in all patient information first.")
            return
        func()

    # ---------- REFRESH SUMMARY DISPLAY ----------
    def refresh_results(self):
        client_info.update({
            "Name": self.name.get(), "Age": self.age.get(), "Gender": self.gender.get(), "Date": self.date.get()
        })
        self.results_display.delete('1.0', tk.END)
        for key, value in results.items():
            self.results_display.insert(tk.END, f"{key} Result:\n{value}\n{'-'*40}\n")

    # ---------- BMI FUNCTIONALITY ----------
    def create_bmi_content(self):
        win = tk.Toplevel(self.root)
        win.title("BMI Calculator")
        win.geometry("400x300")
        self.create_labeled_entry(win, "Weight (kg):", self.bmi_weight)
        self.create_labeled_entry(win, "Height (cm):", self.bmi_height)
        ttk.Button(win, text="Calculate BMI", command=self.calculate_bmi).pack(pady=10)
        ttk.Label(win, textvariable=self.bmi_result).pack(pady=10)

    def calculate_bmi(self):
        try:
            height_m = self.bmi_height.get() / 100
            bmi = self.bmi_weight.get() / (height_m ** 2)
            status = ("Underweight", "Normal", "Overweight", "Obese")
            level = ("Consider increasing calorie intake.",
                     "Maintain current lifestyle.",
                     "Add more exercise and reduce calories.",
                     "Consult a healthcare provider.")
            index = 0 if bmi < 18.5 else 1 if bmi < 24.9 else 2 if bmi < 29.9 else 3
            result = f"BMI: {bmi:.2f} ({status[index]})\nAdvice: {level[index]}"
            self.bmi_result.set(result)
            results["BMI"] = result
            self.refresh_results()
        except:
            messagebox.showerror("Error", "Invalid input for BMI.")

    # ---------- BMR FUNCTIONALITY ----------
    def create_bmr_content(self):
        win = tk.Toplevel(self.root)
        win.title("BMR Calculator")
        win.geometry("400x350")
        self.create_labeled_entry(win, "Weight (kg):", self.bmr_weight)
        self.create_labeled_entry(win, "Height (cm):", self.bmr_height)
        ttk.Label(win, text="Goal:").pack()
        ttk.Combobox(win, textvariable=self.bmr_goal, values=["lose", "maintain", "gain"]).pack(pady=5)
        ttk.Button(win, text="Calculate BMR", command=self.calculate_bmr).pack(pady=10)
        ttk.Label(win, textvariable=self.bmr_result).pack(pady=10)

    def calculate_bmr(self):
        try:
            w, h, a = self.bmr_weight.get(), self.bmr_height.get(), self.age.get()
            g = self.gender.get().lower()
            bmr = 10 * w + 6.25 * h - 5 * a + (5 if g == "male" else -161)
            goal = self.bmr_goal.get().lower()
            adj = bmr - 500 if goal == "lose" else bmr + 500 if goal == "gain" else bmr
            advice = {
                "lose": "Consume fewer calories, increase physical activity.",
                "gain": "Increase calorie intake with nutrient-dense foods.",
                "maintain": "Maintain current eating and activity levels."
            }[goal]
            result = f"Base BMR: {bmr:.0f} kcal\nAdjusted for goal: {adj:.0f} kcal\nAdvice: {advice}"
            self.bmr_result.set(result)
            results["BMR"] = result
            self.refresh_results()
        except:
            messagebox.showerror("Error", "Invalid input for BMR.")

    # ---------- BLOOD SUGAR FUNCTIONALITY ----------
    def create_sugar_content(self):
        win = tk.Toplevel(self.root)
        win.title("Blood Sugar Analyzer")
        win.geometry("400x250")
        self.create_labeled_entry(win, "Blood Sugar (mg/dL):", self.sugar_value)
        ttk.Button(win, text="Analyze", command=self.analyze_blood_sugar).pack(pady=10)
        ttk.Label(win, textvariable=self.sugar_result).pack(pady=10)

    def analyze_blood_sugar(self):
        try:
            sugar = self.sugar_value.get()
            if sugar < 70:
                s, a = "Low", "Eat fast-acting carbs."
            elif sugar <= 99:
                s, a = "Normal", "Maintain healthy diet."
            elif sugar <= 125:
                s, a = "Prediabetes", "Consult doctor and adopt diet changes."
            else:
                s, a = "High", "Seek medical advice."
            result = f"Blood Sugar: {sugar} mg/dL\nStatus: {s}\nAdvice: {a}"
            self.sugar_result.set(result)
            results["Blood Sugar"] = result
            self.refresh_results()
        except:
            messagebox.showerror("Error", "Invalid input for blood sugar.")

    # ---------- URINALYSIS FUNCTIONALITY ----------
    def create_urinalysis_content(self):
        win = tk.Toplevel(self.root)
        win.title("Urinalysis Checker")
        win.geometry("700x550")

        def dropdown(label, var, values):
            ttk.Label(win, text=label).pack(anchor="w")
            ttk.Combobox(win, textvariable=var, values=values).pack(fill="x", pady=2)

        dropdown("Pus Cells:", self.pus_cells, ["None", "0-5/hpf", "6-10/hpf", ">10/hpf"])
        dropdown("RBC:", self.rbc, ["None", "0-2/hpf", "3-5/hpf", ">5/hpf"])
        dropdown("Transparency:", self.transparency, ["Transparent", "Hazy", "Turbid"])
        dropdown("Squamous Cells:", self.squamous_cells, ["None", "Few", "Many"])
        dropdown("Urates:", self.urates, ["None", "Few", "Many"])
        dropdown("Symptoms Present?", self.symptoms, ["Yes", "No"])

        ttk.Button(win, text="Interpret", command=self.interpret_urinalysis).pack(pady=10)
        self.urinalysis_result = scrolledtext.ScrolledText(win, height=8)
        self.urinalysis_result.pack(fill="both", padx=10, pady=5)

    def interpret_urinalysis(self):
        findings, uti = [], False
        if self.pus_cells.get() in ["6-10/hpf", ">10/hpf"]:
            findings.append("High WBC – possible infection")
            uti = True
        if self.transparency.get() != "Transparent":
            findings.append("Urine not clear – possible infection")
            uti = True
        if self.symptoms.get() == "Yes":
            findings.append("Symptoms present – potential UTI")
            uti = True
        if self.rbc.get() in ["3-5/hpf", ">5/hpf"]:
            findings.append("Elevated RBC – irritation or infection")
        findings.append(f"UTI Detected: {'Yes' if uti else 'No'}")
        findings.append("Advice: Please consult a physician." if uti else "Advice: No signs of UTI.")
        result = "\n".join(findings)
        self.urinalysis_result.delete("1.0", tk.END)
        self.urinalysis_result.insert(tk.END, result)
        results["Urinalysis"] = result
        self.refresh_results()

    # ---------- SAVE SUMMARY TO TEXT FILE ----------
    def download_summary(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "w") as f:
                f.write("HEALTHTRACK WELLNESS RECEIPT\n==============================\n")
                for key, val in client_info.items():
                    f.write(f"{key}: {val}\n")
                f.write("\n==============================\n")
                for key, val in results.items():
                    f.write(f"{key} Result:\n{val}\n\n")
            messagebox.showinfo("Success", f"Summary saved to {filename}")

# ---------- MAIN APPLICATION LAUNCH ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = HealthTrackApp(root)
    root.mainloop()

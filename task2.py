import tkinter as tk
from tkinter import messagebox


class GradeManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Grade Tracker")

        self.grades = {}

        # Create UI components
        self.label_subject = tk.Label(master, text="Subject:")
        self.label_subject.grid(row=0, column=0)

        self.entry_subject = tk.Entry(master)
        self.entry_subject.grid(row=0, column=1)

        self.label_grade = tk.Label(master, text="Grade:")
        self.label_grade.grid(row=1, column=0)

        self.entry_grade = tk.Entry(master)
        self.entry_grade.grid(row=1, column=1)

        self.button_add = tk.Button(master, text="Add Grade", command=self.add_grade)
        self.button_add.grid(row=2, columnspan=2)

        self.button_calculate = tk.Button(master, text="Calculate Average", command=self.calculate_average)
        self.button_calculate.grid(row=3, columnspan=2)

        self.text_output = tk.Text(master, height=30, width=40)
        self.text_output.grid(row=4, columnspan=2)

    def add_grade(self):
        subject = self.entry_subject.get()
        try:
            grade = float(self.entry_grade.get())
            self.grades[subject] = grade
            self.entry_subject.delete(0, tk.END)
            self.entry_grade.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added grade for {subject}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric grade.")

    def calculate_average(self):
        if not self.grades:
            messagebox.showwarning("Warning", "No grades available to calculate.")
            return

        average = sum(self.grades.values()) / len(self.grades)
        letter_grade = self.determine_letter_grade(average)
        gpa = self.calculate_gpa(average)

        output = (
            f"Total subjects: {len(self.grades)}\n"
            f"Average grade: {average:.2f}\n"
            f"Letter grade: {letter_grade}\n"
            f"GPA: {gpa:.2f}"
        )

        self.text_output.delete(1.0, tk.END)  # Clear previous output
        self.text_output.insert(tk.END, output)

    def determine_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0


def main():
    root = tk.Tk()
    app = GradeManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()

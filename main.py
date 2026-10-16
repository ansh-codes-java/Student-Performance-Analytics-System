

''' Student Performance Analytics System'''

 
import numpy as np
import pandas as pd
import functions as fn  
 

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)
 
 
def print_heading(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)
 
 
def main():
    
    df = fn.load_data("students.csv")
 
    print_heading("1. DATASET OVERVIEW")
    print("Number of students :", df.shape[0])
    print("Number of columns  :", df.shape[1])
    print("Column names       :", list(df.columns))
    print("Missing values     :", df.isna().sum().sum())
    print()
    print("First 5 records:")
    print(df.head())
 
    
    df = fn.calculate_total_and_average(df)   
    df = fn.assign_grades_and_result(df)      
 
    print_heading("2. STUDENT-WISE REPORT")
    columns_to_show = ["Student_ID", "Name", "Department", "Total", "Average",
                       "Percentage", "Grade", "Result", "Attendance", "Attendance_Status"]
    print(df[columns_to_show].to_string(index=False))
 
    
    summary = fn.class_summary(df)
 
    print_heading("3. CLASS SUMMARY")
    print("Total students     :", summary["total_students"])
    print("Passed             :", summary["passed"])
    print("Failed             :", summary["failed"])
    print("Pass percentage    :", summary["pass_percentage"], "%")
    print("Class average      :", summary["class_average"])
    print("Class median       :", summary["class_median"])
    print("Standard deviation :", summary["std_dev"])
    print("Highest average    :", summary["highest_name"], "-", summary["highest_avg"])
    print("Lowest average     :", summary["lowest_name"], "-", summary["lowest_avg"])
    print("Average attendance :", summary["avg_attendance"], "%")
 
   
    subject_table = fn.subject_analysis(df)
 
    print_heading("4. SUBJECT-WISE ANALYSIS")
    print(subject_table.to_string(index=False))
 

    best_subject = ""
    best_average = 0
    weak_subject = ""
    weak_average = 100
 
    for i in range(len(subject_table)):
        name = subject_table.loc[i, "Subject"]
        avg = subject_table.loc[i, "Average"]
 
        if avg > best_average:
            best_average = avg
            best_subject = name
 
        if avg < weak_average:
            weak_average = avg
            weak_subject = name
 
    print()
    print("Best subject    :", best_subject, "(average", best_average, ")")
    print("Weakest subject :", weak_subject, "(average", weak_average, ")")
 
    
    print_heading("5. TOP 5 PERFORMERS")
    print(fn.top_performers(df, 5).to_string())
 

    print_heading("6. GRADE DISTRIBUTION")
    grade_counts = fn.grade_distribution(df)
 
    for grade in grade_counts.index:
        count = grade_counts[grade]
        print(grade, ":", count)
 

    print_heading("7. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df).to_string())
 

    print_heading("8. STUDENTS NEEDING ATTENTION")
 
    print("Failed students:")
    for i in range(len(df)):
        if df.loc[i, "Result"] == "FAIL":
           
            failed_in = ""
            for subject in fn.SUBJECTS:
                if df.loc[i, subject] < fn.SUBJECT_PASS_MARK:
                    failed_in = failed_in + subject + " "
            print("  -", df.loc[i, "Name"], "failed in:", failed_in)
 
    print()
    print("Students with attendance below", fn.ATTENDANCE_MIN, "%:")
    for i in range(len(df)):
        if df.loc[i, "Attendance_Status"] == "SHORTAGE":
            print("  -", df.loc[i, "Name"], ":", df.loc[i, "Attendance"], "%")
 
        
    df.to_csv("results.csv", index=False)
    print()
    print("Full report saved in results.csv")
 
 

if __name__ == "__main__":
    main()


import numpy as np
import pandas as pd


SUBJECTS = ["Physics", "Maths", "Chemistry", "Communication", "Programming"]


SUBJECT_PASS_MARK = 40
ATTENDANCE_MIN = 75
MAX_MARKS_PER_SUBJECT = 100
GRADE_RULES = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (40, "E"),
]



def load_data(path):

    df = pd.read_csv(path)


    df.columns = df.columns.str.strip()


    df = df.rename(columns={"Enroll no.": "Student_ID"})

    return df


def calculate_total_and_average(df):
    
    marks = df[SUBJECTS].to_numpy()

    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)

    maximum_total = len(SUBJECTS) * MAX_MARKS_PER_SUBJECT
    df["Percentage"] = np.round(df["Total"] / maximum_total * 100, 2)

    return df


def get_grade(average):

    for minimum_average, grade in GRADE_RULES:
        if average >= minimum_average:
            return grade

    return "F"


def get_result(subject_marks):

    for mark in subject_marks:
        if mark < SUBJECT_PASS_MARK:
            return "FAIL"

    return "PASS"


def assign_grades_and_result(df):
    result_list = []
    grade_list = []
    attendance_list = []


    for i in range(len(df)):


        marks = []
        for subject in SUBJECTS:
            marks.append(df.loc[i, subject])


        result = get_result(marks)

        if result == "PASS":
            grade = get_grade(df.loc[i, "Average"])
        else:
            grade = "F"

        if df.loc[i, "Attendance"] >= ATTENDANCE_MIN:
            attendance_status = "OK"
        else:
            attendance_status = "SHORTAGE"

        result_list.append(result)
        grade_list.append(grade)
        attendance_list.append(attendance_status)

    df["Result"] = result_list
    df["Grade"] = grade_list
    df["Attendance_Status"] = attendance_list

    return df


def class_summary(df):
    total_students = len(df)

    # count PASS and FAIL
    passed = int((df["Result"] == "PASS").sum())
    failed = int((df["Result"] == "FAIL").sum())

    pass_percentage = round(passed / total_students * 100, 2)

    class_average = round(float(np.mean(df["Average"])), 2)
    class_median = round(float(np.median(df["Average"])), 2)
    std_dev = round(float(np.std(df["Average"])), 2)

    highest_avg = df["Average"].max()
    highest_name = df[df["Average"] == highest_avg]["Name"].iloc[0]

    lowest_avg = df["Average"].min()
    lowest_name = df[df["Average"] == lowest_avg]["Name"].iloc[0]

    avg_attendance = round(float(np.mean(df["Attendance"])), 2)

    summary = {
        "total_students": total_students,
        "passed": passed,
        "failed": failed,
        "pass_percentage": pass_percentage,
        "class_average": class_average,
        "class_median": class_median,
        "std_dev": std_dev,
        "highest_name": highest_name,
        "highest_avg": highest_avg,
        "lowest_name": lowest_name,
        "lowest_avg": lowest_avg,
        "avg_attendance": avg_attendance,
    }

    return summary



def subject_analysis(df):
    rows = []  

    for subject in SUBJECTS:
        marks = df[subject]

        subject_average = round(float(np.mean(marks)), 2)
        highest = int(np.max(marks))
        lowest = int(np.min(marks))

        topper = df[marks == highest]["Name"].iloc[0]

        passed = int(np.sum(marks >= SUBJECT_PASS_MARK))
        failed = int(np.sum(marks < SUBJECT_PASS_MARK))

        row = {
            "Subject": subject,
            "Average": subject_average,
            "Highest": highest,
            "Lowest": lowest,
            "Topper": topper,
            "Passed": passed,
            "Failed": failed,
        }
        rows.append(row)


    return pd.DataFrame(rows)


def department_analysis(df):
    rows = []

    for department in df["Department"].unique():


        group = df[df["Department"] == department]

        row = {
            "Department": department,
            "Students": len(group),
            "Avg_Marks": round(float(np.mean(group["Average"])), 2),
            "Avg_Attendance": round(float(np.mean(group["Attendance"])), 2),
            "Passed": int((group["Result"] == "PASS").sum()),
        }
        rows.append(row)

    table = pd.DataFrame(rows)
    table = table.set_index("Department")

    # best department first
    table = table.sort_values("Avg_Marks", ascending=False)

    return table


def top_performers(df, n=5):

    ranked = df.sort_values(["Average", "Attendance"], ascending=False)

    ranked = ranked.head(n)


    ranked = ranked.reset_index(drop=True)
    ranked.index = ranked.index + 1

    return ranked[["Student_ID", "Name", "Department", "Total", "Average", "Grade"]]



def grade_distribution(df):
    grades = []
    for minimum_average, grade in GRADE_RULES:
        grades.append(grade)
    grades.append("F")

    counts = []
    for grade in grades:
        count = int((df["Grade"] == grade).sum())
        counts.append(count)

    return pd.Series(counts, index=grades)
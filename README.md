# Student Performance Analytics System

This is a Python project that reads student marks from a CSV file and finds useful results from it, like totals, averages, grades, pass/fail status, subject-wise performance and the top students. It is built with Python, NumPy and Pandas.

## Objective

Checking marks by hand for a whole class takes time and mistakes are easy. This project does the work automatically. After running it, we can quickly see:

- which student has the highest average
- which subject is the strongest and which is the weakest
- how many students passed and failed
- what the class average is
- which students need extra attention (failed or low attendance)

## Technologies Used

- Python 3
- NumPy, for calculations like sum, mean, median, standard deviation and correlation
- Pandas, for reading the CSV file, working with the table and saving the result

No other library is used.

## Dataset

The data is in `students.csv`. It has 20 students and 9 columns, and there are no missing values.

- `Enroll no.` (renamed to `Student_ID` in the code)
- `Name`
- `Department` (CSE, ECE, EE, ME, CE)
- `Physics`, `Maths`, `Chemistry`, `Communication`, `Programming` (marks out of 100)
- `Attendance` (in percent)

The data has a mix of toppers, average students, a few failed students and some students with low attendance, so the analysis shows different results.

## Rules Used

- A student passes only if he/she scores **40 or more in every subject**.
- Attendance below **75%** is counted as a shortage.
- A failed student always gets grade **F**.
- Grades are given by the average marks:

| Average | Grade |
|---|---|
| 90 and above | A+|
| 80 and above | A |
| 70 and above | B |
| 60 and above | C |
| 50 and above | D |
| 40 and above | E |
| below 40     | F |

## How It Works

The project has two Python files. `functions.py` has all the calculation functions, and `main.py` calls them one by one and prints the report.

1. **Load the data.** `load_data()` reads the CSV file into a Pandas DataFrame and renames the ID column.
2. **Check the data.** `main.py` prints the number of rows and columns, missing values and the first 5 records.
3. **Total and average.** `calculate_total_and_average()` takes the subject columns as a NumPy array and uses `np.sum` and `np.mean` to get the total, average and percentage of each student.
4. **Result and grade.** `assign_grades_and_result()` loops through every student, checks pass/fail with `get_result()`, gets the grade with `get_grade()`, and marks attendance as OK or SHORTAGE.
5. **Analysis.** The remaining functions work on the final table:
   - `class_summary()` gives passed/failed count, class average, median, standard deviation, highest and lowest student
   - `subject_analysis()` gives average, highest, lowest, topper and pass/fail count for each subject
   - `department_analysis()` gives department-wise average marks, attendance and pass count
   - `top_performers()` gives the top students with their rank
   - `grade_distribution()` counts how many students got each grade
6. **Students needing attention.** The program lists the failed students with the subjects they failed in, and the students with low attendance.
7. **Correlation.** `np.corrcoef()` is used to see how attendance and marks are related.
8. **Save.** The full report is saved in `results.csv`.

## Output

Run the program with `python main.py`. Some of the output:

```
Total students     : 20
Passed             : 17
Failed             : 3
Pass percentage    : 85.0 %
Class average      : 68.98
Highest average    : Pooja Tiwari - 93.0
Lowest average     : Vikram Yadav - 42.0
```

```
Best subject    : Communication (average 71.75 )
Weakest subject : Maths (average 66.85 )
```

```
   Student_ID           Name Department  Total  Average Grade
1          12   Pooja Tiwari        CSE    465     93.0    A+
2           4   Ananya Gupta        CSE    451     90.2    A+
3          20  Tanvi Rathore         EE    442     88.4     A
4           8   Priya Mishra        CSE    434     86.8     A
5          18   Divya Pandey        CSE    420     84.0     A
```

```
            Students  Avg_Marks  Avg_Attendance  Passed
Department
CSE                6      80.77           90.83       5
EE                 4      73.75           87.75       4
ECE                4      69.90           85.25       4
CE                 3      60.40           78.00       3
ME                 3      46.40           66.33       1
```

```
Failed students:
  - Riya Verma failed in: Maths
  - Vikram Yadav failed in: Physics Programming
  - Rahul Dubey failed in: Maths

Correlation between Attendance and Average: 0.99
```

## Final Outcome

The project works as expected and gives a complete report of the class without any manual calculation.

- 17 out of 20 students passed (85%) and the class average is 68.98.
- Pooja Tiwari is the topper with an average of 93.0.
- Communication has the best average and Maths has the lowest.
- CSE is the best department and ME is the weakest.
- 3 students failed and 5 students have attendance below 75%.
- Attendance and marks are strongly related in this data (correlation 0.99).

## Challenges and Learning

> Replace this part with your own experience. Write in your own words, 4 to 6 lines is enough.

Things you can write about:

- What error or problem did you face while running or writing the code, and how did you fix it?
- Which part was difficult to understand (for example loops, functions, NumPy or Pandas), and how did you understand it?
- What did you learn from this project?

## How to Run

Install the libraries and run the main file. Keep `main.py`, `functions.py` and `students.csv` in the same folder.

```
pip install numpy pandas
python main.py
```

After running, a file called `results.csv` is created with the complete report.

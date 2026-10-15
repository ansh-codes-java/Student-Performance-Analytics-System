Student Performance Analytics System
Overview
The Student Performance Analytics System is a Python-based data
analysis project that processes student marks and attendance to produce
a clear summary of academic performance. It helps review individual
results, compare subjects and departments, identify top performers, and
highlight students who may need additional academic support.
Technologies Used
- Python --- implements the program logic, functions, loops, and
  conditions.
- Pandas --- organizes student records in a DataFrame and supports
  tabular analysis.
- NumPy --- supports numerical calculations.
- CSV --- stores the student dataset and exported results.
Dataset
The dataset used in the project contains 20 student records and 9
columns:
- Student_ID
- Name
- Department
- Physics
- Maths
- Chemistry
- Communication
- Programming
- Attendance
The dataset overview reported no missing values.
Key Features
- Loads and inspects student data.
- Displays individual student totals, averages, percentages, grades,
  pass/fail status, and attendance.
- Summarizes class performance using statistics such as average,
  median, standard deviation, and pass percentage.
- Compares performance across subjects.
- Lists the top five students by average marks.
- Shows grade distribution.
- Compares performance across departments.
- Flags students who failed in one or more subjects or have attendance
  below 75%.
- Exports the analysis report to results.csv.
Results Summary
The project output showed the following results for the dataset:
  Metric                                       Result
  Total students                                   20
  Dataset columns                                   9
  Missing values                                    0
  Students passed                                  17
  Students failed                                   3
  Pass percentage                               85.0%
  Class average                                 68.98
  Class median                                   70.3
  Standard deviation                            15.79
  Average attendance                            83.5%
  Highest student average       Pooja Tiwari --- 93.0
  Lowest student average        Vikram Yadav --- 42.0
  Highest subject average     Communication --- 71.75
  Lowest subject average              Maths --- 66.85
How to Run
1. Make sure Python is installed.
2. Install the required libraries if they are not already installed:
   pip install pandas numpy
3. Keep the main Python file and the student dataset in the appropriate
   project folder.
4. Run the main Python program:
   python main.py
   If your main file has a different name, replace main.py with that
   filename.
Output
The program displays student-wise results and summaries for class
performance, subjects, top performers, grades, departments, and students
who may need attention. It also saves the report as results.csv.
Conclusion
The Student Performance Analytics System demonstrates how Python,
Pandas, and NumPy can be used to turn student records into useful
academic insights. It provides an organized view of student and class
performance and helps identify areas of strength and students who may
benefit from additional support.

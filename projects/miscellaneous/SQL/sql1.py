# sql1.py
"""Volume 1: SQL 1 (Introduction).
"""

import csv
import numpy as np
import sqlite3 as sql
from matplotlib import pyplot as plt

# Problems 1, 2, and 4
def student_db(
        db_file="projects/miscellaneous/SQL/students.db",
        student_info="projects/miscellaneous/SQL/student_info.csv",
        student_grades="projects/miscellaneous/SQL/student_grades.csv",
        ):
    """Connect to the database db_file (or create it if it doesn’t exist).
    Drop the tables MajorInfo, CourseInfo, StudentInfo, and StudentGrades from
    the database (if they exist). Recreate the following (empty) tables in the
    database with the specified columns.

        - MajorInfo: MajorID (integers) and MajorName (strings).
        - CourseInfo: CourseID (integers) and CourseName (strings).
        - StudentInfo: StudentID (integers), StudentName (strings), and
            MajorID (integers).
        - StudentGrades: StudentID (integers), CourseID (integers), and
            Grade (strings).

    Next, populate the new tables with the following data and the data in
    the specified 'student_info' 'student_grades' files.

                MajorInfo                         CourseInfo
            MajorID | MajorName               CourseID | CourseName
            -------------------               ---------------------
                1   | Math                        1    | Calculus
                2   | Science                     2    | English
                3   | Writing                     3    | Pottery
                4   | Art                         4    | History

    Finally, in the StudentInfo table, replace values of -1 in the MajorID
    column with NULL values.

    Parameters:
        db_file (str): The name of the database file.
        student_info (str): The name of a csv file containing data for the
            StudentInfo table.
        student_grades (str): The name of a csv file containing data for the
            StudentGrades table.
    """
    try:
        with sql.connect(db_file) as conn:
            cur = conn.cursor()
            tables_to_drop = [
                "MajorInfo",
                "CourseInfo",
                "StudentInfo",
                "StudentGrades",
                ]
            for table in tables_to_drop:
                cur.execute(f"DROP TABLE IF EXISTS {table};")

            tables_to_create = {
                "MajorInfo": {
                    "MajorID": "INTEGER",
                    "MajorName": "STRING",
                    },
                "CourseInfo": {
                    "CourseID": "INTEGER",
                    "CourseName": "STRING",
                    },
                "StudentInfo": {
                    "StudentID": "INTEGER",
                    "StudentName": "STRING",
                    "MajorID": "INTEGER",
                    },
                "StudentGrades": {
                    "MajorID": "INTEGER",
                    "CourseID": "INTEGER",
                    "Grade": "STRING",
                    },
            }
            for table, schema in tables_to_create.items():
                full_schema = ", ".join([
                    f"{c_name} {c_type}" for c_name, c_type in schema.items()
                    ])
                cur.execute(f"CREATE TABLE {table} ({full_schema});")

            # Populate data tables
            major_info = [
                (1, "Math"),
                (2, "Science"),
                (3, "Writing"),
                (4, "Art"),
            ]
            cur.executemany("INSERT INTO MajorInfo VALUES(?,?);", major_info)

            course_info = [
                (1, "Calculus"),
                (2, "English"),
                (3, "Pottery"),
                (4, "History"),
            ]
            cur.executemany("INSERT INTO CourseInfo VALUES(?,?);", course_info)

            with open(student_info, "r") as file:
                student_info_rows = list(csv.reader(file))
            cur.executemany("INSERT INTO StudentInfo VALUES(?,?,?)", student_info_rows)

            with open(student_grades, "r") as file:
                student_grades_rows = list(csv.reader(file))
            cur.executemany("INSERT INTO StudentGrades VALUES(?,?,?)", student_grades_rows)
    except:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()


# Problems 3 and 4
def earthquakes_db(db_file="earthquakes.db", data_file="us_earthquakes.csv"):
    """Connect to the database db_file (or create it if it doesn’t exist).
    Drop the USEarthquakes table if it already exists, then create a new
    USEarthquakes table with schema
    (Year, Month, Day, Hour, Minute, Second, Latitude, Longitude, Magnitude).
    Populate the table with the data from 'data_file'.

    For the Minute, Hour, Second, and Day columns in the USEarthquakes table,
    change all zero values to NULL. These are values where the data originally
    was not provided.

    Parameters:
        db_file (str): The name of the database file.
        data_file (str): The name of a csv file containing data for the
            USEarthquakes table.
    """
    try:
        with sql.connect(db_file) as conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS USEarthquakes;")
            cur.execute("CREATE TABLE USEarthquakes "
                        + "(Year INT, "
                        + "Month INT, "
                        + "Day INT, "
                        + "Hour INT, "
                        + "Minute INT, "
                        + "Second INT, "
                        + "Latitude FLOAT, "
                        + "Longitude FLOAT, "
                        + "Magnitude FLOAT);")

            with open("projects/miscellaneous/SQL/us_earthquakes.csv", "r") as file:
                earthquake_rows = list(csv.reader(file))

            print(earthquake_rows)

            cur.executemany("INSERT INTO USEarthquakes "
                            + "VALUES(?,?,?,?,?,?,?,?,?)",
                            earthquake_rows
                            )

    except:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()



# Problem 5
def prob5(db_file="students.db"):
    """Query the database for all tuples of the form (StudentName, CourseName)
    where that student has an 'A' or 'A+'' grade in that course. Return the
    list of tuples.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (list): the complete result set for the query.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6(db_file="earthquakes.db"):
    """Create a single figure with two subplots: a histogram of the magnitudes
    of the earthquakes from 1800-1900, and a histogram of the magnitudes of the
    earthquakes from 1900-2000. Also calculate and return the average magnitude
    of all of the earthquakes in the database.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (float): The average magnitude of all earthquakes in the database.
    """
    raise NotImplementedError("Problem 6 Incomplete")


def main():
    # # Testing problem 1
    # student_db()
    # with sql.connect("projects/miscellaneous/SQL/students.db") as conn:
    #     cur = conn.cursor()
    #     tables = [row[0] for row in cur.execute(
    #         "SELECT name FROM sqlite_master WHERE type='table';"
    #     )]
    #     for table in tables:
    #         cur.execute(f"SELECT * FROM {table};")
    #         print([d[0] for d in cur.description])

    # # Testing problem 2
    # with sql.connect("projects/miscellaneous/SQL/students.db") as conn:
    #     cur = conn.cursor()
    #     for table in tables:
    #         for row in cur.execute(f"SELECT * FROM {table};"):
    #             print(row)

    # Testing problem 3
    earthquakes_db("projects/miscellaneous/SQL/earthquakes.db")
    with sql.connect("projects/miscellaneous/SQL/earthquakes.db") as conn:
        cur = conn.cursor()
        tables = [row[0] for row in cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )]
        for table in tables:
            for row in cur.execute(f"SELECT * FROM {table};"):
                print(row)


if __name__ == "__main__":
    main()

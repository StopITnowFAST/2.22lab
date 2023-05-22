#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
import students
import sqlite3
import os
import numpy
from random import choice, randint


def test_select_all():
    """Full test"""
    conn = sqlite3.connect('test_db.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS marks (
            mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
            marks_list TEXT NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_group TEXT NOT NULL,
            mark_id INTEGER NOT NULL,
            FOREIGN KEY(mark_id) REFERENCES marks(mark_id)
        )
        """
    )

    db_list = []

    i = 0
    records = randint(2, 10)
    print(f"Количество записей в базу данных: {records}")

    group_variants = ('ПИЖ', 'ИВТ', 'ИСБ', 'ИСП')
    name = ('Никита ', 'Андрей ', 'Егор ', 'Сергей ', 'Данил ')
    sname = ('Ботвинкин', 'Ямбогло', 'Косарев', 'Шульга', 'Тагиев')

    while i < records:
        stud = ''.join(choice(name)) + ''.join(choice(sname))
        st_marks = str(numpy.random.randint(2, 5, 5))
        group = choice(group_variants)
        i += 1

        ans = {
            'student_name': stud,
            'student_group': group,
            'marks_list': st_marks
        }

        print(ans)
        db_list.append(ans)

        cursor.execute(
            """
                INSERT INTO marks (marks_list) 
                VALUES (?)
                """,
            (st_marks,),
        )

        mark_id = cursor.lastrowid

        cursor.execute(
            """
            INSERT INTO students (student_name, mark_id, student_group)
            VALUES (?, ?, ?)
            """,
            (str(stud), mark_id, group),
        )
        conn.commit()
        assert students.select_all('test_db.db') == db_list

    conn.close()
    os.remove('test_db.db')


def test_select_by_type():
    """Marks test"""
    conn = sqlite3.connect('test_db.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS marks (
            mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
            marks_list TEXT NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_group TEXT NOT NULL,
            mark_id INTEGER NOT NULL,
            FOREIGN KEY(mark_id) REFERENCES marks(mark_id)
        )
        """
    )

    db_list = []
    i = 0
    records = randint(10, 20)
    print(f"Всего студентов: {records}")
    print("Студенты с оценкой 2: ")

    group_variants = ('ПИЖ', 'ИВТ', 'ИСБ', 'ИСП')
    name = ('Никита ', 'Андрей ', 'Егор ', 'Сергей ', 'Данил ')
    sname = ('Ботвинкин', 'Ямбогло', 'Косарев', 'Шульга', 'Тагиев')

    while i < records:
        stud = ''.join(choice(name)) + ''.join(choice(sname))
        st_marks = str(numpy.random.randint(2, 5, 5))
        group = choice(group_variants)
        i += 1

        ans = {
            'student_name': stud,
            'marks_list': st_marks
        }

        if '2' in st_marks:
            print(ans)
            db_list.append(ans)

            cursor.execute(
                """
                    INSERT INTO marks (marks_list) 
                    VALUES (?)
                    """,
                (st_marks,),
            )

            mark_id = cursor.lastrowid

            cursor.execute(
                """
                INSERT INTO students (student_name, mark_id, student_group)
                VALUES (?, ?, ?)
                """,
                (str(stud), mark_id, group),
            )
            conn.commit()
            assert students.marks('test_db.db') == db_list
    print(f"Всего студентов с оценкой 2: {len(db_list)}")
    conn.close()
    os.remove('test_db.db')


if __name__ == "__main__":
    test_select_all()
    test_select_by_type()

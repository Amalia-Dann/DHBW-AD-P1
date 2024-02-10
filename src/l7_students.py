for _ in range(10):
    student = {
        "name": fake.name(),
        "age": random.randint(18, 25),
        "major": random.choice(["Computer Science", "Mathematics", "Physics"]),
        "gpa": round(random.uniform(2.0, 4.0), 2),
        "is_international": random.choice([True, False])
    }
    students.append(student)

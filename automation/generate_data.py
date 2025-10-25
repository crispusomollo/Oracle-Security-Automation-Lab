from faker import Faker
import csv, os
fake = Faker()
os.makedirs("data/generated", exist_ok=True)
with open("data/generated/dummy_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["EMP_NAME", "JOB_TITLE", "SALARY", "DEPT_ID"])
    for _ in range(50):
        writer.writerow([fake.name(), fake.job(), fake.random_int(3000, 15000), fake.random_int(1,3)])
print("[INFO] Dummy data generated in data/generated/dummy_data.csv")

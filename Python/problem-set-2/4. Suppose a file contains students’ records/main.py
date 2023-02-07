def sort_by_name(student_records):
 return sorted(student_records, key=lambda x: x[0])
student_records = []
with open("data.txt", "r") as file:
 for line in file:
  name, age = line.strip().split(",")
  student_records.append((name, age))
sorted_records = sort_by_name(student_records)
for name, age in sorted_records:
 print(f"{name}, {age}")

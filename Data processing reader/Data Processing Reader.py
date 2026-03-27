import csv

print("--- Data Entry Module ---")
num_students = int(input("Enter number of students: "))
student_data = []

for i in range(num_students):
    name = input(f"Enter name for student {i+1}: ")
    score = input(f"Enter score for {name}: ")
    student_data.append([name, score])

with open('student_marks.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerows(student_data)

print("\n--- Initializing Data Processing ---")

try:
    with open('student_marks.csv', 'r') as infile, \
         open('processed_results.csv', 'w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        header = next(reader)
        writer.writerow(header + ["Status"])
        
        print(f"{'Name':<10} | {'Score':<5} | {'Status':<6}")
        print("-" * 30)

        for row in reader:
            name = row[0]
            score = int(row[1]) 
            status = "Pass" if score >= 40 else "Fail"
            
            writer.writerow([name, score, status])
            
            print(f"{name:<10} | {score:<5} | {status:<6}")

    print(f"\n[Success] {num_students} records processed and saved.")

except FileNotFoundError:
    print("Error: Source file not found.")
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("HR-Employee-Attrition.csv")

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}\n")

print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Employee Attrition Analysis

print("\n" + "=" * 50)
print("EMPLOYEE ATTRITION")
print("=" * 50)

attrition = df["Attrition"].value_counts()

total = len(df)
left = attrition["Yes"]
stayed = attrition["No"]

print(f"Total Employees: {total}")
print(f"Employees Stayed: {stayed}")
print(f"Employees Left: {left}")
print(f"Attrition Rate: {(left / total) * 100:.2f}%")

plt.figure(figsize=(6,4))

attrition.plot(kind="bar")

plt.title("Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Department Analysis

print("\n" + "=" * 50)
print("EMPLOYEES BY DEPARTMENT")
print("=" * 50)

department_count = df["Department"].value_counts()

print(department_count)

plt.figure(figsize=(6,4))

department_count.plot(kind="bar")

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()

# Average Monthly Income

print("\n" + "=" * 50)
print("AVERAGE MONTHLY INCOME")
print("=" * 50)

avg_income = df.groupby("Department")["MonthlyIncome"].mean()

print(avg_income)

plt.figure(figsize=(6,4))

avg_income.plot(kind="bar")

plt.title("Average Monthly Income by Department")
plt.ylabel("Monthly Income")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()

# Attrition Rate by Department

print("\n" + "=" * 50)
print("ATTRITION RATE BY DEPARTMENT")
print("=" * 50)

department_attrition = (
    pd.crosstab(
        df["Department"],
        df["Attrition"],
        normalize="index"
    ) * 100
)

print(department_attrition)

plt.figure(figsize=(6,4))

department_attrition["Yes"].plot(kind="bar")

plt.title("Attrition Rate by Department")
plt.ylabel("Attrition (%)")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()

# Age Distribution

print("\n" + "=" * 50)
print("AGE DISTRIBUTION")
print("=" * 50)

print(f"Average Age: {df['Age'].mean():.2f}")

plt.figure(figsize=(7,4))

plt.hist(df["Age"], bins=15)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()


print("\n" + "=" * 50)
print("KEY INSIGHTS")
print("=" * 50)

print(f"• Overall Attrition Rate: {(left / total) * 100:.2f}%")
print(f"• Largest Department: {department_count.idxmax()}")
print(f"• Highest Average Income Department: {avg_income.idxmax()}")
print(f"• Average Employee Age: {df['Age'].mean():.1f} years")
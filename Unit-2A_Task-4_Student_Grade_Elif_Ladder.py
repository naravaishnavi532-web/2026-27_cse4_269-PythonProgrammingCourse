score = int(input("Enter the score out of 100: "))
if score >= 90:
    print(f"Grade A (marks:{score})")
elif score >=80 and score < 90:
    print(f"Grade B (marks:{score})")
elif score >=70 and score < 80:
    print(f"Grade C (marks:{score})")
else:
    print(f"Grade D (marks:{score})")

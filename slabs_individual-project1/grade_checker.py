def main():
    try:
        practical = int(input("Enter Practical Assessment mark (0-100): "))
        theory = int(input("Enter Theory Examination mark (0-100): "))

        if not (0 <= practical <= 100):
            print("Error: Practical mark must be between 0 and 100.")
            return
        if not (0 <= theory <= 100):
            print("Error: Theory mark must be between 0 and 100.")
            return

        final_mark = (practical * 0.40) + (theory * 0.60)
        print(f"Final weighted percentage: {final_mark:.2f}%")

        if final_mark >= 50:
            print("Status: PASS")
        else:
            print("Status: FAIL")

    except ValueError:
        print("Error: Please enter a numeric value only.")

if __name__ == "__main__":
    main()

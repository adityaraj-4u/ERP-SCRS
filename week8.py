import pandas as pd
import os

students_db = {
    "S101": {"name": "Alice", "program": "B.Tech", "courses": "CS101"},
    "S102": {"name": "Bob", "program": "B.Tech", "courses": ""}
}

def save_to_csv():
    data_list = []
    for s_id, data in students_db.items():
        data_list.append({
            "student_id": s_id,
            "name": data["name"],
            "program": data["program"],
            "registered_courses": data["courses"]
        })
    
    df = pd.DataFrame(data_list)
    df.to_csv("students_data.csv", index=False)
    print("[SUCCESS] Data saved to students_data.csv")

def load_from_csv():
    if os.path.exists("students_data.csv"):
        df = pd.read_csv("students_data.csv").fillna("")
        print("\n--- LOADING DATA FROM CSV ---")
        print(df)
        print("-----------------------------\n")
    else:
        print("[ERROR] File not found.")

print("[INFO] Simulating System Shutdown...")
save_to_csv()

print("[INFO] Simulating System Startup...")
load_from_csv()
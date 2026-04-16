# services/advisor_service.py
import pandas as pd
from utils.file_handler import load_csv, save_csv

def view_pending_requests():
    """Fetches all registrations that are waiting for advisor approval."""
    df = load_csv("data/registrations.csv")
    
    if df.empty or 'status' not in df.columns:
        print("No registration records or missing status column.")
        return []

    pending = df[df['status'] == 'Pending']
    if pending.empty:
        print(" No pending requests at this time.")
        return []
        
    for index, row in pending.iterrows():
        print(f"[{index}] Student: {row['student_id']} wants to take {row['course_code']}")
    return pending

def process_request(index_id, decision):
    """Allows advisor to set status to 'Approved' or 'Rejected'"""
    df = load_csv("data/registrations.csv")
    
    try:
        
        df.loc[index_id, 'status'] = decision
        save_csv(df, "data/registrations.csv")
        print(f" Request #{index_id} has been marked as: {decision}")
    except KeyError:
        print(" Invalid request ID.")

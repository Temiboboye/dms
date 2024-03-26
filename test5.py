import pandas as pd
from datetime import datetime, timedelta
import math
import numpy as np

# Assuming df is your DataFrame loaded from an Excel file
# For the purpose of demonstration, creating a sample DataFrame
df = pd.read_excel('out.xls')  # Adjust the path to your file
df_sorted = df.sort_values(by='PRIORITY', ascending=False)


# Simulation parameters
total_people = 25
hours_per_person_per_day = 8
current_date = datetime(2024, 1, 1)

# Initialize columns for start and end dates
df_sorted['Start Date'] = pd.NaT
df_sorted['End Date'] = pd.NaT
df_sorted['Day 1'] = ""
df_sorted['Day 2'] = np.nan
df_sorted['Day 3'] = pd.NaT
ongoing_tasks = []

daily_available_hours = total_people * hours_per_person_per_day

for index, row in df_sorted.iterrows():
    task_hours_needed = row['RESIL TIM(Hrs)'] * row['PEP RQ']
    people_required = row['PEP RQ']
    daily_hours_for_task = min(people_required * hours_per_person_per_day, daily_available_hours)
    task_hours_per_day = people_required * hours_per_person_per_day


    if daily_available_hours >= task_hours_per_day:
    # Assuming each task can start as soon as there are enough resources available from the start date
        days_needed = math.ceil(task_hours_needed / daily_hours_for_task)
        df_sorted.at[index, 'Start Date'] = current_date
        df_sorted.at[index, 'End Date'] = current_date + timedelta(days=days_needed - 1)
        task_time = task_hours_needed * people_required
        spill_hours = (task_time) - (task_hours_per_day)
        print(int(task_hours_per_day))
        df_sorted.at[index, 'Day 1'] = task_hours_per_day
        df_sorted.at[index, 'Day 2'] = spill_hours
        task_time_usage = min(task_time, task_hours_per_day)
        daily_available_hours -= task_time_usage
    elif (daily_available_hours < task_time_usage):
        # Move to the next day and reset available hours
        #current_date += timedelta(days=1)
        daily_available_hours = daily_available_hours + (total_people * hours_per_person_per_day)
        daily_hour_usage = daily_available_hours
        current_date += timedelta(days=1)
    # Update current_date for the next task (this logic might vary based on your actual scheduling needs)
    current_date += timedelta(days=days_needed)

# Assuming 'fin.xlsx' is your desired output Excel file
#output_excel_path = 'fin.xlsx'  # Update this path as needed
#df_sorted.to_excel(output_excel_path, index=False)

print(f"{df_sorted}.")

import pandas as pd
from datetime import datetime, timedelta
import math

# Load the DataFrame from the Excel file and sort by priority
df = pd.read_excel('out.xls')  # Adjust the path to your file
df_sorted = df.sort_values(by='PRIORITY', ascending=False)
output_excel_path = "fin.xlsx"
# Simulation parameters
total_people = 25
hours_per_person_per_day = 8
start_date = [datetime(2023, 1, 1)]
end_date = [datetime(2023, 1, 1)]
daily_hours = total_people * hours_per_person_per_day
spill_hourss = 0
# Initialize tracking for each task's start and end dates
#data_dict = {column: df[column].tolist() for column in df.columns}
#task_schedule = {}
data_dict = {column: df_sorted[column].tolist() for column in df_sorted.columns}
# Initialize a record of daily available hours (for all people combined)
daily_available_hours = total_people * hours_per_person_per_day
current_date = start_date
daily_hour_usage = daily_hours
df_sorted['Start Date'] = [[] for _ in range(len(df_sorted))]
df_sorted['End Date'] = [[] for _ in range(len(df_sorted))]
start_date = df_sorted['Start Date'] 
#print("TOp boy", df_sorted['End Date'])
# Track ongoing tasks to adjust available workers dynamically
ongoing_tasks = []

while not df_sorted.empty or ongoing_tasks:
    # Assign tasks that can be started on the current day
    for index, task in df_sorted.iterrows():
        task_hours_needed = task['RESIL TIM(Hrs)']
        people_required = task['PEP RQ']
        task_hours_per_day = people_required * hours_per_person_per_day

        
        
        # Check if there are enough available workers to start this task
        if daily_available_hours >= task_hours_per_day:
            # Schedule the task
            #start_date.append([current_date])
            #print(data_dict)
            # Calculate the end date and update the task schedule
            days_needed = math.ceil(task_hours_needed / hours_per_person_per_day)
            #print(task_hours_needed * people_required)
            #floating_date = current_date + timedelta(days=days_needed - 1)
            df_sorted.at[index, 'Start Date'] = start_date
            #end_date = current_date + timedelta(days=days_needed - 1)
            df_sorted.at[index, 'End Date'] = end_date
            #end_date.append([current_date + timedelta(days=days_needed - 1)])
            #data_dict['End Date'] = end_date
            task_time = task_hours_needed * people_required
            spill_hours = (task_time) - (task_hours_per_day)
            print(days_needed, spill_hours)
            # Add to ongoing tasks and adjust available hours
            ongoing_tasks.append((task_hours_needed, people_required))
            task_time_usage = min(task_time, task_hours_per_day)
            daily_available_hours -= task_time_usage
            #task_time_usage = min(task_time, task_hours_per_day)
            daily_hour_usage -= task_time_usage
            print("Daily usage", daily_hour_usage, )
            # Remove the task from the to-do list
            df_sorted = df_sorted.drop(index)
        elif (daily_available_hours < task_time_usage):
            # Move to the next day and reset available hours
            #current_date += timedelta(days=1)
            daily_available_hours = daily_available_hours + (total_people * hours_per_person_per_day)
            daily_hour_usage = daily_available_hours
            current_date += timedelta(days=1)
            
            #df_sorted['Start Date'].append(str(current_date))
            end_date = current_date +  timedelta(days= days_needed - 1)

    # Update ongoing tasks and available hours for the next day
    new_ongoing_tasks = []
    for task_hours_needed, people_required in ongoing_tasks:
        task_hours_per_day = people_required * hours_per_person_per_day
        task_hours_needed -= min(task_time, task_hours_per_day)
        if task_hours_needed > 0:

            end_date.append(current_date +  timedelta(days= days_needed))
            new_ongoing_tasks.append((task_hours_needed, people_required))
        else:
            # Task finished, update end date
            data_dict['End Date'] = current_date +  timedelta(days= days_needed)
    ongoing_tasks = new_ongoing_tasks
    #print(new_ongoing_tasks)
new_df = pd.DataFrame(data_dict)
print(new_df)
# Output the schedule for each task
for items in data_dict.items():
    #print(f"{task}: Start Date: {df_sorted['Start Date']}, End Date: {df_sorted['End Date']}, Work hours {days_needed}")
    print(items) 

import pandas as pd
import math

# Specify the path to your Excel file
input_excel_path = 'out.xls'  # Update this with the actual path to your Excel file
#output_excel_path = 'out.xls'  # Path where you want to save the sorted Excel file

# Specify the column name you want to sort by
sort_by_column = "TASKS"  # Replace 'YourColumnName' with the actual column name

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(input_excel_path)
data_dict = {column: df[column].tolist() for column in df.columns}
#print(data_dict)
# Sort the DataFrame by the specified column
# ascending=True for ascending order, set ascending=False for descending order

#tasks_name = df['TASKS']
#sorted_tasks = sorted(tasks_name, key=lambda x: int(x.split(" ")[-1]))
#df_sorted = df.sort_values(by='TASKS', key=lambda x: x.str.extract('(\d+)', expand=False).astype(int))


# Write the sorted DataFrame to a new Excel file
# If you're using a version of pandas that is 1.2.0 or newer, and it's an .xlsx file, the engine='openpyxl' is needed
#df_sorted.to_excel(output_excel_path, index=False, engine='openpyxl')
#print(df_sorted)
#print(f'The Excel file has been sorted by {sort_by_column} and saved to {output_excel_path}')
#print(sorted_tasks)
df_sorted = df.sort_values(by='PRIORITY', ascending=False)

def calculate_days(df):
    total_hours_per_day = 200  # Total available hours per day (25 people * 8 hours)
    task_days = {}  # Dictionary to store the number of days required for each task
    
    for index, row in df.iterrows():
        task_id = row['TASKS']
        required_hours = row['RESIL TIM(Hrs)'] * row['PEP RQ']
        # Calculate days needed, considering the constraint of working hours per person per day
        days_needed_round_up = math.ceil(max(required_hours / total_hours_per_day, row['RESIL TIM(Hrs)'] / 8))
        days_needed = max(required_hours / total_hours_per_day, row['RESIL TIM(Hrs)'] / 8)
        task_days[task_id] = days_needed
    
    return task_days

# Calculate the number of days required for each task
task_days = calculate_days(df_sorted)
tdays = 0
# Print the results
for task, days in task_days.items():
    
    print(f'{task} requires {days:.2f} days')
    tdays += days

print(tdays)

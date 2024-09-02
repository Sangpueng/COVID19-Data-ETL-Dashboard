# Use the official Apache Airflow image as the base
FROM apache/airflow:2.10.0

# Install any necessary dependencies for Dash, Plotly, Pandas, etc.
#RUN pip install dash plotly pandas sqlite3

# Copy the covid_dashboard.py script into the container
COPY covid_dashboard.py /app/covid_dashboard.py

# Set the working directory
WORKDIR /app

# Run the Dash application
CMD ["python", "covid_dashboard.py"]

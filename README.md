# COVID19-Data-ETL-Dashboard
End-to-end ETL pipeline and COVID-19 dashboard project

# Project Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline and the creation of an interactive dashboard to visualize COVID-19 case data. The project leverages Docker for managing the database environment, Apache Airflow for scheduling and orchestrating ETL tasks, and Python's Dash framework for data visualization.

# Table of Contents
- Project Overview
- Technical Stack
- Installation
- Project Structure
- ETL Process
- Dashboard
- Usage
- Screenshots
- Contributing
- License

# Technical Stack
- Programming Languages: Python
- Database Management: PostgreSQL (Dockerized), SQLite
- ETL Scheduling: Apache Airflow
- Data Visualization: Dash, Plotly
- Containerization: Docker
- Other Tools: Git, Pandas

# Installation
# Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.
- Docker and Docker Compose installed.
- Git installed and configured on your system.
- A GitHub account.

# Clone the Repository
- Clone this repository to your local machine using Git:

git clone https://github.com/your-username/COVID19-Data-ETL-Dashboard.git
cd COVID19-Data-ETL-Dashboard

# Set Up the Environment
1. Create a virtual environment:


2. Activate the virtual environment:
- On Windows:

- On macOS/Linux:

3. Install the required packages:

# Running the Dockerized PostgreSQL Database
1. Build and run the Docker containers:

2. Check if PostgreSQL and other services are running correctly:
PostgreSQL will run on port 5432.
Airflow webserver will be available on http://localhost:8080.


# Running the Airflow Scheduler
1. Access the Airflow web interface:
- Visit http://localhost:8080 in your browser.
2. Run the ETL pipeline:
- Once logged in to Airflow, trigger the ETL DAG manually or wait for it to run as per the schedule.

# Project Structure
![image](https://github.com/user-attachments/assets/eddd0a3a-20be-43b1-b4fc-527d60f2805a)

COVID19-Data-ETL-Dashboard/
│
├── README.md                # Project documentation
├── Dockerfile               # Dockerfile to build the container
├── docker-compose.yml       # Docker Compose file for setting up services
├── requirements.txt         # Python dependencies
├── covid_dashboard.py       # Main Dash application
└── data/
    └── healthcare_data.db   # SQLite database file (output from ETL)
    
# ETL Process
The ETL pipeline extracts COVID-19 case data, transforms it by applying a 7-day rolling average, and loads it into a SQLite database. The process is automated and scheduled using Apache Airflow.

# Extract
- Data is extracted from the COVID-19 dataset and loaded into a PostgreSQL database running in a Docker container.
# Transform
- Data is transformed using Python scripts, including aggregation and smoothing of the data with rolling averages.
# Load
- The transformed data is loaded into a SQLite database for efficient querying and visualization in the Dash application.

# Dashboard
The COVID-19 dashboard is built using Python Dash and visualizes the COVID-19 cases across different countries over time. The dashboard features:

- A dropdown menu to select countries/regions.
- A 7-day rolling average to smooth the data trends.
- An interactive date range slider.

# Usage
1. Start the Dash application:

python covid_dashboard.py

2. Access the dashboard:

- Navigate to http://localhost:8050 in your web browser.

3. Interact with the dashboard:
- Select countries/regions from the dropdown.
- Adjust the date range using the slider to focus on specific periods. 

# Screenshots


# Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

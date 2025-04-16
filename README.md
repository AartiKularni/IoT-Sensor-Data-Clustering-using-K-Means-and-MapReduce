🧠 IoT Sensor Data Clustering using K-Means and Hadoop MapReduce

This project implements Room Occupancy Detection by analyzing IoT sensor data using the K-Means clustering algorithm on the Hadoop MapReduce framework. It classifies sensor readings into "Occupied" and "Not Occupied" clusters and visualizes the results using Power BI.

📁 Dataset

Dataset used: Room Occupancy Detection Data Set (UCI Repository)

Preprocessing:

Removed Occupancy and Date columns

Retained only numerical features: Temperature, Humidity, Light, CO2, HumidityRatio

Saved as sensor_data.csv

🧮 Project Workflow

Step 1: Dataset Preparation

Cleaned and saved the dataset as sensor_data.csv in C:/BDA_Project/

Step 2: Hadoop Setup

Started Hadoop services using start-all.cmd

Created HDFS directories: hdfs dfs -mkdir /bda_projects
hdfs dfs -mkdir /bda_projects/clusterinput
hdfs dfs -put sensor_data.csv /bda_projects/clusterinput

Step 3: Initial Centroid Generation (Python)

Script: centroids.py

Generates centroids.txt with K=2 random centroids

Upload:
hdfs dfs -put centroids.txt /bda_projects/clusterinput

📦 MapReduce Programs

Phase 1: Iterative Clustering
Java Project Name: kmeans.hadoop

KMeansMapper.java: Calculates distance to centroids

KMeansReducer.java: Averages points to update centroids

KMeansDriver.java: Runs iteration, reads & writes centroids

Steps:

Run each iteration from Eclipse

Update and upload centroids.txt after each run

Repeat until centroids converge

Phase 2: Cluster Assignment
Java Project Name: cluster.assignment

ClusterAssignMapper.java: Assigns each point to nearest final centroid

ClusterAssignReducer.java: Outputs labeled data

ClusterAssignDriver.java: Sets up the job with Distributed Cache

Compile and export as KMeansClusterAssign.jar

🚀 Running JAR on Hadoop

hadoop jar C:/BDA_Project/KMeansClusterAssign.jar
cluster.assignment.ClusterAssignDriver
/clusterinput/sensor_data.csv
/bda_projects/cluster_output
/clusterinput/centroids.txt

hdfs dfs -get /bda_projects/cluster_output/part-r-00000 C:/BDA_Project/final_clustered_output.txt

📊 Power BI Visualization

Steps:

Open Power BI → Get Data → Text/CSV → Select final_clustered_output.txt

Transform Data:

Split columns by comma

Rename first column to Cluster

Create Scatter Plot:

X-axis: CO2

Y-axis: Temperature

Legend: Cluster

Insight:
Power BI visually separates "Occupied" and "Not Occupied" rooms based on CO2 and temperature levels, enabling data-driven space utilization strategies. This aids smart building automation for HVAC, lighting, and ventilation.

📂 File Structure

Python
├── centroids.py

Java
├── kmeans.hadoop
│ ├── KMeansMapper.java
│ ├── KMeansReducer.java
│ └── KMeansDriver.java
├── cluster.assignment
│ ├── ClusterAssignMapper.java
│ ├── ClusterAssignReducer.java
│ └── ClusterAssignDriver.java

JARs
├── KMeansClusterAssign.jar

Data
├── sensor_data.csv
└── centroids.txt

Output
└── final_clustered_output.txt

🎯 Features

Works with real IoT sensor data

Implements distributed clustering logic

Supports multiple iterations for convergence

Power BI dashboard for result visualization

Uses unsupervised learning without labels

📌 Future Improvements

Add real-time data streaming support

Increase number of clusters (K > 2)

Migrate to Apache Spark for faster performance

Integrate anomaly detection modules

📚 References

J. MacQueen, “Some Methods for Classification and Analysis of Multivariate Observations”

Dean & Ghemawat, “MapReduce: Simplified Data Processing”

Han, Kamber & Pei – Data Mining: Concepts and Techniques

Apache Hadoop Documentation – MapReduce Tutorial

UCI ML Repository – Room Occupancy Detection

👩‍💻 Author

Aarti Kulkarni
Bachelor of Technology in Electronics and Telecommunication
Pillai College of Engineering, University of Mumbai

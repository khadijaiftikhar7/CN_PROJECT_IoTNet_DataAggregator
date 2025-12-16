# IoT Smart Campus Network: Sensor Simulation & Analytics

**Project Name:** CN_PROJECT_IoTNet_SimulatedAnalytics
**Subject:** Computer Networks / IoT

## Project Overview

This repository contains the source code and documentation for the Smart Campus IoT Network. The system monitors critical environmental parameters including **Temperature, Humidity, CO2 levels, Noise, and Room Occupancy** across multiple zones.

**Simulation Approach:**
Instead of generating random "fake" numbers or requiring physical hardware, this project **simulates a live sensor network** by streaming data from a real-world dataset. The system treats the dataset records as incoming sensor payloads, allowing for a realistic demonstration of data processing, normalization, and visualization logic without the complexity of MQTT brokers or external databases.

## System Architecture

The system operates on a **Sensor Emulation Model**:

1.  **Sensor Emulation (Data Source):** A structured dataset (CSV) acts as the "Virtual Sensor Layer." Node-RED reads this data sequentially to mimic the periodic reporting of physical IoT devices.
2.  **Data Processing:** Raw data is parsed, normalized, and routed based on Room ID (e.g., Library, Cafe), replicating the edge processing done in real networks.
3.  **Visualization:** Processed streams are visualized on a "Glassmorphism" UI Dashboard for real-time monitoring.
4.  **Session Logging:** Recent sensor readings are maintained in a local history log for immediate analysis.

## Key Features

* **Realistic Sensor Simulation:** Uses actual dataset records to emulate the variability and trends of real-world environmental sensors.
* **Advanced User Interface:** Custom-built "Glassmorphism" interface with a professional industrial aesthetic.
* **Smart Filtering:** Global dropdown menu allows filtering the entire dashboard view (gauges, charts, status) to a single selected room.
* **Real-Time Analytics:** * Line charts visualize environmental trends (Temp, Humidity) over time.
    * Bar charts track dynamic occupancy levels.
* **Local History Log:** An auto-scrolling HTML table displays the most recent sensor packets processed during the current session.

## Dataset

This project utilizes a specific IoT dataset to drive the sensor simulation.

**Download the Dataset here:** > **[https://archive.ics.uci.edu/dataset/357/occupancy+detection]**

*Please ensure the dataset file is downloaded and configured in the Node-RED flow before running the simulation.*

## Technology Stack

* **Runtime Environment:** Node.js
* **IoT Platform:** Node-RED
* **Logic & Processing:** JavaScript (ES6)
* **Data Source:** CSV / Structured Dataset (Virtual Sensors)

---

## Project Structure

| Folder | Contents | Description |
| :--- | :--- | :--- |
| `dashboard_frontend` | `flows.json` | The final Node-RED flow configuration (Logic, Dashboard, Data Parsing). |
| `data` | `datatest.txt`, `datatest2.txt`, `datatraining.txt` | The dataset files used for simulating sensor readings. |

## Installation and Execution Guide

### Prerequisites

* Node.js (LTS version recommended)
* Node-RED
* **Required Palettes:** * `node-red-dashboard`
    * `node-red-contrib-ui-table` (if used for the history log)

### Step 1: Start Node-RED

1.  Open a Command Prompt or Terminal.
2.  Run Node-RED:
    ```bash
    node-red
    ```
3.  The server will start at `http://localhost:1880/`.

### Step 2: Import the Project Flow

1.  Open your browser and navigate to **[http://localhost:1880/](http://localhost:1880/)**.
2.  Go to **Menu (≡) > Import > Select File**.
3.  Choose the `flows.json` file from the `dashboard_frontend` folder in this repository.
4.  Click **Import**.

### Step 3: Connect the Dataset (Virtual Sensors)

1.  Locate the **"Read File"** or **"Data Injection"** node at the start of the flow.
2.  Double-click it and set the **File Path** to the location of your downloaded dataset (e.g., `C:\Users\YourName\Downloads\campus_data.csv`).
3.  Click **Done**.
4.  Click **Deploy** in the top right corner.

### Step 4: Access the Dashboard UI

Open your browser to view the live interface:

* **Live Dashboard UI:** **[http://localhost:1880/ui](http://localhost:1880/ui)**

---

## Troubleshooting

* **Dashboard is empty?** * Check that the dataset path in the "Read File" node is correct.
    * Ensure the CSV headers in the dataset match the keys expected by the flow (e.g., "Temperature", "Humidity").
* **"Context Collision" Warnings:** * These are safe to ignore; the system uses isolated context stores for room data to prevent data overlap between different virtual sensors.
# AutoStockSheet

This project is designed to track data on stock prices, PER (Price-to-Earnings Ratio), and EPS (Earnings Per Share), and store them into Google Sheets using Google Cloud Functions (GCF), Google Cloud Storage (GCS), and Pub/Sub in Google Cloud Platform (GCP).

## Introduction

AutoStockSheet automates the process of tracking and storing stock-related data into Google Sheets. It leverages GCP services for cloud-based data management and processing.

## Features

- Track stock prices, PER, and EPS
- Store data in Google Sheets automatically
- Utilize GCF, GCS, and Pub/Sub for efficient data handling

## Installation

Follow these steps to set up the project:

1. **Clone the repository**
    ```bash
    git clone https://github.com/hei8san/AutoStockSheet.git
    cd AutoStockSheet
    ```

2. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Google Cloud Platform (GCP)**
    - Create a GCP project and enable the necessary APIs (Google Sheets API, Cloud Functions, Cloud Storage, Pub/Sub)
    - Set up authentication and download the service account key

## Usage

1. **Configure Google Sheets and GCP settings**
    - Update the configuration in `config.py` with your Google Sheets and GCP details

2. **Run the main script**
    ```bash
    python main.py
    ```

## Project Structure

```plaintext
AutoStockSheet/
├── data_management.py      # Handles data fetching and processing
├── main.py                 # Main script to run the project
├── requirements.txt        # Project dependencies
└── README.md               # Project README

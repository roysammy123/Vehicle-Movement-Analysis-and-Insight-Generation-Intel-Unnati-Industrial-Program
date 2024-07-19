<a id="readme-top"></a>
<h1 align="center">Vehicle Movement Analysis and Insight Generation</h1>
<h2 align="center">Intel Unnati Industrial Program</h2>

<div align="center">
  
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![Open with Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://smartcampusparking.streamlit.app/)
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a> </li>
    <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#register-vehicle">Register Vehicle</a></li>
        <li><a href="#vehicle-log">Vehicle Log</a></li>
        <li><a href="#vehicle-entry">Vehicle Entry</a></li>
        <li><a href="#parking-insights">Parking Insights</a></li>
      </ul>
    </li>
    <li><a href="#contributors">Contributors</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![WhatsApp Image 2024-07-15 at 20 26 24_cecced33](https://github.com/user-attachments/assets/f38a5248-8adf-4da6-9a21-eeb50f475d9c)


- **Custom Trained YOLOv8n Model**
  - Demonstrates effectiveness for real-time license plate detection and vehicle movement analysis.
  - Trained on a manually annotated dataset of 433 images.
  - Shows high accuracy in detecting and locating license plates in various images.

- **Integration of Optical Character Recognition (OCR)**
  - Enhances model's practical utility.
  - Extracts text from detected license plates.
  - Allows for detailed analysis of vehicle movements.

- **Data Exploration and Visualization**
  - Utilized "indian_vehicle_parking_data.csv" dataset.
  - Identified significant patterns in vehicle entries, exits, and parking durations.
  - Revealed insights into occupancy and utilization patterns.

- **Key Insights**
  - Peak times of parking.
  - Frequently occupied parking slots.
  - Behaviour of frequent users.

- **Benefits for Parking Management**
  - Provides valuable information for optimizing parking management.
  - Highlights potential of edge AI in improving real-time parking solutions.
  - Makes parking management more efficient and user-friendly.


## Built With

Techstacks used for this project.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) <br>
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try) <br>
<img src="https://github.com/user-attachments/assets/63169f5b-77cd-4e04-90e3-d43467a2697e" alt="Made with Streamlit" width="200" height="80">


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is a list of things that you need to use the software and how to install them.<br>
Before you begin, ensure you have met the following requirements. You can install them by running the provided pip commands.
* Streamlit
  ```sh
  pip install streamlit
  ```
* Pandas
  ```sh
  pip install pandas
  ```
* Numpy
  ```sh
  pip install numpy
  ```
* OpenCV-Python-Headless
  ```sh
  pip install opencv-python-headless
  ```
* Pytesseract
  ```sh
  pip install pytesseract
  ```
* Ultralytics
  ```sh
  pip install ultralytics
  ```
* Matplotlib
  ```sh
  pip install matplotlib
  ```
* Seaborn
  ```sh
  pip install seaborn
  ```
* Torch
  ```sh
  pip install torch
  ```
* IPyWidgets
  ```sh
  pip install ipywidgets
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/roysammy123/Vehicle-Movement-Analysis-and-Insight-Generation-Intel-Unnati-Industrial-Program
   ```
2. Navigate to the project directory.
   ```sh
   cd Vehicle-Movement-Analysis-and-Insight-Generation-Intel-Unnati-Industrial-Program
   ```
3. Install the dependencies
   ```sh
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage

### Register Vehicle
![WhatsApp Image 2024-07-15 at 20 33 44_9eb2b46d](https://github.com/user-attachments/assets/a9e845a3-e117-4b9e-9185-777bfc7ce6f7)

This webpage allows users to upload an image of their vehicle, automatically detects the vehicle's license plate number, identifies the state of registration, and provides a mechanism for users to confirm the detected information. If the vehicle is already authorised for parking, the system informs the user accordingly otherwise adds the vehicle number to the authorised vehicles database

### Vehicle Log
![WhatsApp Image 2024-07-15 at 20 35 07_c632001b](https://github.com/user-attachments/assets/cea64cac-5be0-4148-bebb-b1e3d2e28801)

The "Vehicle Log" page allows users to enter a vehicle's license plate number, check if the vehicle is authorized for campus parking, and view detailed logs of the vehicle's entry and exit times, parking slot numbers, and total parking durations. This functionality helps users keep track of their vehicle's parking activities on campus.

### Vehicle Entry
![WhatsApp Image 2024-07-15 at 20 37 01_e72e6f7d](https://github.com/user-attachments/assets/b625564a-6f8a-4370-99c2-ad4605fff86a)

This webpage allows users to upload an image of a vehicle. Once an image is uploaded, the application displays the image and detects the vehicle number plate. Users are then prompted to confirm the accuracy of the detected number plate. Upon confirmation, if the vehicle is authorised, the webpage displays a message confirming the number plate as correct and grants access to the vehicle, indicated by a green "Access granted" message; else it denies access to the vehicle, indicated by a red “Access denied” message, and asks the user to register vehicle.

### Parking Insights
![WhatsApp Image 2024-07-15 at 20 50 44_719b199b](https://github.com/user-attachments/assets/d81b73e0-ffe4-4f9b-85c2-e70799d654ef)

This webpage is designed to provide insights into parking data. It features sections for finding the hour with the maximum cars parked on a selected date, viewing current parking slot occupancy by selecting a date and time, and searching for vehicle parking records by entering a plate number and date. The occupancy data is displayed in a table format, showing slot numbers, vehicle numbers, in times, and out times.



<!-- CONTRIBUTORS -->
## Contributors

1. **Manav Malhotra**  
   [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Manav173)

2. **Soumyajit Roy**  
   [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/roysammy123)

3. **Swarnav Kumar**  
   [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Swarnav-Kumar)

4. **Ishtaj Kaur Deol**  
   [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/ishtaj)



<!-- CONTACT -->
## Contact

Manav Malhotra -  manavmalhotra173@gmail.com <br>
Soumyajit Roy - roysoumyajit36@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/roysammy123/Vehicle-Movement-Analysis-and-Insight-Generation-Intel-Unnati-Industrial-Program.svg?style=for-the-badge
[contributors-url]: https://github.com/roysammy123/Vehicle-Movement-Analysis-and-Insight-Generation-Intel-Unnati-Industrial-Program/graphs/contributors
[license-shield]: https://img.shields.io/github/license/roysammy123/Vehicle-Movement-Analysis-and-Insight-Generation-Intel-Unnati-Industrial-Program.svg?style=for-the-badge
[license-url]: https://github.comroysammy123/Vehicle-Movement-Analysis-and-Insight-Generation-Intel-Unnati-Industrial-Program/blob/master/LICENSE.txt

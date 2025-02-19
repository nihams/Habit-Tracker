# Habit-Tracker

A desktop app using Electron to track everyday habits using Pixela.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Description

Habit-Tracker is a desktop application built with Electron that helps you track your everyday habits. It tracks reading progress based on the number of pages you read. It makes use of the Pixela API to visualize your progress over time.

## Features

- Tracks reading habits with user input.
- Pixela integration for progress visualisation.
- Simple and intuitive user interface based on Electron.

## Installation

To install and set up the Habit-Tracker application, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/nihams/Habit-Tracker.git
    cd Habit-Tracker
    ```

2. Install the required dependencies:
    ```bash
    npm install
    ```

3. Start the application using Electron Forge:
    ```bash
    npm run start
    ```

4. Package the app(optional) :
    ```bash
    npm run package
    ```

## Usage

1. Open the Habit-Tracker application.
2. **Set up your Pixela account**:
- Create an account on [Pixela](https://pixe.la).
- Generate a Pixela token and username.
- Update the file with your credentials.
4. Start tracking your daily habits by logging the number of pages read.
5. Visualize your progress over time using the charts provided by Pixela.

## Dependencies

Habit-Tracker depends on the following libraries and frameworks:

- **Electron**: For building cross-platform desktop applications using web technologies.
- **Electron Forge**: For packaging, distributing, and managing Electron applications with a simple and developer-friendly workflow. Streamlines the build process and supports multiple platforms.
- **JavaScript**: The primary programming language used in the project.
- **Python**: Used for accessing and updating the graph using the Pixela API.
- **CSS**: For styling the user interface.
- **HTML**: For structuring the application interface.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

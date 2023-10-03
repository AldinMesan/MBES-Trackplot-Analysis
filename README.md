# Project Documentation: MBES Trackplot Analysis

## Table of Contents

1. [Introduction](#1-introduction)
2. [Folder Structure](#2-folder-structure)
3. [Dependencies](#3-dependencies)
4. [Project Workflow](#4-project-workflow)
5. [Usage](#5-usage)
6. [Customization](#6-customization)
7. [Contributors](#7-contributors)


## 1. Introduction

### Purpose of the Project

The purpose of the project is to automate the analysis of Multibeam Echo Sounder (MBES) trackplot data. Specifically, the project aims to import trackplot files, calculate polygons for areas where the distance exceeds 50 meters between trackplots, and store the results as a shapefile with the required attributes.

### Project Overview

This project automates the analysis of MBES trackplot data, helping hydrographers and marine scientists efficiently identify and analyze areas of interest in survey data.

## 2. Folder Structure

### Description of Folders and Files

- **Input:** Contains the input trackplot file (`Task 2 Trackplots`) that serves as the source data for the analysis.
- **Output:** The calculated areas are stored as a single shapefile (`calculated_polygons.shp`) and placed in this folder.
- **Helpers:** Contains the script (`polygon_calculation.py`) responsible for calculating polygons between trackplots.
- **run.py:** The main script that coordinates the workflow by importing trackplot data, calling the polygon calculation code, and saving the results.

## 3. Dependencies

### Required Software and Libraries

- QGIS (Quantum GIS): A geospatial software application used for working with geospatial data.
- QGIS Python API: Used to interact with QGIS programmatically.

## 4. Project Workflow

### Explanation of How the Project Works

The project workflow involves the following steps:
1. Load the trackplot layer from the "Input" folder.
2. Import the helper script (`polygon_calculation.py`) for polygon calculation.
3. Calculate polygons for areas where the distance exceeds 50 meters between trackplots.
4. Save the calculated polygons as a shapefile in the "Output" folder.
5. Add the calculated polygons to the QGIS project.

## 5. Usage

### How to Run the Project

1. Ensure QGIS is installed.
2. Open the QGIS Python Console.
3. Run the `run.py` script to execute the project workflow.

## 6. Customization

### How to Customize the Project for Different Inputs or Requirements

Users can customize the project by:
- Replacing the `Task 2 Trackplots` file in the "Input" folder with their own trackplot data.
- Modifying the `polygon_calculation.py` script in the "Helpers" folder to adjust polygon calculation logic.

## 7. Contributors

### List of Contributors and Roles

- [Aldin Mešan]: Project lead and developer.

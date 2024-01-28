# TOPSIS Implementation

This repository contains a Python implementation of the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS). TOPSIS is a powerful multi-criteria decision-making method that assists in ranking a set of alternatives based on their proximity to the ideal solution.

## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Command-line Arguments](#command-line-arguments)
4. [Input](#input)
5. [Results](#results)
6. [Requirements](#requirements)
7. [Installation](#installation)
8. [Example](#example)
9. [Author](#author)
10. [License](#license)

## Introduction

The Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) is a well-established method for decision-making. This Python implementation allows you to easily apply TOPSIS to your decision matrix and obtain a ranked list of alternatives.

### Key Concepts:

- Decision Matrix: Represents alternatives and criteria.
- Weights: Assign importance to criteria.
- Impacts: Indicate whether higher or lower values are favorable.
- Normalization: Ensures all criteria are on a similar scale.
- Ideal and Worst Solutions: Represent best and worst possible outcomes.
- Similarity and Dissimilarity Measures: Calculate proximity to ideal and dissimilarity to worst.
- TOPSIS Score: Combines similarity and dissimilarity measures.
- Ranking: Alternatives are ranked based on TOPSIS scores.

## Usage

1. Ensure you have Python installed on your system.

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/cheshtabiala/Assignment-Topsis

3. Navigate to the project directory:

      ```bash
   git clone https://github.com/cheshtabiala/Assignment-Topsis

   
4.Run the TOPSIS script with the required command-line arguments:
               ```bash
   python topsis.py input_data.csv "1,1,1,2" "+,+,-,+" result.csv
            
            


5.The TOPSIS analysis will be performed, and the result will be saved to the specified CSV file.

## Command-line Arguments

- `<InputDataFile>`: Path to the input CSV file containing the decision matrix.

- `<Weights>`: Comma-separated weights for each criterion.

- `<Impacts>`: Comma-separated impact signs for each criterion (use '+' for beneficial criteria and '-' for non-beneficial criteria).

- `<ResultFileName>`: Desired name for the output CSV result file.


## Input


<img width="278" alt="Screenshot 2024-01-28 at 5 05 32 PM" src="https://github.com/cheshtabiala/Assignment-Topsis/assets/94442128/9e36c515-eaab-4b3a-b373-3a56cdf963c5">

## Results
<img width="472" alt="Screenshot 2024-01-28 at 5 05 01 PM" src="https://github.com/cheshtabiala/Assignment-Topsis/assets/94442128/a0276a4f-3f49-428e-9677-f8bb87cd6288">

<img width="655" alt="Screenshot 2024-01-28 at 5 04 40 PM" src="https://github.com/cheshtabiala/Assignment-Topsis/assets/94442128/38e64040-0571-4e3b-95f2-cc3af59e54f8">

## Requirements

- Python 3.x
- pandas
- numpy

## Installation

You can install the required packages using the following command:

   
                           ```bash
                           pip install -r requirements.

     

## Author

Cheshta Biala

## LICENSE

This project is licensed under the MIT License - see the LICENSE.md file for details.










   

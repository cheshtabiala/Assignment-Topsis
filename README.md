TOPSIS Implementation

This repository contains a Python implementation of the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS). TOPSIS is a powerful multi-criteria decision-making method that assists in ranking a set of alternatives based on their proximity to the ideal solution.


Table of Contents

1.	Introduction
2.	Usage
3.	Command-line Arguments
4.	Input
5.	Results
6.	Requirements
7.	Installation
8.	Example
9.	Author
10.	License


Introduction

The Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) is a well-established method for decision-making. This Python implementation allows you to easily apply TOPSIS to your decision matrix and obtain a ranked list of alternatives.

Key Concepts:

•	Decision Matrix: Represents alternatives and criteria.
•	Weights: Assign importance to criteria.
•	Impacts: Indicate whether higher or lower values are favorable.
•	Normalization: Ensures all criteria are on a similar scale.
•	Ideal and Worst Solutions: Represent best and worst possible outcomes.
•	Similarity and Dissimilarity Measures: Calculate proximity to ideal and dissimilarity to worst.
•	TOPSIS Score: Combines similarity and dissimilarity measures.
•	Ranking: Alternatives are ranked based on TOPSIS scores.

Usage

1.To use this TOPSIS implementation, follow the steps below:

Ensure you have Python installed on your system.

2.Clone this repository to your local machine:

git clone https://github.com/cheshtabiala/Assignment-Topsis
3.Navigate to the project directory:

cd your-repo

4.Run the TOPSIS script with the required command-line arguments:

python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
Example:

python topsis.py input_data.csv "1,1,1,2" "+,+,-,+" result.csv

5.The TOPSIS analysis will be performed, and the result will be saved to the specified CSV file.

Command-line Arguments

•	<InputDataFile>: Path to the input CSV file containing the decision matrix.

•	<Weights>: Comma-separated weights for each criterion.

•	<Impacts>: Comma-separated impact signs for each criterion (use '+' for beneficial criteria and '-' for non-beneficial criteria).

•	<ResultFileName>: Desired name for the output CSV result file.

Example:

python topsis.py input_data.csv "1,1,1,2" "+,+,-,+" result.csv

Input
 

Results

 
 


Requirements

•	Python 3.x
•	pandas
•	numpy

Installation

      You can install the required packages using the following command:

•	pip install -r requirements.txt
Example: 
pip install Topsis-CheshtaBiala-102103545

Author

Cheshta Biala

License

This project is licensed under the MIT License - see the LICENSE.md file for details.

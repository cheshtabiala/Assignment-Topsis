TOPSIS Implementation in 

This repository contains a Python implementation of the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS). TOPSIS is a multi-criteria decision-making method that helps in ranking a set of alternatives based on their proximity to the ideal solution.

Usage
To use this TOPSIS implementation, follow these steps:

1.Ensure you have Python installed on your system.

2.Clone this repository to your local machine:

        git clone https://github.com/cheshtabiala/Assignment-Topsis

3.Navigate to the project directory:

        cd your-repo
        
4.Run the TOPSIS script with the required command-line arguments:



        python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
        Example:python topsis.py input_data.csv "1,1,1,2" "+,+,-,+" result.csv

5.The TOPSIS analysis will be performed, and the result will be saved to the specified CSV file.

Command-line Arguments:

<InputDataFile>: Path to the input CSV file containing the decision matrix.

<Weights>: Comma-separated weights for each criterion.

<Impacts>: Comma-separated impact signs for each criterion (use '+' for beneficial criteria and '-' for non-beneficial criteria).

<ResultFileName>: Desired name for the output CSV result file.

        Example:python topsis.py input_data.csv "1,1,1,2" "+,+,-,+" result.csv

Requirements:
Python 3.x
pandas
numpy

Author:
Cheshta Biala

License:
This project is licensed under the MIT License - see the LICENSE.md file for details.
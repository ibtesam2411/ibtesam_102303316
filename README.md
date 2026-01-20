Title: TOPSIS Web Service Implementation

1.Methodology The TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) follows a structured mathematical approach to multi-criteria decision making.
Data Collection: Input CSV file containing the alternatives and criteria.

Data Pre-Processing: Normalizing the decision matrix to ensure comparability across different units.

Model Training: Applying weights to the normalized matrix based on criteria importance.

Model Testing: Calculating the distance of each alternative from the Ideal Best (+) and Ideal Worst (-) solutions.

Result Analysis: Computing the TOPSIS score and ranking the alternatives.

2.Description This web service allows users to upload a dataset and receive ranked results directly via email. It is built using Python (streamlit) and Pandas for efficient data processing.
Functionality: Automates the TOPSIS ranking process.

Core Library: Uses NumPy for matrix calculations and Pandas for CSV handling.

Input Requirements: A CSV file with at least three columns (the first being the object name).

Other Information: Includes automated email delivery of results using SMTP.

3.Input / Output The service requires specific inputs to calculate the relative closeness of each alternative to the ideal solution.
<img width="938" height="171" alt="538145543-7573b281-7485-445d-a1fe-f10d2052fcaa" src="https://github.com/user-attachments/assets/d384bea1-3638-43cd-89b0-b64ea1a7361b" />
4. PyPI Package The TOPSIS implementation is available as a Python package on PyPI.
PyPI Package Name: Topsis-MdIbtesam-102303316
<img width="1909" height="604" alt="Screenshot 2026-01-20 023458" src="https://github.com/user-attachments/assets/4e7f849b-c0c9-4746-95b3-07301e1d1868" />
Installation Command:

pip install Topsis-MdIbtesam-102303316
link-https://pypi.org/project/Topsis-MDIBTESAM-102303316/1.0.0/
Command Line Usage:

python topsis.py INPUT_FILE WEIGHTS IMPACTS OUTPUT_FILE

Example

python topsis.py data.csv "1,1,1,2" "+,+,-,+" result.csv
5.Live Link The application is deployed and accessible at the following address: https://ibtesam102303316-gwt8hfzbkjha7tplgl8hhy.streamlit.app/
6.Screenshot of the Interface The interface is designed to be clean and user-friendly, as shown below:
<img width="1071" height="663" alt="image" src="https://github.com/user-attachments/assets/ab07336e-e080-4ba5-9b9b-7de214d78034" />
7.Conclusion This project provides a complete and automated solution for TOPSIS-based decision making using both a command-line interface and a web-based application.
The program handles the following cases:

*Incorrect number of command-line arguments

*File not found exception

*Input file with less than three columns

*Non-numeric values in criteria columns

*Mismatch between number of weights, impacts, and criteria

*Invalid impact symbols

8.Conclusion: This project provides a complete and automated solution for TOPSIS-based decision making using both a command-line interface and a web-based application.

9.Author: Md Ibtesam

10.License: This project is intended for academic and educational use.

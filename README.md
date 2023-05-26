# Product Alternate Task 2

This repository contains the code implementation for the "Product Alternate Task 2" assignment. The assignment focuses on finding key differences 
between products in a given e-commerce store using Ai model.

## Task Description
The goal of this task is to develop a program that identifies key differences between products within a given e-commerce store. The program uses
Ai model to group similar products and then analyzes the product data to determine the key difference for each product within the groups.

## Files
The repository contains the following files:

- `FindKeyDifference.py`: This file contains the implementation of the `FindKeyDifference()` function, which takes a JSON object containing arrays of
-  similar product links and returns a JSON object outlining the key difference for each product within the groups.


## Usage
To use the `FindKeyDifference()` function, follow these steps:

1. Import the function into your Python script: `from FindKeyDifference import FindKeyDifference`

2. Pass a JSON object containing arrays of similar product links to the `FindKeyDifference()` function: `result = FindKeyDifference(product_links)`

3. The function will return a JSON object outlining the key difference for each product within the groups.

4. You can then process or display the results as per your requirements.

Please refer to the `test.py` file for an example usage of the `FindKeyDifference()` function.

## Testing
To test the code, you can use your own product links or the provided example links from various e-commerce stores. Ensure that the input JSON 
object contains valid product links.

## Contributing
Pull requests and contributions to enhance the functionality or fix any issues are welcome. Please feel free to open an issue if you encounter 
any problems or have suggestions for improvements.

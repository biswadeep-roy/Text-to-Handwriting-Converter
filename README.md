## Text to Handwriting Converter

Convert plain text into handwritten-style images using this simple Python script.

# Table of Contents

Overview
Getting Started
Usage
Customization
Font
Examples
Contributing
License

# Overview

This Python script allows you to convert plain text into a sequence of handwritten-style images. Each character in the input text is represented by a corresponding image in the "font" folder. The script combines these images to create a visual representation of the text, emulating a handwritten appearance.

# Getting Started

Clone the repository to your local machine:

``git clone https://github.com/biswadeep-roy/text-to-handwriting-converter.git
``

Install the required Python libraries:

``pip install pillow
``

# Usage

Run the script by providing a text file as input. If no input file is provided, the script will use the default "test.txt" file.

``python convert_text_to_handwriting.py input_file.txt
``

The script will generate an image file with the converted text.

# Customization

myfont/bg.png: Background image for the handwriting. You can replace this with your preferred background.

myfont/{char_code}.png: Handwritten-style images for each character. You can add or replace images to change the handwriting style.

115: Adjust the scaling factor for character spacing to fit your preferred layout.


# Font

The "font" folder contains individual character images that make up the handwriting style. You can customize or replace these images to change the appearance of the handwritten text.


# Examples

Here are some examples of how to use the script:

Convert a custom text file:

``python convert_text_to_handwriting.py custom_text.txt
``

Use the default "test.txt" file:

``python convert_text_to_handwriting.py
``
 
# Contributing

Contributions are welcome! If you have any ideas for improvements or new features, please open an issue or submit a pull request.

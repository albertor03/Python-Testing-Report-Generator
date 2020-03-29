# Python-Testing-Report-Generator

Report generator created in python with Jinja, Pdfkit and wkhtmltopdf software. The generator gets the data from a json file, the data is rendered with Jinja2 and created by pdkit and wkhtmltopdf.

## Table of contens:
* [Requirements](#Requirements)
* [Usage](#Usage)
* [Project structure](#Project-structure)
* [Built](#Built)
* [Contributing](#Contributing)
* [License](#License)

## Requirements

To use the report generator you need to install a couple of python libraries:

```python
pip install Jinja2 && pip install pdfkit
```
or install the libraries from the requirements.txt file that is in the project:
```python
pip install -r requirements.txt
```

You also need to install the [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html ) software
## Usage
To generate the reports you need to run the command:

```python
python Generator\Generator.py
```
The report will be generated in the Report folder

## Project structure
* **Data folder:** Here are the data.json files that contain the data to build the report and pdf_options.json to set the report parameters.
* **Generator folder:** contains the python class to generate the pdf report.
* **Report folder:** It will contain all the generated reports.
* **Templates folder:** from here you take the template to generate the reports.
* **requirements.txt file:** it has the necessary libraries to execute the generator.py class.

## Built
* [Python](https://www.python.org/)
* [Jinja](https://palletsprojects.com/p/jinja/)
* [Pdfkit](https://pdfkit.org/)
* [Wkhtmltopdf](https://wkhtmltopdf.org/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
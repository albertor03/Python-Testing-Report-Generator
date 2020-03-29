from datetime import datetime
import json
import sys

import pdfkit
from jinja2 import Environment, FileSystemLoader


class Generator:

    # Constructor
    def __init__(self):
        # Open json file
        with open('Data/data.json') as json_file:
            self.report_json = json.load(json_file)

        # Open json file
        with open('Data/pdf_options.json') as json_options_file:
            self.json_pdf_options = json.load(json_options_file)

        # Set the path of all json files
        self.path_to_template = 'Templates/'
        self.path_to_report = 'Report/'
        self.extension = '.pdf'
        self.date = datetime.now().strftime("%a") + " " + datetime.now().strftime("%b") + " " + datetime.now().\
            strftime("%d") + " " + datetime.now().strftime("%Y")
        self.app = 'Report Generator Python '

    # Get the html template
    def get_template(self):
        env = Environment(loader=FileSystemLoader(self.path_to_template))
        template = env.get_template("template.html")
        return template

    # Render the template with the data
    def template_rendering(self):
        render_template = self.get_template()
        results = self.report_json
        date = self.date
        summary = self.get_total_element()
        total = summary['Passed'] + summary['Failed'] + summary['Skipped']
        template = render_template.render(results=results, date=date, summary=summary, total=total)
        return template

    # Generate the pdf file
    def generate_pdf(self):
        date = self.date.replace(" ", "_")
        app = self.app.lower().replace(" ", "_").capitalize()
        file_name = str(self.path_to_report + app + date + self.extension)
        html = self.template_rendering()
        if sys.platform == 'win32':
            path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
            pdfkit.from_string(html, file_name, options=self.json_pdf_options, configuration=config)
        elif sys.platform == 'linux':
            pdfkit.from_string(html, file_name, options=self.json_pdf_options)

    def get_total_element(self):
        length = len(self.report_json)
        total = dict()
        passed = 0
        failed = 0
        skipped = 0
        item = 0
        while length > 0:
            if self.report_json[item]['Result'] == 'Passed':
                passed += 1
                item += 1
                length -= 1
            elif self.report_json[item]['Result'] == 'Failed':
                failed += 1
                item += 1
                length -= 1
            else:
                skipped += 1
                item += 1
                length -= 1
        total['Passed'] = passed
        total['Skipped'] = skipped
        total['Failed'] = failed
        return total


a = Generator()
a.generate_pdf()

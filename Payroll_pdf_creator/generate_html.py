# Functions to create different HTML layout 
import pandas as pd
import numpy as np
import pdfkit
import os


def generate_html_v1(row, logo_url, footer1_url, footer2_url):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
            h2, h3 {{
                font-size: 16px;
                color: #333;
                margin: 5px 0;
                font-weight: normal;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            /* layout of columns */
            table.fixed-columns {{
                table-layout: fixed;
            }}
            table.fixed-columns th,
            table.fixed-columns td {{
                width: 50%; /* fixed value */
            }}
            .header-img {{
                position: absolute;
                top: 20px;
                right: 20px;
                width: 120px;
            }}
            .footer-images {{
                margin-top: 80px;
                display: flex;
                justify-content: space-between; 
                align-items: center;
            }}
            .footer-img {{
                width: 420px; 
            }}
        </style>
    </head>
    <body>
        <img src="{logo_url}" class="header-img" alt="Logo">

        <br><br>

        <h1>Payroll</h1>

        <br><br>
        <h2><span style="font-weight: bold;">Month:</span> {row['Month']} {row['Year']}</h2>

        <table class="fixed-columns">
            <tr>
                <th>Name</th>
                <th>ID</th>
                <th>Start Date</th>
                <th>Type Contract</th>
                <th>Area</th>
                <th>Rol</th>
            </tr>
            <tr>
                <td>{row['First Name']} {row['Last Name']}</td>
                <td>{row['ID']}</td>
                <td>{row['Start Date']}</td>
                <td>{row['Contract Type']}</td>
                <td>{row['Area']}</td>
                <td>{row['Role']}</td>
            </tr>
        </table>

        <table class="fixed-columns">
            <tr><th colspan="2">Assets</th></tr>
            <tr><td>Base Salary</td><td>${row['Base Salary']}</td></tr>
            <tr><td>Gratification</td><td>${row['Gratification']}</td></tr>
            <tr><td>Seniority Bonus</td><td>${row['Seniority bonus']}</td></tr>
            <tr style="font-weight: bold;"><td>Total Taxable</td>
            <td>${row['Gross Salary']}</td></tr>
            <tr><td>Commuter Benefit</td><td>${row['Commuter Benefit']}</td></tr>
            <tr><td>Lunch Benefit</td><td>${row['Lunch Stipend']}</td></tr>
            <tr><td>Home Office Stipend</td><td>${row['Home Office Stipend']}</td></tr>
            <tr style="font-weight: bold;"><td>Total No Taxable</td>
            <td>${row['No Taxable']}</td></tr>
            <tr style="font-weight: bold;"><td>Total Assets</td>
            <td>${row['Assets']}</td></tr>
        </table>

        <br>

        <table class="fixed-columns">
            <tr><th colspan="2">Legal Discounts</th></tr>
            <tr><td>Health Insurance Deduction</td><td>${row['Health Insurance Deduction']}</td></tr>
            <tr><td>Retirement Plan Deduction</td><td>${row['Retirement Plan Deduction']}</td></tr>
            <tr><td>Unemployment Insurance</td><td>${row['Unemployment Insurance']}</td></tr>
            <tr><td>Union Dues</td><td>${row['union dues']}</td></tr>
            <tr><td>Income tax</td><td>${row['Income tax']}</td></tr>
            <tr><td>Total Discounts</td><td><strong>${row['Legal Discounts']}</strong></td></tr>
        </table>

        <table class="fixed-columns">
            <tr><td>Net Payment</td><td><strong>${row['Net Salary']}</strong></td></tr>
        </table>


        <div class="footer-images">
            <img src="{footer1_url}" class="footer-img left" alt="Footer Image 1">
            <img src="{footer2_url}" class="footer-img right" alt="Footer Image 2">
        </div>

    </body>
    </html>
    """
    return html_content



def generate_html_v2(row, logo_url, footer1_url, footer2_url):
    html_content = f"""
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            text-align: center;
            color: #333;
        }}
        h2, h3 {{
            font-size: 16px;
            color: #333;
            margin: 5px 0;
            font-weight: normal;
        }}
        .original-table {{
            width: 98.5%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        .assets-wrapper {{
            overflow: hidden; /* Clear floats for assets and Discounts */
            width: 100%;
            margin-top: 20px;
        }}
        .assets-table {{
            width: 48%;
            border-collapse: collapse;
            float: left;
            margin-right: 20px;
        }}
        .discounts-net-container {{ /* New container for Discounts and Net */
            float: left; /* Position to the right of Haberes */
            width: 48%;
        }}
        .discounts-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px; /* Space between Discounts and Net */
        }}
        .neto-table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}

        .neto-table td {{
            width: 50%;
            border: 1px solid #ccc;
            padding: 10px;
            vertical-align: top;
        }}
        .custom-table th, .custom-table td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }}
        .custom-table th {{
            background-color: #d9e8f5;
        }}
        .custom-table td:last-child {{
            text-align: right;
        }}
        .total-row {{
            font-weight: bold;
            background-color: #f2f2f2;
        }}
                    .header-img {{
                position: absolute;
                top: 20px;
                right: 20px;
                width: 120px;
            }}
            .footer-images {{
                margin-top: 80px;
                display: flex;
                justify-content: space-between; /* Empuja las imágenes a los extremos */
                align-items: center;
            }}
            .footer-img {{
                width: 420px; /* Ajusta según necesidad */
            }}
        </style>
    </style>
</head>
<body>
    <img src="{logo_url}" class="header-img" alt="Logo">

    <br><br>

    <h1>Payroll</h1>

    <br><br>
    <h2><span style="font-weight: bold;">Month:</span> {row['Month']} {row['Year']}</h2>

    <table class="custom-table" style="width: 98.5%;">
        <tr>
            <th>Nombre</th>
            <th>ID</th>
            <th>Start Date</th>
            <th>Type Contract</th>
            <th>Area</th>
            <th>Rol</th>
        </tr>
        <tr>
            <td>{row['First Name']} {row['Last Name']}</td>
            <td>{row['ID']}</td>
            <td>{row['Start Date']}</td>
            <td>{row['Contract Type']}</td>
            <td>{row['Area']}</td>
            <td>{row['Role']}</td>
        </tr>
    </table>

    <div class="assets-wrapper">
        <table class="custom-table assets-table">
            <tr><th colspan="2">Assets</th></tr>
            <tr><td>Base Salary</td><td>${row['Base Salary']}</td></tr>
            <tr><td>Gratification</td><td>${row['Gratification']}</td></tr>
            <tr><td>Seniority Bonus</td><td>${row['Seniority bonus']}</td></tr>
            <tr class="total-row"><td>Total Taxable</td><td>${row['Gross Salary']}</td></tr>
            <tr><td>Commuter Benefit</td><td>${row['Commuter Benefit']}</td></tr>
            <tr><td>Lunch Benefit</td><td>${row['Lunch Stipend']}</td></tr>
            <tr><td>Home Office Stipend</td><td>${row['Home Office Stipend']}</td></tr>
            <tr class="total-row"><td>Total No Taxable</td><td>${row['No Taxable']}</td></tr>
            <tr class="total-row"><td>Total Assets</td><td>${row['Assets']}</td></tr>
        </table>

        <div class="discounts-net-container">
            <table class="custom-table discounts-table">
                <tr><th colspan="2">Legal Discounts</th></tr>
                <tr><td>Health Insurance Deduction</td><td>${row['Health Insurance Deduction']}</td></tr>
                <tr><td>Retirement Plan Deduction</td><td>${row['Retirement Plan Deduction']}</td></tr>
                <tr><td>Unemployment Insurance</td><td>${row['Unemployment Insurance']}</td></tr>
                <tr><td>Union Dues</td><td>${row['union dues']}</td></tr>
                <tr><td>Income tax</td><td>${row['Income tax']}</td></tr>
                <tr class="total-row"><td>Total Discounts</td><td>${row['Legal Discounts']}</td></tr>
        </table>
            
        <table class="custom-table neto-table">
            <tr class="total-row">
                <td><strong>Account</strong><br>{row['Bank']} {row['Bank_Account_ID']}</td>
                <td><strong>Payment</strong><br>${row['Net Salary']}</td>
            </tr>
        </table>
        </div>
    </div>
    <div class="footer-images">
        <img src="{footer1_url}" class="footer-img left" alt="Footer Image 1">
        <img src="{footer2_url}" class="footer-img right" alt="Footer Image 2">
    </div>
</body>
</html>
"""

    return html_content


def generate_html_v3(row, logo_url, footer1_url,footer2_url):
    html_content = f"""
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}

        h1 {{
            text-align: center;
            color: #333;
        }}

        h2, h3 {{
            font-size: 16px;
            color: #333;
            margin: 5px 0;
            font-weight: normal;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}

        .custom-table th,
        .custom-table td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }}

        .custom-table th {{
            background-color: #d9e8f5;
        }}

        .total-row {{
            font-weight: bold;
            background-color: #f2f2f2;
        }}

        .assets-wrapper {{
            overflow: hidden;
            width: 100%;
            margin-top: 20px;
        }}

        .assets-table {{
            width: 48%;
            float: left;
            margin-right: 20px;
        }}

        .discounts-net-container {{
            float: left;
            width: 48%;
        }}

        .neto-table tr td {{
            border: none;
            text-align: left;
        }}

        .header-img {{
                position: absolute;
                top: 20px;
                right: 20px;
                width: 120px;
            }}

        .footer-images {{
            margin-top: 80px;
            display: flex;
            justify-content: space-between; /* Empuja las imágenes a los extremos */
            align-items: center;
        }}

        .footer-img {{
            width: 420px; /* Ajusta según necesidad */
        }}
    </style>
</head>
<body>
    <!-- Imagen superior izquierda -->
    <img src="{logo_url}" class="header-img" alt="Logo">

    <br>
    

    <h1>Payroll</h1>

    <br>
    <br>

    <h2><span style="font-weight: bold;">Month:</span> {row['Month']} {row['Year']}</h2>

    <table class="custom-table" style="width: 98.5%;">
        <tr>
            <th>Nombre</th>
            <th>ID</th>
            <th>Start Date</th>
            <th>Type Contract</th>
            <th>Area</th>
            <th>Rol</th>
        </tr>
        <tr>
            <td>{row['First Name']} {row['Last Name']}</td>
            <td>{row['ID']}</td>
            <td>{row['Start Date']}</td>
            <td>{row['Contract Type']}</td>
            <td>{row['Area']}</td>
            <td>{row['Role']}</td>
        </tr>
    </table>

    <div class="assets-wrapper">
        <table class="custom-table assets-table">
            <tr><th colspan="2">Assets</th></tr>
            <tr><td>Base Salary</td><td>${row['Base Salary']}</td></tr>
            <tr><td>Gratification</td><td>${row['Gratification']}</td></tr>
            <tr><td>Seniority Bonus</td><td>${row['Seniority bonus']}</td></tr>
            <tr class="total-row"><td>Total Taxable</td><td>${row['Gross Salary']}</td></tr>
            <tr><td>Commuter Benefit</td><td>${row['Commuter Benefit']}</td></tr>
            <tr><td>Lunch Benefit</td><td>${row['Lunch Stipend']}</td></tr>
            <tr><td>Home Office Stipend</td><td>${row['Home Office Stipend']}</td></tr>
            <tr class="total-row"><td>Total No Taxable</td><td>${row['No Taxable']}</td></tr>
            <tr class="total-row"><td>Total Assets</td><td>${row['Assets']}</td></tr>
        </table>

        <div class="discounts-net-container">
            <table class="custom-table discounts-table">
                <tr><th colspan="2">Legal Discounts</th></tr>
                <tr><td>Health Insurance Deduction</td><td>${row['Health Insurance Deduction']}</td></tr>
                <tr><td>Retirement Plan Deduction</td><td>${row['Retirement Plan Deduction']}</td></tr>
                <tr><td>Unemployment Insurance</td><td>${row['Unemployment Insurance']}</td></tr>
                <tr><td>Union Dues</td><td>${row['union dues']}</td></tr>
                <tr><td>Income tax</td><td>${row['Income tax']}</td></tr>
                <tr class="total-row"><td>Total Discounts</td><td>${row['Legal Discounts']}</td></tr>
            </table>
            
            <table class="custom-table neto-table">
                <tr class="total-row">
                    <td><strong>Account</strong></td>
                    <td>{row['Bank']} {row['Bank_Account_ID']}</td>
                </tr>
                <tr class="total-row">
                    <td><strong>Payment</strong></td>
                    <td>${row['Net Salary']}</td>
                </tr>
            </table>
        </div>
    </div>

    <!-- Imágenes finales -->
    <div class="footer-images">
        <img src="{footer1_url}" class="footer-img left" alt="Footer Image 1">
        <img src="{footer2_url}" class="footer-img right" alt="Footer Image 2">
        
    </div>

</body>
</html>
"""
    return html_content



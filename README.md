# Tracking COVID-19 Data at the University of Florida and in Alachua County

## Tracking

The Independent Florida Alligator is tracking COVID-19 cases in Florida, Alachua County and the University of Florida. 

If you have any questions about the data or its use please contact [rizaguirre@alligator.org](mailto:rizaguirre@alligator.org)

This data is publicly available for broad, noncommercial public use including by medical and public health researchers, policymakers, analysts and news media.

### Alachua.csv

This sheet contains tracked data of Alachua County confirmed cases and deaths. Also included are daily counts and 7-day averages to depict trends in the data. The sheet fields beyond cumulative counts are calculated using Excel.

Data is collected from [Florida Department of Health's COVID-19 Dashboard](https://experience.arcgis.com/experience/96dd742462124fa0b38ddedb9b25e429). Initial data was compiled from [The New York Times](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html).

### Florida.csv

This sheet contains tracked data of Florida confirmed cases and deaths. Also included are daily counts and 7-day averages to depict trends in the data. The sheet fields beyond cumulative counts are calculated using Excel.

Data is collected from [Florida Department of Health's COVID-19 Dashboard](https://experience.arcgis.com/experience/96dd742462124fa0b38ddedb9b25e429). Initial data was compiled from [The New York Times](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html) and [The COVID Tracking Project](https://covidtracking.com/data/state/florida).

### uf.csv

This sheet results from the `ufcovid.py` scraper that scrapes data from [UF Health's COVID-19 Testing Dashboard](https://coronavirus.ufhealth.org/screen-test-protect-2/about-initiative/testing-dashboard/) daily. The fields match those from the dashboard.

### ufcovid.py

Python script designed to scrape data from [UF Health's COVID-19 Testing Dashboard](https://coronavirus.ufhealth.org/screen-test-protect-2/about-initiative/testing-dashboard/).

from reader import read_csv
from pdf_generator import generate_pdf

if __name__ == "__main__":
    data = read_csv("app/sample_data.csv")
    generate_pdf(data, "salary_report.pdf")
    print("PDF report generated successfully")

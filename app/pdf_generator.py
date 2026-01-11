from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

def generate_pdf(data, output_path):
    pdf = SimpleDocTemplate(output_path, pagesize=A4)

    table_data = [["Name", "Department", "Salary"]]
    for row in data:
        table_data.append([row["name"], row["department"], row["salary"]])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (2, 1), (2, -1), "RIGHT"),
    ]))

    pdf.build([table])

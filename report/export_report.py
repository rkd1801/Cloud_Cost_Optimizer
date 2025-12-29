import os
from datetime import datetime

def get_desktop_path():
    # Works reliably even with OneDrive
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    if not os.path.exists(desktop):
        # Fallback for OneDrive Desktop
        desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

    os.makedirs(desktop, exist_ok=True)
    return desktop

def export_html_report(data):
    desktop_path = get_desktop_path()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"cloud_cost_report_{timestamp}.html"
    filepath = os.path.join(desktop_path, filename)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Cost Optimization Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                padding: 40px;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
            }}
            table {{
                margin: auto;
                border-collapse: collapse;
                width: 70%;
                background-color: #ffffff;
            }}
            th, td {{
                padding: 12px 16px;
                border: 1px solid #ddd;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
        </style>
    </head>
    <body>
        <h1>Cloud Cost Optimization Report</h1>
        <table>
            <tr>
                <th>Metric</th>
                <th>Value</th>
            </tr>
    """

    for key, value in data.items():
        html_content += f"""
            <tr>
                <td>{key}</td>
                <td>{value}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ HTML report exported successfully to:\n{filepath}")
    import webbrowser
    webbrowser.open(f"file:///{filepath}")

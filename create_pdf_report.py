#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os

def create_pdf_report():
    """Создает PDF отчет из markdown файла"""
    
    # Читаем markdown файл
    with open('design_analysis_report.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    
    # Конвертируем markdown в HTML
    md = markdown.Markdown(extensions=['tables', 'fenced_code'])
    html_content = md.convert(markdown_content)
    
    # Создаем полный HTML документ
    full_html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Анализ дизайна сайта фотографа</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            h1, h2, h3 {{
                color: #2c3e50;
                border-bottom: 2px solid #eee;
                padding-bottom: 10px;
            }}
            
            h1 {{
                font-size: 2.5em;
                text-align: center;
            }}
            
            h2 {{
                font-size: 1.8em;
                color: #34495e;
            }}
            
            h3 {{
                font-size: 1.4em;
                color: #7f8c8d;
            }}
            
            code {{
                background-color: #f8f9fa;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }}
            
            pre {{
                background-color: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
            }}
            
            blockquote {{
                border-left: 4px solid #3498db;
                margin: 0;
                padding-left: 20px;
                font-style: italic;
            }}
            
            .highlight {{
                background-color: #fff3cd;
                padding: 10px;
                border-radius: 5px;
                margin: 10px 0;
            }}
            
            hr {{
                border: none;
                height: 2px;
                background: linear-gradient(to right, #3498db, #9b59b6);
                margin: 30px 0;
            }}
            
            @page {{
                size: A4;
                margin: 2cm;
                @top-center {{
                    content: "Анализ дизайна сайта фотографа";
                    font-size: 10pt;
                    color: #666;
                }}
                @bottom-center {{
                    content: counter(page);
                    font-size: 10pt;
                    color: #666;
                }}
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Создаем CSS для PDF
    css = CSS(string='''
        @page {
            size: A4;
            margin: 2cm;
        }
        
        body {
            font-size: 11pt;
        }
        
        h1 {
            font-size: 24pt;
            page-break-after: avoid;
        }
        
        h2 {
            font-size: 18pt;
            page-break-after: avoid;
            margin-top: 20pt;
        }
        
        h3 {
            font-size: 14pt;
            page-break-after: avoid;
        }
        
        .page-break {
            page-break-before: always;
        }
    ''')
    
    # Создаем PDF
    font_config = FontConfiguration()
    
    try:
        HTML(string=full_html).write_pdf(
            'design_analysis_report.pdf',
            stylesheets=[css],
            font_config=font_config
        )
        print("✅ PDF отчет успешно создан: design_analysis_report.pdf")
        
        # Проверяем размер файла
        file_size = os.path.getsize('design_analysis_report.pdf')
        print(f"📄 Размер файла: {file_size / 1024:.1f} KB")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при создании PDF: {e}")
        return False

if __name__ == "__main__":
    create_pdf_report()

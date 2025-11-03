#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import re

def create_pdf_report():
    """Создает PDF отчет из markdown содержимого"""
    
    # Читаем markdown файл
    with open('design_analysis_report.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Создаем PDF документ
    doc = SimpleDocTemplate(
        "design_analysis_report.pdf",
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Получаем стили
    styles = getSampleStyleSheet()
    
    # Создаем собственные стили
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=20,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor='darkblue'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=12,
        textColor='darkblue'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=8,
        spaceBefore=8,
        textColor='darkgreen'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )
    
    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=9,
        backgroundColor='lightgray',
        borderColor='black',
        borderWidth=1,
        borderPadding=5
    )
    
    # Разбираем содержимое на блоки
    story = []
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            story.append(Spacer(1, 6))
            continue
            
        if line.startswith('# '):
            # Заголовок 1 уровня
            text = line[2:].strip()
            story.append(Paragraph(text, title_style))
            story.append(Spacer(1, 12))
            
        elif line.startswith('## '):
            # Заголовок 2 уровня
            text = line[3:].strip()
            story.append(Paragraph(text, heading_style))
            
        elif line.startswith('### '):
            # Заголовок 3 уровня
            text = line[4:].strip()
            story.append(Paragraph(text, subheading_style))
            
        elif line.startswith('```'):
            # Пропускаем блоки кода для упрощения
            continue
            
        elif line.startswith('**') and line.endswith('**'):
            # Жирный текст
            text = f"<b>{line[2:-2]}</b>"
            story.append(Paragraph(text, normal_style))
            
        elif line.startswith('*'):
            # Курсив
            text = f"<i>{line[1:]}</i>"
            story.append(Paragraph(text, normal_style))
            
        elif line.startswith('- '):
            # Пункты списка
            text = f"• {line[2:]}"
            story.append(Paragraph(text, normal_style))
            
        elif line.startswith('---'):
            # Разделитель
            story.append(Spacer(1, 20))
            story.append(Paragraph("_" * 50, normal_style))
            story.append(Spacer(1, 20))
            
        else:
            # Обычный текст
            if line:
                # Экранируем специальные символы для ReportLab
                line = line.replace('&', '&')
                line = line.replace('<', '<')
                line = line.replace('>', '>')
                story.append(Paragraph(line, normal_style))
    
    # Создаем PDF
    try:
        doc.build(story)
        print("✅ PDF отчет успешно создан: design_analysis_report.pdf")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при создании PDF: {e}")
        return False

if __name__ == "__main__":
    create_pdf_report()

from django.shortcuts import render, redirect

from .models import ProfileDetail
from .forms import ProfileDetailForm

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import re


def home(request):
    allprofile=ProfileDetail.objects.all()
    if request.method=='POST':
        resume=ProfileDetail()
        resume.file=request.FILES['file1']
        resume.save()
        output_string = StringIO()
        with open(resume.file.path, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)

        resume_text=output_string.getvalue()
        email=re.findall('\S+@\S+', resume_text)

        mobile=re.findall('\d{10}|\d{3}-\d{8}|\d{4}-\d{7}',resume_text)

        for i in email:
            resume.email=i
        for i in mobile:
            resume.number=i
        resume.save()
        allprofile=ProfileDetail.objects.all()
        return render(request, 'resume_parser.html', {'allprofile':allprofile})
    else:
        return render(request, 'resume_parser.html',{'allprofile':allprofile})

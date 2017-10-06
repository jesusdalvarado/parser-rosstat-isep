- pip install pdfminer.six

----------

- url: <http://www.gks.ru/wps/wcm/connect/rosstat_main/rosstat/ru/statistics/publications/catalog/doc_1140087276688>?
- save current word or pdf locally
- transform to something readable (xml/csv)
  - ```python D:\Continuum\Anaconda3\Scripts\pdf2txt.py -p 4 oper.pdf -t xml > oper.xml```
- must emit cells by row 
- emit name-freq-date-value dict

----------

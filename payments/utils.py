from django.template.loader import render_to_string
from django.http import HttpResponse
def render_pdf_from_template(template_src, context_dict={}):
    try:
        from weasyprint import HTML
        html_string = render_to_string(template_src, context_dict)
        html = HTML(string=html_string)
        result = html.write_pdf()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=receipt.pdf'
        response.write(result)
        return response
    except Exception:
        html_string = render_to_string(template_src, context_dict)
        return HttpResponse(html_string)

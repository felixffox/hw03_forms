from datetime import datetime

def year(request):
    """Добавляет переменную с текущим годом."""
    a = datetime.today().year
    return {'year' : a}
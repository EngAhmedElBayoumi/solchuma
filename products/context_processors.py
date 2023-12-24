from .models import category


def categories(request):
    # Assuming you want all categories available in the base template
    all_categories = category.objects.all()
    return {'all_categories': all_categories}

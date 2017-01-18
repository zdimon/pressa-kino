from main.models import Page

def menu(request):
   context_data = dict()
   context_data['menu'] = Page.objects.all.filter(is_menu=True)
   print context_data['menu']
   import pdb; pdb.set_trace()
   return context_data

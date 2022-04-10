from django.urls import reverse_lazy

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from .models import Familiar
from .forms import FamiliarForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
 

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class FamiliarCreateView(CreateView):
    model = Familiar
    template_name = "persona/add.html"
    form_class = FamiliarForm
    
    success_url = reverse_lazy('persona_app:registro_correcto')

    def form_valid(self, form):
        Familiar = form.save(commit=False) 
        Familiar.full_name = Familiar.first_name + ' ' + Familiar.last_name
        Familiar.save()
        return super(FamiliarCreateView, self).form_valid(form)


class UpdateSuccessView(TemplateView):
    template_name = "persona/update_success.html"


class FamiliarUpdateView(UpdateView):
    model = Familiar
    template_name = "persona/update.html"
    form_class = FamiliarForm
    success_url = reverse_lazy('persona_app:actualizacion-exitosa')


class ListFamiliares(ListView):
    template_name = 'persona/list_all.html'
    context_object_name = 'lista_familiares'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Familiar.objects.filter(
            full_name__icontains = palabra_clave
        )

        return lista


class FamiliarDetailView(DetailView):
    model = Familiar
    template_name = "persona/detalle_familiar.html"
 
    def get_context_data(self, **kwargs):
        context = super(FamiliarDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Mi Familia'
        return context
    

class FamiliarDeleteView(DeleteView):
    model = Familiar
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:actualizacion-exitosa')

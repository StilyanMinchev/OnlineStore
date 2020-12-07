from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from store.forms import FilterForm, WatchCreateForm
from store.models import Watch


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }


def index(request):
    params = extract_filter_values(request.GET)
    order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
    watches = Watch.objects.filter(name__icontains=params['text']).order_by(order_by)

    # for watch in watches:
    #     watch.can_delete = watch.created_by_id == request.user.id
    #     watch.can_edit = watch.created_by_id == request.user.id

    context = {
        'watches': watches,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
    }

    return render(request, 'index.html', context)


def watch_details(request, pk, slug=None):
    watch = Watch.objects.get(pk=pk)
    # if slug and watch.name.lower() != slug.lower():
    #     return redirect('404')
    context = {
        'watch': watch,
    }

    return render(request, 'watches/details.html', context)


# @group_required(groups=['Regular User'])
@login_required
def create(req):
    if req.method == 'GET':
        context = {
            'form': WatchCreateForm(),
            'current_page': 'create',
        }

        return render(req, 'create.html', context)
    else:
        form = WatchCreateForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
            'current_page': 'create',
        }

        return render(req, 'create.html', context)

# class Create(LoginRequiredMixin, FormView):
#     form_class = WatchCreateForm
#     template_name = 'create.html'
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

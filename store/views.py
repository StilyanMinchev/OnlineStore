from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic as views

from store.forms import FilterForm, WatchCreateForm, CommentForm
from store.models import Watch, Like


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

    context = {
        'watches': watches,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
    }

    return render(request, 'index.html', context)


# @login_required
# def watch_details(request, pk, slug=None):
#     watch = Watch.objects.get(pk=pk)
#     if slug and watch.name.lower() != slug.lower():
#         return redirect('404')
#     context = {
#         'can_delete': request.user == watch.user.user,
#         'can_edit': request.user == watch.user.user,
#         'can_like': request.user != watch.user.user,
#         'has_liked': watch.like_set.filter(user_id=request.user.userprofile.id).exists(),
#         'can_comment': request.user != watch.user.user,
#         'watch': watch,
#     }
#
#     return render(request, 'watches/details.html', context)

class WatchDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Watch
    template_name = 'watches/details.html'
    context_object_name = 'watch'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        watch = context[self.context_object_name]
        context['form'] = CommentForm()
        context['can_delete'] = self.request.user == watch.user.user
        context['can_edit'] = self.request.user == watch.user.user
        context['can_like'] = self.request.user != watch.user.user
        context['has_liked'] = watch.like_set.filter(user_id=self.request.user.userprofile.id).exists()
        context['can_comment'] = self.request.user != watch.user.user
        context['comments'] = list(watch.comment_set.all())

        return context


# @group_required(groups=['Regular User'])
@login_required
def create(request):
    if request.method == 'GET':
        context = {
            'form': WatchCreateForm(),
            'current_page': 'create',
        }

        return render(request, 'create.html', context)
    else:
        form = WatchCreateForm(request.POST, request.FILES)
        form.instance.user = request.user.userprofile
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
            'current_page': 'create',
        }

        return render(request, 'create.html', context)


# def delete_watch(request, pk):
#     watch = Watch.objects.get(pk=pk)
#     if request.method == 'GET':
#         context = {
#             'watch': watch,
#         }
#
#         return render(request, 'delete_watch.html', context)
#     else:
#         watch.delete()
#         return redirect('index')


class DeleteWatchView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Watch
    template_name = 'delete_watch.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        watch = self.get_object()
        if watch.user_id != request.user.userprofile.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


# def edit_watch(request, pk):
#     watch = Watch.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = WatchCreateForm(instance=watch)
#
#         context = {
#             'form': form,
#             'watch': watch,
#         }
#
#         return render(request, 'edit_watch.html', context)
#     else:
#         form = WatchCreateForm(
#             request.POST,
#             instance=watch
#         )
#         if form.is_valid():
#             form.save()
#             # return redirect('watches/details.html', watch.pk)
#             return redirect('index')
#
#         context = {
#             'form': form,
#             'watch': watch,
#         }
#
#         return render(request, f'edit_watch.html', context)


class UpdateWatchView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'edit_watch.html'
    model = Watch
    form_class = WatchCreateForm

    def get_success_url(self):
        url = reverse_lazy('watch details', kwargs={'pk': self.object.id})
        return url


# def like_watch(request, pk):
#     like = Like.objects.filter(user_id=request.user.userprofile.id, watch_id=pk).first()
#     if like:
#         like.delete()
#     else:
#         watch = Watch.objects.get(pk=pk)
#         like = Like(test=str(pk), user=request.user.userprofile)
#         like.watch = watch
#         like.save()
#     return redirect('watch details', pk)

class LikeWatchView(views.View):
    @staticmethod
    def get(request, **kwargs):
        user_profile = request.user.userprofile
        watch = Watch.objects.get(pk=kwargs['pk'])

        like = watch.like_set.filter(user_id=user_profile.id).first()
        if like:
            like.delete()
        else:
            like = Like(
                user=user_profile,
                watch=watch,
                test='as'
            )
            like.save()

        return redirect('watch details', watch.id)


class CommentWatchView(views.FormView):
    template_name = 'watches/details.html'
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user.userprofile
        comment.watch = Watch.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('watch details', self.kwargs['pk'])

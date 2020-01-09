from django.http import JsonResponse
from django.template.loader import render_to_string

class AjaxCreateMixin:
    template_partial_form = ''
    template_partial_list = ''

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            form = self.get_form()
            data = dict()
            data['html_form'] = render_to_string(self.template_partial_form, {'form': form}, request=request)
            return JsonResponse(data)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = dict()
            list_name = self.get_context_object_name(self.object) + '_list'
            data['form_is_valid'] = True
            data['html_list'] = render_to_string(self.template_partial_list, {list_name: self.model.objects.all()})
            return JsonResponse(data)
        return response

    def form_invalid(self, form):
        if self.request.is_ajax():
            data = dict()
            data['form_is_valid'] = False
            data['html_form'] = render_to_string(self.template_partial_form, {'form': form}, request=self.request)
            return JsonResponse(data)
        return super().form_invalid(form)


class AjaxUpdateMixin:
    template_partial_form = ''
    template_partial_list = ''

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            form_class = self.get_form_class()
            form = form_class(instance=self.get_object())
            data = dict()
            data['html_form'] = render_to_string(self.template_partial_form, {'form': form, 'object': self.get_object()}, request=request)
            return JsonResponse(data)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = dict()
            list_name = self.get_context_object_name(self.object) + '_list'
            data['form_is_valid'] = True
            data['html_list'] = render_to_string(self.template_partial_list, {list_name: self.model.objects.all()})
            return JsonResponse(data)
        return response

    def form_invalid(self, form):
        if self.request.is_ajax():
            data = dict()
            data['form_is_valid'] = False
            data['html_form'] = render_to_string(self.template_partial_form, {'form': form, 'object': self.get_object()}, request=self.request)
            return JsonResponse(data)
        return super().form_invalid(form)


class AjaxDeleteMixin:
    template_partial_form = ''
    template_partial_list = ''

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            data = dict()
            data['html_form'] = render_to_string(self.template_partial_form, {'object': self.get_object()}, request=request)
            return JsonResponse(data)
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if self.request.is_ajax():
            data = dict()
            list_name = self.get_context_object_name(self.object) + '_list'
            data['form_is_valid'] = True
            data['html_list'] = render_to_string(self.template_partial_list, {list_name: self.model.objects.all()})
            return JsonResponse(data)
        return response
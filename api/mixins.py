from datetime import datetime
from django.contrib.auth import get_user_model

class OrderFilterMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all active users and add to context
        context['users'] = get_user_model().objects.filter(is_active=True).order_by('first_name')
        return context

    def get_queryset(self):
        # Get the base queryset from the parent class
        queryset = super().get_queryset()
        
        # Get filter parameters
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        status = self.request.GET.get('status')
        owner_id = self.request.GET.get('owner')

        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            queryset = queryset.filter(order_Created__date__gte=start_date)
        
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            queryset = queryset.filter(order_Created__date__lte=end_date)

        if status:
            queryset = queryset.filter(status=status)

        if owner_id:
            queryset = queryset.filter(owner=owner_id)

        return queryset.order_by('-order_Created') 
from datetime import datetime

class OrderFilterMixin:
    def apply_filters(self, queryset):
        # Get filter parameters
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        status = self.request.GET.get('status')

        # Apply filters if provided
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            queryset = queryset.filter(order_Created__date__gte=start_date)
        
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            queryset = queryset.filter(order_Created__date__lte=end_date)

        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by('-order_Created') 
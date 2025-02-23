from datetime import datetime

class OrderFilterMixin:
    def get_queryset(self):
        # Get the base queryset from the parent class
        queryset = super().get_queryset()
        
        # Apply filters if they exist
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        status = self.request.GET.get('status')

        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            queryset = queryset.filter(order_Created__date__gte=start_date)
        
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            queryset = queryset.filter(order_Created__date__lte=end_date)

        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by('-order_Created') 
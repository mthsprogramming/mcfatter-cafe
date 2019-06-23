from django.contrib import admin
from .models import BlogPost, Category, Menu, MenuItem, MealType, Order, Ticket, CafeProfile, BlogPostImage, Specials
from django import forms

# Admin for the cafe app

class BlogPostForm(forms.ModelForm):
    post_text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['post_title']}),
        (None, {'fields': ['post_text']}),
        ('Date information', {'fields': ['pub_date']}),
        (None, {'fields': ['category']}),
        ('Images', {'fields': ['images']}),
    ]

    #form = BlogPostForm
    list_display = ('post_title', 'post_text', 'pub_date', 'category', 'was_published_recently')
    list_filter = ['pub_date', 'category']
    search_fields = ['post_text']

class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'is_complete', 'email', 'date')

class MenuItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['price']}),
        (None, {'fields': ['menu']}),
        (None, {'fields': ['type']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['image']}),
        (None, {'fields': ['available']}),
        ('Nutritional information', {'fields': ['calories']}),
        (None, {'fields': ['fat']}),
        (None, {'fields': ['sat_fat']}),
        (None, {'fields': ['trans_fat']}),
        (None, {'fields': ['cholesterol']}),
        (None, {'fields': ['sodium']}),
        (None, {'fields': ['carbs']}),
        (None, {'fields': ['dietary_fiber']}),
        (None, {'fields': ['sugar']}),
        (None, {'fields': ['protein']}),
    ]

    list_display = ('name', 'price', 'calories')


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Customer information', {'fields': ['user']}),
        (None, {'fields': ['order_for']}),
        ('Time information', {'fields': ['time_placed']}),
        (None, {'fields': ['pickup_time']}),
        (None, {'fields': ['is_ready']}),
        ('Order information', {'fields': ['items']}),
        (None, {'fields': ['instructions']}),
        (None, {'fields': ['total']}),
    ]

    list_display = ('items', 'is_ready', 'time_placed', 'order_for', 'pickup_time')


admin.site.register(BlogPostImage)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MealType)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Specials)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(CafeProfile)

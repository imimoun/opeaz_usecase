from django.contrib import admin

from .models import (
    CommercialCondition,
    Document,
    Flyer,
    Groupement,
    Laboratory,
    Pharmacy,
    PharmacyGroupement,
)


@admin.register(Groupement)
class GroupementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'groupement',)
    list_filter = ('groupement',)
    search_fields = ('name', 'groupement__name',)


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name',)
    search_fields = ('name', 'code',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'laboratory', 'created_at',)
    list_filter = ('laboratory', 'created_at',)
    search_fields = ('name', 'laboratory__name',)
    readonly_fields = ('created_at',)


@admin.register(Flyer)
class FlyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'laboratory', 'start_at', 'end_at',)
    list_filter = ('laboratory', 'start_at', 'end_at',)
    search_fields = ('title', 'laboratory__name',)


@admin.register(CommercialCondition)
class CommercialConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'laboratory', 'year',)
    list_filter = ('laboratory', 'year',)
    search_fields = ('name', 'laboratory__name', 'text',)


@admin.register(PharmacyGroupement)
class PharmacyGroupementAdmin(admin.ModelAdmin):
    list_display = ('id', 'groupement',)
    list_filter = ('groupement',)
    search_fields = ('groupement__name',)

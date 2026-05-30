from django.contrib import admin

from .models import (
    TreeEntity,
    TreeFolder,
    TreeFile,
    SharedTreeElement,
)


@admin.register(TreeEntity)
class TreeEntityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
        "original_entity_ct",
        "original_entity_id",
    )
    raw_id_fields = ("original_entity_ct",)


@admin.register(TreeFolder)
class TreeFolderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
        "name",
        "tree_entity",
    )
    list_filter = ("tree_entity",)
    search_fields = ("name",)
    raw_id_fields = (
        "tree_entity",
        "tree_folder",
    )


@admin.register(TreeFile)
class TreeFileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
        "tree_entity",
        "original_file_ct",
        "original_file_id",
    )
    list_filter = ("tree_entity", "original_file_ct")
    search_fields = ("external_id",)
    raw_id_fields = (
        "tree_entity",
        "tree_folder",
        "original_file_ct",
    )


@admin.register(SharedTreeElement)
class SharedTreeElementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tree_entity",
        "original_tree_element_ct",
        "original_tree_element_id",
    )
    raw_id_fields = (
        "tree_entity",
        "original_tree_element_ct",
    )

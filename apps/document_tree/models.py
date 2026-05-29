import uuid

from django.contrib.contenttypes.fields import (
    GenericForeignKey,
)
from django.contrib.contenttypes.models import (
    ContentType,
)
from django.db import (
    models,
)
from django.db.models.signals import (
    post_delete,
)
from django.dispatch import (
    receiver,
)

from apps.opeaz_heart.models import (
    CommercialCondition,
    Document,
    Flyer,
    Groupement,
    Laboratory,
    Pharmacy,
)


class TreeEntity(
    models.Model,
):
    id = models.BigAutoField(
        primary_key=True,
    )
    external_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    original_entity_ct = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in': [
                'groupement',
                'laboratory',
                'pharmacy',
            ],
        },
    )
    original_entity_id = models.PositiveIntegerField()
    original_entity = GenericForeignKey(
        'original_entity_ct',
        'original_entity_id',
    )


class TreeFolder(
    models.Model,
):
    id = models.BigAutoField(
        primary_key=True,
    )
    tree_folder = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subfolders',
    )
    external_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    name = models.CharField(
        max_length=255,
    )
    tree_entity = models.ForeignKey(
        'TreeEntity',
        on_delete=models.CASCADE,
        related_name='folders',
    )


class TreeFile(
    models.Model,
):
    id = models.BigAutoField(
        primary_key=True,
    )
    tree_folder = models.ForeignKey(
        'TreeFolder',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='files',
    )
    external_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    tree_entity = models.ForeignKey(
        'TreeEntity',
        on_delete=models.CASCADE,
        related_name='files',
    )
    original_file_ct = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in': [
                'commercialcondition',
                'document',
                'flyer',
            ],
        },
    )
    original_file_id = models.PositiveIntegerField()
    original_file = GenericForeignKey(
        'original_file_ct',
        'original_file_id',
    )


class SharedTreeElement(
    models.Model,
):
    id = models.BigAutoField(
        primary_key=True,
    )
    tree_entity = models.ForeignKey(
        'TreeEntity',
        on_delete=models.CASCADE,
        related_name='shared_elements',
    )
    original_tree_element_ct = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in': [
                'treefile',
                'treefolder',
            ],
        },
    )
    original_tree_element_id = models.PositiveIntegerField()
    original_tree_element = GenericForeignKey(
        'original_tree_element_ct',
        'original_tree_element_id',
    )


@receiver(
    post_delete,
    sender=Groupement,
)
@receiver(
    post_delete,
    sender=Pharmacy,
)
@receiver(
    post_delete,
    sender=Laboratory,
)
def delete_tree_entity(
    sender,
    instance,
    **kwargs,
):
    content_type = ContentType.objects.get_for_model(
        model=sender,
    )
    TreeEntity.objects.filter(
        original_entity_ct=content_type,
        original_entity_id=instance.id,
    ).delete()


@receiver(
    post_delete,
    sender=Document,
)
@receiver(
    post_delete,
    sender=Flyer,
)
@receiver(
    post_delete,
    sender=CommercialCondition,
)
def delete_tree_file(
    sender,
    instance,
    **kwargs,
):
    content_type = ContentType.objects.get_for_model(
        model=sender,
    )
    TreeFile.objects.filter(
        original_file_ct=content_type,
        original_file_id=instance.id,
    ).delete()


@receiver(
    post_delete,
    sender=TreeFolder,
)
@receiver(
    post_delete,
    sender=TreeFile,
)
def delete_shared_tree_element(
    sender,
    instance,
    **kwargs,
):
    content_type = ContentType.objects.get_for_model(
        model=sender,
    )
    SharedTreeElement.objects.filter(
        original_tree_element_ct=content_type,
        original_tree_element_id=instance.id,
    ).delete()

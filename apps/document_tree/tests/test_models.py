from django.contrib.contenttypes.models import (
    ContentType,
)
from django.test import (
    TestCase,
)

from apps.document_tree.models import (
    SharedTreeElement,
    TreeEntity,
    TreeFile,
    TreeFolder,
)
from apps.opeaz_heart.models import (
    CommercialCondition,
    Document,
    Flyer,
    Groupement,
    Laboratory,
    Pharmacy,
)


class DeleteTreeEntityTestCase(
    TestCase,
):

    def test_delete_groupement(
        self,
    ):
        """If a Groupement is deleted, then the associated
            TreeEntity is also deleted.
        """
        groupement = Groupement.objects.create(
            name="Test Groupement",
        )
        ct = ContentType.objects.get_for_model(
            model=Groupement,
        )
        entity = TreeEntity.objects.create(
            original_entity_ct=ct,
            original_entity_id=groupement.id,
        )
        self.assertTrue(
            TreeEntity.objects.filter(
                id=entity.id,
            ).exists(),
        )
        groupement.delete()
        self.assertFalse(
            TreeEntity.objects.filter(
                id=entity.id,
            ).exists(),
        )

    def test_delete_pharmacy(
        self,
    ):
        """If a Pharmacy is deleted, then the associated
            TreeEntity is also deleted.
        """
        pharmacy = Pharmacy.objects.create(
            name="Test Pharmacy",
        )
        ct = ContentType.objects.get_for_model(
            model=Pharmacy,
        )
        entity = TreeEntity.objects.create(
            original_entity_ct=ct,
            original_entity_id=pharmacy.id,
        )
        self.assertTrue(
            TreeEntity.objects.filter(
                id=entity.id,
            ).exists(),
        )
        pharmacy.delete()
        self.assertFalse(
            TreeEntity.objects.filter(
                id=entity.id,
            ).exists(),
        )

    def test_delete_laboratory(
        self,
    ):
        """If a Laboratory is deleted, then the associated
            TreeEntity is also deleted.
        """
        laboratory = Laboratory.objects.create(
            name="Test Laboratory",
            code="LAB001",
        )
        ct = ContentType.objects.get_for_model(
            model=Laboratory,
        )
        entity = TreeEntity.objects.create(
            original_entity_ct=ct,
            original_entity_id=laboratory.id,
        )
        self.assertTrue(
            TreeEntity.objects.filter(
                id=entity.id,
            ).exists(),
        )
        laboratory.delete()
        self.assertFalse(
            TreeEntity.objects.filter(
                id=entity.id,
            ).exists(),
        )


class DeleteTreeFileTestCase(
    TestCase,
):

    def setUp(
        self,
    ):
        self.laboratory = Laboratory.objects.create(
            name="Test Laboratory",
            code="LAB001",
        )
        self.entity_ct = ContentType.objects.get_for_model(
            model=Laboratory,
        )
        self.entity = TreeEntity.objects.create(
            original_entity_ct=self.entity_ct,
            original_entity_id=self.laboratory.id,
        )
        self.folder = TreeFolder.objects.create(
            name="Root",
            tree_entity=self.entity,
        )

    def test_delete_document(
        self,
    ):
        """If a Document is deleted, then the associated
            TreeFile is also deleted.
        """
        doc = Document.objects.create(
            laboratory=self.laboratory,
            name="Doc A",
            file="documents/doc_a.pdf",
        )
        ct = ContentType.objects.get_for_model(
            model=Document,
        )
        tree_file = TreeFile.objects.create(
            tree_entity=self.entity,
            tree_folder=self.folder,
            original_file_ct=ct,
            original_file_id=doc.id,
        )
        self.assertTrue(
            TreeFile.objects.filter(
                id=tree_file.id,
            ).exists(),
        )
        doc.delete()
        self.assertFalse(
            TreeFile.objects.filter(
                id=tree_file.id,
            ).exists(),
        )

    def test_delete_flyer(
        self,
    ):
        """If a Flyer is deleted, then the associated
            TreeFile is also deleted.
        """
        flyer = Flyer.objects.create(
            laboratory=self.laboratory,
            title="Flyer A",
            image="flyers/flyer_a.png",
            start_at="2026-01-01",
            end_at="2026-12-31",
        )
        ct = ContentType.objects.get_for_model(
            model=Flyer,
        )
        tree_file = TreeFile.objects.create(
            tree_entity=self.entity,
            tree_folder=self.folder,
            original_file_ct=ct,
            original_file_id=flyer.id,
        )
        self.assertTrue(
            TreeFile.objects.filter(
                id=tree_file.id,
            ).exists(),
        )
        flyer.delete()
        self.assertFalse(
            TreeFile.objects.filter(
                id=tree_file.id,
            ).exists(),
        )

    def test_delete_commercial_condition(
        self,
    ):
        """If a CommercialCondition is deleted, then the associated
            TreeFile is also deleted.
        """
        cc = CommercialCondition.objects.create(
            laboratory=self.laboratory,
            name="CC A",
            text="Condition content",
            year=2026,
        )
        ct = ContentType.objects.get_for_model(
            model=CommercialCondition,
        )
        tree_file = TreeFile.objects.create(
            tree_entity=self.entity,
            tree_folder=self.folder,
            original_file_ct=ct,
            original_file_id=cc.id,
        )
        self.assertTrue(
            TreeFile.objects.filter(
                id=tree_file.id,
            ).exists(),
        )
        cc.delete()
        self.assertFalse(
            TreeFile.objects.filter(
                id=tree_file.id,
            ).exists(),
        )


class DeleteSharedTreeElementTestCase(
    TestCase,
):

    def setUp(
        self,
    ):
        self.laboratory = Laboratory.objects.create(
            name="Test Laboratory",
            code="LAB001",
        )
        self.entity_ct = ContentType.objects.get_for_model(
            model=Laboratory,
        )
        self.entity = TreeEntity.objects.create(
            original_entity_ct=self.entity_ct,
            original_entity_id=self.laboratory.id,
        )
        self.folder = TreeFolder.objects.create(
            name="Root",
            tree_entity=self.entity,
        )
        doc = Document.objects.create(
            laboratory=self.laboratory,
            name="Doc A",
            file="documents/doc_a.pdf",
        )
        ct = ContentType.objects.get_for_model(
            model=Document,
        )
        self.file = TreeFile.objects.create(
            tree_entity=self.entity,
            tree_folder=self.folder,
            original_file_ct=ct,
            original_file_id=doc.id,
        )

    def test_delete_tree_folder(
        self,
    ):
        """If a TreeFolder is deleted, then the associated
            SharedTreeElement is also deleted.
        """
        ct = ContentType.objects.get_for_model(
            model=TreeFolder,
        )
        shared = SharedTreeElement.objects.create(
            tree_entity=self.entity,
            original_tree_element_ct=ct,
            original_tree_element_id=self.folder.id,
        )
        self.assertTrue(
            SharedTreeElement.objects.filter(
                id=shared.id,
            ).exists(),
        )
        self.folder.delete()
        self.assertFalse(
            SharedTreeElement.objects.filter(
                id=shared.id,
            ).exists(),
        )

    def test_delete_tree_file(
        self,
    ):
        """If a TreeFile is deleted, then the associated
            SharedTreeElement is also deleted.
        """
        ct = ContentType.objects.get_for_model(
            model=TreeFile,
        )
        shared = SharedTreeElement.objects.create(
            tree_entity=self.entity,
            original_tree_element_ct=ct,
            original_tree_element_id=self.file.id,
        )
        self.assertTrue(
            SharedTreeElement.objects.filter(
                id=shared.id,
            ).exists(),
        )
        self.file.delete()
        self.assertFalse(
            SharedTreeElement.objects.filter(
                id=shared.id,
            ).exists(),
        )

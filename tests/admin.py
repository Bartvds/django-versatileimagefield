from django.contrib import admin
from django.forms import ModelForm

from versatileimagefield.widgets import VersatileImagePPOISelectWidget

from .models import VersatileImageTestModel, VersatileImageWidgetTestModel, VersatileImageTestParentModel, VersatileImageTestChildModel


class VersatileImageTestModelForm(ModelForm):

    class Meta:
        model = VersatileImageTestModel
        fields = (
            'image',
            'img_type',
            'optional_image',
            'optional_image_2',
            'optional_image_3'
        )
        widgets = {
            'optional_image': VersatileImagePPOISelectWidget(),
        }


class VersatileImageTestModelAdmin(admin.ModelAdmin):
    form = VersatileImageTestModelForm


class AlwaysChangedModelForm(ModelForm):
    """
    Ensures VersatileImageField's inline models ALWAYS get saved so PPOI
    values will make their way into the database.

    via: https://github.com/WGBH/django-versatileimagefield/issues/44
    """
    def has_changed(self):
        return True


class VersatileImageTestChildModelInlineAdmin(admin.StackedInline):
    model = VersatileImageTestChildModel
    form = AlwaysChangedModelForm
    fields = (
        'image',
    )
    extra = 0


class VersatileImageTestParentModelAdmin(admin.ModelAdmin):
    fields = (
        'some_field',
        'image',
    )
    inlines = (
        VersatileImageTestChildModelInlineAdmin,
    )


admin.site.register(VersatileImageTestModel, VersatileImageTestModelAdmin)
admin.site.register(VersatileImageWidgetTestModel)
admin.site.register(VersatileImageTestParentModel, VersatileImageTestParentModelAdmin)

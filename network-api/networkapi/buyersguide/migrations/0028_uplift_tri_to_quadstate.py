# Generated by Django 2.2.5 on 2019-10-09 21:15

from django.db import migrations
import networkapi.buyersguide.fields
from networkapi.buyersguide.utils import tri_to_quad, quad_to_tri

def copy_tri_to_quad(apps, schema_editor):
    Product = apps.get_model("buyersguide", "Product")
    for product in Product.objects.all():
        product.manage_security_temp = tri_to_quad(product.manage_security)
        product.must_change_default_password_temp = tri_to_quad(product.must_change_default_password)
        product.security_updates_temp = tri_to_quad(product.security_updates)
        product.uses_encryption_temp = tri_to_quad(product.uses_encryption)
        product.save()

def copy_quad_to_tri(apps, schema_editor):
    Product = apps.get_model("buyersguide", "Product")
    for product in Product.objects.all():
        product.manage_security = quad_to_tri(product.manage_security_temp)
        product.must_change_default_password = quad_to_tri(product.must_change_default_password_temp)
        product.security_updates = quad_to_tri(product.security_updates_temp)
        product.uses_encryption = quad_to_tri(product.uses_encryption_temp)
        product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0027_null_boolean_field'),
    ]

    operations = [
        # introduce temporary fields

        migrations.AddField(
            model_name='product',
            name='manage_security_temp',
            field=networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Manages security vulnerabilities?'),
        ),
        migrations.AddField(
            model_name='product',
            name='must_change_default_password_temp',
            field=networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Must change a default password?'),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_temp',
            field=networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Security updates?'),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_temp',
            field=networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does the product use encryption?'),
        ),

        # perform data conversion for new field type

        migrations.RunPython(copy_tri_to_quad, copy_quad_to_tri),

        # remove original fields

        migrations.RemoveField(model_name='product', name='manage_security', ),
        migrations.RemoveField(model_name='product', name='must_change_default_password', ),
        migrations.RemoveField(model_name='product', name='security_updates', ),
        migrations.RemoveField(model_name='product', name='uses_encryption', ),

        # and rename the temporary fields back to their original name

        migrations.RenameField(
            model_name='product',
            old_name='manage_security_temp',
            new_name='manage_security',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='must_change_default_password_temp',
            new_name='strong_password',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='security_updates_temp',
            new_name='security_updates',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='uses_encryption_temp',
            new_name='uses_encryption',
        ),

        # then, rename all other fields that needed to be renamed

        migrations.RenameField(
            model_name='product',
            old_name='must_change_default_password_helptext',
            new_name='strong_password_helptext',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='manage_security',
            new_name='manage_vulnerabilities',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='manage_security_helptext',
            new_name='manage_vulnerabilities_helptext',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='child_rules',
            new_name='parental_controls'
        ),

        # and finally, remove the help text attribyte on the "strong password" field

        migrations.AlterField(
            model_name='product',
            name='strong_password',
            field=networkapi.buyersguide.fields.ExtendedYesNoField(),
        ),
    ]

from django.core.validators import FileExtensionValidator
from django.db import models

# from django.http import HttpRequest
# from django.urls import reverse
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import qrcode
# from io import BytesIO
# from PIL import Image
# from django.core.files.base import ContentFile


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(
        null=True, blank=True, default="Product has no description"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    image = models.ImageField(
        upload_to="product/img/",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        null=False,
        blank=False,
    )
    qr_code = models.ImageField(
        upload_to="product/qr-codes/",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        null=True,
        blank=True,
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"ID [{self.id}] {self.name}"


#     def generate_qr_code(self):
#         product_url = HttpRequest().build_absolute_uri(
#             reverse("product", args=[self.id])
#         )
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr.add_data(product_url)
#         qr.make(fit=True)
#         img = qr.make_image(fill_color="black", back_color="white")
#         img_bytes = BytesIO()
#         img.save(img_bytes, format="PNG")
#         filename = f"qr_code_{self.id}.png"
#         self.qr_code.save(filename, ContentFile(img_bytes.getvalue()), save=True)
#         self.save()


# @receiver(post_save, sender=Product)
# def generate_qr_code(sender, instance, **kwargs):
#     instance.generate_qr_code()

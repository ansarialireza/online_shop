from googletrans import Translator

class tools:
    def translate_to_english(farsi_word):
        translator = Translator()
        translation = translator.translate(farsi_word, src='fa', dest='en')
        return translation.text
    





# from django.urls import reverse
# from django.template.defaultfilters import slugify
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .translator import tools

# @receiver(pre_save, sender=Category)
# def category_pre_save(sender, instance, *args, **kwargs):
#     fa_slug=instance.category_name
#     en_slug=tools.translate_to_english(fa_slug)
#     instance.slug = slugify(en_slug)

# @receiver(pre_save, sender=Product)
# def product_pre_save(sender, instance, *args, **kwargs):
#     fa_slug=instance.title
#     en_slug=tools.translate_to_english(fa_slug)
#     instance.slug = slugify(en_slug)
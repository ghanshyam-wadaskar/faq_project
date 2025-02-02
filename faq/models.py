from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali

    def save(self, *args, **kwargs):
        # Auto-translate questions
        if not self.question_hi:
            self.question_hi = translator.translate(
                self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(
                self.question, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def get_translation(self, lang='en'):
        cache_key = f"faq_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        translation = getattr(self, f"question_{lang}", self.question)
        cache.set(cache_key, translation, timeout=3600)
        return translation

    def __str__(self):
        return self.question

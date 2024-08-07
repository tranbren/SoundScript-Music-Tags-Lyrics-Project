from django.db import models

class SearchHistory(models.Model):
    artist = models.CharField(max_length=255)
    song = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.artist} - {self.song} on {self.search_date}"
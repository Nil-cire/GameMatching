from django.contrib import admin
from .models import Game, GameType, Platform, Series, Language, Company, Target, Room

# Register your models here.


class GameAdmin(admin.ModelAdmin):
    list_display = ('chinese_name', 'english_name', 'japanese_name', 'release_date',
    'get_type', 'get_platform', 'serie', 'get_language', 'get_company', 'demo', 'get_target')

#    def get_type(self, obj):
#        return "\n".join([i.types for i in obj.type.all()])

#    def get_platform(self, obj):
#        return "\n".join([i.platforms for i in obj.platform.all()])


#    def get_language(self, obj):
#        return "\n".join([i.languages for i in obj.language.all()])

#    def get_company(self, obj):
#        return "\n".join([i.companies for i in obj.company.all()])

admin.site.register(Game, GameAdmin)


admin.site.register(GameType)
admin.site.register(Platform)
admin.site.register(Series)
admin.site.register(Language)
admin.site.register(Company)
admin.site.register(Target)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'create_time', 'room_id')
    readonly_fields = ('create_time',)
admin.site.register(Room, RoomAdmin)
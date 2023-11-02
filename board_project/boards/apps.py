from django.apps import AppConfig

class BoardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board_project.boards'

    def ready(self):
        # ここでカスタムコマンドを登録します
        try:
            import boards.commands
        except ImportError:
            pass

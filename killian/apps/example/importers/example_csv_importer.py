from ..serializers import ExampleSerializer
from killian.libs.csv_importer import AbstractModelCSVImporter


class ExampleCSVImporter(AbstractModelCSVImporter):

    def get_file_dir_path(self):
        return 'killian/apps/example/seed/example/'

    def get_model_name(self):
        return 'Example'

    def get_col_name_to_start(self):
        return 'code'

    def save_row(self, instance):
        ser = ExampleSerializer(data=instance)
        if ser.is_valid(raise_exception=True):
            ser.save()

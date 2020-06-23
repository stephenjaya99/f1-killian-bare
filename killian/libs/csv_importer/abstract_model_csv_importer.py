import logging
from abc import ABCMeta
from abc import abstractmethod

from django.db import transaction

from .csv_parser import CSVParser

logger = logging.getLogger(__name__)


class AbstractModelCSVImporter(metaclass=ABCMeta):

    @abstractmethod
    def get_file_dir_path(self):
        pass

    @abstractmethod
    def get_model_name(self):
        pass

    @abstractmethod
    def get_col_name_to_start(self):
        pass

    def get_csv_parser(self):
        return CSVParser(col_name_to_start=self.get_col_name_to_start())

    @abstractmethod
    def save_row(self, instance):
        pass

    def execute(self, filenames):
        csv_parser = self.get_csv_parser()

        for filename in filenames:
            file_path = self.get_file_dir_path().lower() + filename.lower() + '.csv'
            row_number = 0
            errors = []

            start_info = "Starting to do ADD import %s: %s" % (
                self.get_model_name(), file_path)
            logger.info(start_info)
            try:
                with transaction.atomic():
                    instances = csv_parser.convert_instance_to_json(
                        file_path)
                    log_info = "Finished conversion for %d %s(s)." % (
                        len(instances), self.get_model_name())
                    logger.info(log_info)

                    for instance in instances:
                        row_number += 1
                        try:
                            self.save_row(instance)
                        except Exception as e:
                            log_err = "%s - row %d: %s" % (
                                self.get_model_name(), row_number, str(e))
                            errors.append(log_err)

                    if errors:
                        for error in errors:
                            logger.error(error)
                        raise Exception(
                            "There are some errors on CSV - %s. Rolling Back!" % file_path)

                    log_info = "Success: Import %s: %s." % (
                        self.get_model_name(), file_path)
                    logger.info(log_info)

            except Exception as e:
                logger.error(str(e))

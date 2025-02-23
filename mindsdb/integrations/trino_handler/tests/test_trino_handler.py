import unittest

from mindsdb.api.mysql.mysql_proxy.mysql_proxy import RESPONSE_TYPE
from mindsdb.integrations.trino_handler.trino_handler import TrinoHandler


class TrinoHandlerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs = {
            "host": "qa.analytics.quantum.site.gs.com",
            "port": "8090",
            "user": "dqsvcuat",
            "password": "",
            "catalog": "gsam_dev2imddata_elastic",
            "schema": "default",
            "service_name": "HTTP/qa.analytics.quantum.site.gs.com",
            "config_file_name": "test_trino_config.ini"
        }
        cls.handler = TrinoHandler('test_trino_handler', **cls.kwargs)

    def test_0_canary(self):
        print('Running canary test')
        assert True
        print('Canary test ran successfully')

    def test_1_check_status(self):
        conn_status = self.handler.check_status()
        print('Trino connection status: ', conn_status)
        assert conn_status.get('success')

    def test_2_get_tables(self):
        tables = self.handler.get_tables()
        assert tables

    def test_3_describe_table(self):
        described = self.handler.describe_table("axioma_att_2021-12")
        assert described['type'] is not RESPONSE_TYPE.ERROR

    # TODO: complete tests implementation
    # def test_3_get_views(self):
    #     views = self.handler.get_views()
    #     assert views['type'] is not RESPONSE_TYPE.ERROR
    #
    # def test_4_select_query(self):
    #     query = "SELECT * FROM data.test_mdb WHERE 'id'='1'"
    #     result = self.handler.query(query)
    #     assert result['type'] is RESPONSE_TYPE.TABLE
    #

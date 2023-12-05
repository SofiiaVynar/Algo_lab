import unittest

from src.main5 import isAble


class TestIsAbleFunction(unittest.TestCase):

    def test_all_cities_reachable(self):
        pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Стрий', 'Сховище_2'], ['Долина', 'Сховище_1'],
                     ['Місто', 'Сховище_3']]
        cities = ['Львів', 'Стрий', 'Долина', 'Місто']
        storages = ['Сховище_1', 'Сховище_2', 'Сховище_3']

        unable = isAble(pipelines, cities, storages)
        expected_result = {'Сховище_1': ['Місто'], 'Сховище_2': ['Місто'], 'Сховище_3': ['Львів', 'Стрий', 'Долина']}
        self.assertEqual(unable, expected_result)

    def test_some_cities_unreachable(self):
        test_pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Стрий', 'Сховище_2'], ['Долина', 'Сховище_1']]
        cities = ['Львів', 'Стрий', 'Долина', 'Місто']
        storages = ['Сховище_1', 'Сховище_2', 'Сховище_3']

        unable = isAble(test_pipelines, cities, storages)
        expected_result = {'Сховище_1': ['Місто'], 'Сховище_2': ['Місто'], 'Сховище_3': ['Львів', 'Стрий', 'Долина', 'Місто']}
        self.assertEqual(unable, expected_result)

    def test_empty_input(self):
        test_pipelines = []
        cities = []
        storages = []
        unable = isAble(test_pipelines, cities, storages)
        self.assertEqual(unable, {})


if __name__ == '__main__':
    unittest.main()


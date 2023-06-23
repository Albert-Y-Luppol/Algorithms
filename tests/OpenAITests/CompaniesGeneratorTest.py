import unittest
from src.OpenAI.companies_generator import get_list_of_companies_in_industry

class CompaniesGeneratorTest(unittest.TestCase):
    @staticmethod
    def test_generate():
        industry = 'Travel industry. Companies that provide housing: hotels, rooms, flats, houses, etc.'
        companies = get_list_of_companies_in_industry(industry)
        print(companies)

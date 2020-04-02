from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


from django.shortcuts import render
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer


# from .serializers import blogSerializer
from blog import models


import requests
from bs4 import BeautifulSoup
from bs4 import CData
import bs4

class ListCryptocurrencyView(generics.ListAPIView):
    """ Provides a get method handler """
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer



class mediumblog(APIView):
    """Medium blog feed api https://medium.com/feed/the-story """

    def post(self, request, formate=None, ):
        """"Returns a list of Apiview features """

        tp_api = "https://medium.com/feed/the-story"
        response = requests.get(tp_api)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('item', )

        records = []
        for result in results:
            title = result.find('title').string[0:100:]
            link = result.find('guid').string
            # category = result.find('category').string
            pubdate = result.find('pubdate').string
            contentencoded = result.find('content:encoded').string

            getFinalArticle = BeautifulSoup(contentencoded, 'html.parser')
            article_img = getFinalArticle.find('figure').img['src']
            article_desc = getFinalArticle.find(
                'figure').next_sibling.text[0:200:]
            
            # queryset = mediumblogdb.objects.all()
            # serializer_class = blogSerializer

            response_dictionary = {
                "title": title,
                "link": link,
                # "category": category,
                "pubdate": pubdate,
                "article_img": article_img,
                "article_desc": article_desc
            }

            records.append(response_dictionary)
        return Response(records)


class TOIBusinessApi(APIView):
    """ TOI Business api https://timesofindia.indiatimes.com/rssfeeds/1898055.cms """

    def post(self, request, formate=None,):
        # TOI Business
        TOIBusiness_api = "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms"
        TOIBusiness_response = requests.get(TOIBusiness_api)
        TOIBusiness_soup = BeautifulSoup(
            TOIBusiness_response.text, 'html.parser')
        TOIBusiness_results = TOIBusiness_soup.find_all('item', )
        TOIBusiness_records = []
        for TOIBusiness_result in TOIBusiness_results:

            TOIBusiness_main = TOIBusiness_result.find('description').string
            TOIBusiness_soup_desc = BeautifulSoup(
                TOIBusiness_main.string, 'html.parser')

            TOIBusiness_pubDate = TOIBusiness_result.find('pubdate').string

            response_dictionary = {
                "title": TOIBusiness_result.find('title').string,
                "link": TOIBusiness_result.find('guid').string,
                "pubdate": TOIBusiness_pubDate[0:16:],
                "article_img": TOIBusiness_soup_desc.a.img['src'],
                "article_desc": TOIBusiness_soup_desc.get_text()
            }

            TOIBusiness_records.append(response_dictionary)
        return Response(TOIBusiness_records)


class TOITechnologyNewsApi(APIView):
    """ TOI Technology News api https://timesofindia.indiatimes.com/rssfeeds/5880659.cms """

    def post(self, request, formate=None,):
        # TOI Technology News
        TOITechnologyNews_api = "https://timesofindia.indiatimes.com/rssfeeds/5880659.cms"
        TOITechnologyNews_response = requests.get(TOITechnologyNews_api)
        TOITechnologyNews_soup = BeautifulSoup(
            TOITechnologyNews_response.text, 'html.parser')
        TOITechnologyNews_results = TOITechnologyNews_soup.find_all('item', )
        TOIBusiness_records = []
        for TOITechnologyNews_result in TOITechnologyNews_results:
            TOITechnologyNews_main = TOITechnologyNews_result.find(
                'description').string
            TOITechnologyNews_soup_desc = BeautifulSoup(
                TOITechnologyNews_main.string, 'html.parser')
            if TOITechnologyNews_soup_desc.a is None:
                print('')
            else:
                if TOITechnologyNews_soup_desc.a.img is None:
                    TOITechnologyNews_img = TOITechnologyNews_soup_desc.a.img['src']
                else:
                    TOITechnologyNews_img = TOITechnologyNews_soup_desc.a.img['src']
            TOIBusiness_pubDate = TOITechnologyNews_result.find(
                'pubdate').string

            TOITechnologyNews__records = {
                "title": TOITechnologyNews_result.find('title').string,
                "link": TOITechnologyNews_result.find('guid').string,
                "pubdate": TOIBusiness_pubDate[0:16:],
                "article_img": TOITechnologyNews_img,
                "article_desc": TOITechnologyNews_soup_desc.get_text()
            }
            TOIBusiness_records.append(TOITechnologyNews__records)
        return Response(TOIBusiness_records)


class EntrepreneurApi(APIView):
    """ Entrepreneur api https://www.entrepreneur.com/latest.rss """

    def post(self, request, formate=None,):
        EntrepreneurApi_api = "https://www.entrepreneur.com/latest.rss"
        EntrepreneurApi_response = requests.get(EntrepreneurApi_api)
        EntrepreneurApi_soup = BeautifulSoup(
            EntrepreneurApi_response.text, 'html.parser')
        EntrepreneurApi_results = EntrepreneurApi_soup.find_all('item', )

        EntrepreneurApi_recordsw = []
        for EntrepreneurApi_result in EntrepreneurApi_results:
            EntrepreneurApi_main = EntrepreneurApi_result.find(
                'description').string
            EntrepreneurApi_newimg = EntrepreneurApi_result.find('media:content')[
                'url']
            EntrepreneurApi_soup_desc = BeautifulSoup(
                EntrepreneurApi_main.string, 'html.parser')

            EntrepreneurApi_pubDate = EntrepreneurApi_result.find(
                'pubdate').string

            EntrepreneurApi_records = {
                "title": EntrepreneurApi_result.find('title').string,
                "link": EntrepreneurApi_result.find('guid').string,
                "pubdate": EntrepreneurApi_pubDate[0:16:],
                "article_img":  EntrepreneurApi_newimg,
                "article_desc": EntrepreneurApi_soup_desc.get_text()
            }
            EntrepreneurApi_recordsw.append(EntrepreneurApi_records)
        return Response(EntrepreneurApi_recordsw)

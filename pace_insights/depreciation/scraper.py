# -*- coding: utf-8 -*-
"""
Script to scrape car depreciation data from http://www.whatcar.com
"""
import json
import logging

import requests
from lxml import html

from .models import CarMake, CarModel, CarVersion, Depreciation
from .utils import make_new_depreciation


logger = logging.getLogger(__name__)
GUESTHOST = 'http://www.whatcar.com'
CPC_PATH = '/car-depreciation-calculator/'  #car depreciation calculator path
CM_PATH = '/Advice/DepreciationSearchSelectMake'  # Car Models  ?makeId=4708
CV_PATH = '/Advice/DepreciationSearchSelectModelVersion' # modelVersionId=5199
CD_PATH = '/car-depreciation-calculator/results' # ?editionId=44479


def scrapping():
    """ scrape from what car, saving car make, car model, car CarVersion
    and car depreciation info into db.
    """

    res = requests.get(GUESTHOST + CPC_PATH)
    tree = html.fromstring(res.text)
    for carmake in tree.xpath('//*[@id="makeId"]/option')[1:]:
        make_id = carmake.attrib['value']
        logger.info(u"{}: {}".format(make_id, carmake.text))
        car_make = CarMake.objects.get_or_create(
            name=carmake.text
        )[0]
        car_make.whatcar_id = make_id
        car_make.save()

        carmodel_res = requests.get(
            GUESTHOST + CM_PATH,
            params={'makeId': make_id})
        for carmodel in carmodel_res.json():
            model_id = carmodel['id']
            model_name = carmodel['name']

            logger.info(u'{}: {}'.format(model_id, model_name))
            carv_res = requests.get(
                GUESTHOST + CV_PATH,
                params={'modelVersionId': model_id}
            )
            car_model = CarModel.objects.get_or_create(
                name=model_name,
                car_make=car_make
            )[0]
            car_model.whatcar_id = model_id
            car_model.save()

            for carv in carv_res.json():
                logger.info(carv)
                print carv
                name = u'{} {} {}dr'.format(
                    carv['bodyRange'],
                    carv['name'],
                    carv['doors']
                )
                car_version = CarVersion.objects.get_or_create(
                    car_model=car_model,
                    name=name,
                    doors=carv['doors'],
                    body_range=carv['bodyRange'],
                )[0]
                car_version.whatcar_id = carv['id']
                car_version.save()

                depr_res = requests.get(
                    GUESTHOST + CD_PATH,
                    params={'editionId': carv['id']}
                )
                depr_tree = html.fromstring(depr_res.text)
                tds = depr_tree.xpath('//*[@id="contentColumn"]//table//td')
                full_name = tds[0].text
                year_0 = tds[1].text
                year_1 = tds[2].text
                year_2 = tds[3].text
                year_3 = tds[4].text
                year_4 = tds[5].text
                msg = u"{}:{},{},{},{},{}".format(
                    full_name, year_0, year_1, year_2, year_3, year_4, 
                )
                car_depr = Depreciation.objects.get_or_create(
                    car_version=car_version,
                    year_0=year_0,
                    year_1=year_1,
                    year_2=year_2,
                    year_3=year_3,
                    year_4=year_4
                )[0]
                if not car_depr.year_0_mock:
                    car_depr.year_0_mock = make_new_depreciation(year_0)
                    car_depr.year_1_mock = make_new_depreciation(year_1)
                    car_depr.year_2_mock = make_new_depreciation(year_2)
                    car_depr.year_3_mock = make_new_depreciation(year_3)
                    car_depr.year_4_mock = make_new_depreciation(year_4)
                    car_depr.save()

                print msg
                logger.info(msg)


if __name__ == '__main__':
    scrapping()

# SPDX-License-Identifier: BSD 3-Clause Clear License

import pathlib

import requests
from lxml import etree


BROTHER_SUPPORT_URL = "https://support.brother.com"
BROTHER_SEWING_CATALOG_URL = "https://support.brother.com/g/b/sp/productseries.aspx?c=us&lang=en&content=ml&pcatid=36"

MANUALS_PATH = pathlib.Path("manuals")


def get_operation_manual_url(model_url: str):
    resp = requests.get(f"{BROTHER_SUPPORT_URL}/{model_url}")
    tree = etree.HTML(resp.text)

    operation_manual = tree.xpath(
        "//a[contains(@class, 'ManualToFileForGlobal') and text()='Download']"
    )
    if operation_manual:
        operation_manual_url = operation_manual[0].get("href")
        return operation_manual_url


def download_operation_manual(model_name: str, operation_manual_url: str):
    if pathlib.Path(MANUALS_PATH / f"{model_name.replace('/', '-')}.pdf").exists():
        return

    resp = requests.get(operation_manual_url)
    with open(MANUALS_PATH / f"{model_name.replace('/', '-')}.pdf", "wb") as f:
        f.write(resp.content)


def main():
    response = requests.get(BROTHER_SEWING_CATALOG_URL)
    tree = etree.HTML(response.text)
    models = tree.xpath("//a[@class='select-product']")
    for model in models:
        model_url = model.get("href")
        model_name = model.xpath(".//p[@class='ttl']/text()")[0]
        print(model_name, model_url)

        operation_manual_url = get_operation_manual_url(model_url)
        if operation_manual_url:
            download_operation_manual(model_name, operation_manual_url)


if __name__ == "__main__":
    main()

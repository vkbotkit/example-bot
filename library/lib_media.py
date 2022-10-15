"""
Copyright 2022 kensoi
"""

import asyncio
from os import path
from urllib.parse import urlparse
from vkbotkit.objects import callback, filters, LibraryModule
from vkbotkit import utils


DOWNLOAD_PHOTO_MESSAGE = """
Фотографии сохранены в директории assets/downloads
"""
STICKER_DOWNLOADED = """
Стикер скачан и теперь хранится в директории assets/downloads
"""
NO_PHOTO_MESSAGE = """
К команде необходимо приложить фотографии для скачивания
"""


class HasPhoto(filters.Filter):
    """
    Фильтр для сообщений, содержащих фото
    """
    async def check(self, package):
        if not package.attachments:
            return

        photos_filter = filter(lambda x: x['type'] == 'photo', package.attachments)

        return len(photos_filter) != 0


class StickerFilter(filters.Filter):
    """
    Фильтр для стикеров
    """
    async def check(self, package):
        """
        Проверка на наличии стикера в сообщении
        """
        if hasattr(package, "attachments"):
            if package.attachments[0]['type'] == "sticker":
                return True

        return False


async def download_file(toolkit, download_url):
    """
    Функция для сохранения изображения в папку assets
    """

    file_name = "downloads" + utils.PATH_SEPARATOR + path.basename(urlparse(download_url).path)

    if not file_name.endswith(".jpg"):
        if not file_name.endswith(".png"):
            file_name += ".png"

    async with toolkit.core.session.get(download_url) as url_content:
        file_content = await url_content.read()

    with toolkit.assets(file_name, 'wb+') as created_file:
        created_file.write(file_content)

    return file_name


class Main(LibraryModule):
    """
    Библиотека с примером работы toolkit.assets и toolkit.uploader
    """


    @callback(filters.IsCommand({"media", "медиа", "медия"}) & HasPhoto())
    async def download_media(self, package):
        """
        Обработчик отправленных пользователем фотографий, который сохраняет
        скачанные фото в папку ассетов
        """

        photos_filtered = filter(lambda x: x['type'] == 'photo', package.attachments)
        photos = list(map(
            lambda x: sorted(x['photo']['sizes'],
            key = lambda j: j['width'])[-1]['url'],
            photos_filtered
        ))

        await asyncio.gather(*[download_file(package.toolkit, image) for image in photos])
        await package.toolkit.send_reply(package, DOWNLOAD_PHOTO_MESSAGE)


    @callback(filters.IsCommand({"media", "медиа", "медия"}) & HasPhoto())
    async def send_media_help(self, package):
        """
        Инструкции к download_media обработчику
        """

        await package.toolkit.send_reply(package, NO_PHOTO_MESSAGE)


    @callback(StickerFilter())
    async def download_sticker(self, package):
        """
        Обработчик отправленных пользователем стикеров, который сохраняет
        скачанные стикеры в папку ассетов
        """

        sticker = package.attachments[0]['sticker']
        filtered = filter(lambda image: image['height'] == 512, sticker['images'])
        result = await download_file(package.toolkit, list(filtered)[0]['url'])

        await package.toolkit.send_reply(package, STICKER_DOWNLOADED.format(result))

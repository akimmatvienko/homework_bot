class ApiRequestException(Exception):
    """Ошибка при обращении к API."""

    pass


class NotOkStatusCodeException(Exception):
    """Ошибка, статус код не 200."""

    pass


class HomeWorkApiException(Exception):
    """Ошибка при неправильном наполнении словаря homework в ответе API."""

    pass


class InvalidTelegramTokenException(Exception):
    """Ошибка при некорректном токене для бота Telegram."""

    pass


class SendMessageError(Exception):
    """Ошибка при попытке отправить сообщение."""

    pass


class JsonError(Exception):
    """Ответ от API не был преобзаван в json."""

    pass

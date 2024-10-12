from dependency_injector import providers

from mono_bot.domain.abs.message_service import MessageServiceBase
from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.interfaces.filter_service import IFilterService
from mono_bot.domain.interfaces.mono_repository import IMonoRepository
from mono_bot.domain.interfaces.presentation_service import IPresentationService
from mono_bot.domain.interfaces.url_service import IUrlService


class ConfigServiceFactory(providers.Factory):
    provided_type = IConfigService


class UrlServiceFactory(providers.Factory):
    provided_type = IUrlService


class MonoRepositoryFactory(providers.Factory):
    provided_type = IMonoRepository


class FilterServiceFactory(providers.Factory):
    provided_type = IFilterService


class PresentationServiceFactory(providers.Factory):
    provided_type = IPresentationService


class MessageServiceFactory(providers.Factory):
    provided_type = MessageServiceBase

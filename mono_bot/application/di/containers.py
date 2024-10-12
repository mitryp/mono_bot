from dependency_injector import containers, providers

from mono_bot.application.api.mono_client import build_mono_client
from mono_bot.application.bot.tg_client import build_tg_client
from mono_bot.application.di import factories
from mono_bot.application.mediator.mediator import Mediator
from mono_bot.application.services.config_service import ConfigService
from mono_bot.application.services.filter_service import FilterService
from mono_bot.application.services.presentation_service import PresentationService
from mono_bot.application.services.url_service import UrlService
from mono_bot.domain.interfaces.mono_repository import IMonoRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            'mono_bot.application.api.mono_client',
            'mono_bot.application.bot.bot_thread',
            'mono_bot.application.bot.tg_client',
            'mono_bot.application.hook_server.server',
            'mono_bot.application.hook_server.webhook_controller',
        ])

    config_service = factories.ConfigServiceFactory(
        ConfigService,
        providers.Configuration(yaml_files=['config.yaml']),
    )

    url_service = factories.UrlServiceFactory(
        UrlService,
        providers.Configuration(yaml_files=['urls.yaml']),
    )

    filter_service = factories.FilterServiceFactory(
        FilterService,
        config_service,
    )

    presentation_service = factories.PresentationServiceFactory(
        PresentationService,
        config_service,
    )

    http_client = providers.Singleton(build_mono_client)

    mono_repository = providers.AbstractSingleton(IMonoRepository)

    tg_client = providers.Singleton(build_tg_client)

    mediator = providers.Singleton(Mediator)

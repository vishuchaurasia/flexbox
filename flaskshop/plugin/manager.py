import logging
from importlib.metadata import entry_points, metadata
from typing import Optional

import pluggy

from .models import PluginRegistry  # noqa: F401

logger = logging.getLogger(__name__)


class FlaskshopPluginManager(pluggy.PluginManager):
    def __init__(self, project_name):
        super().__init__(project_name)
        self.external_plugins = set()
        self.plugin_metadata = {}

    # Python 3.9 compatible type hints (no PEP 604 `X | Y`)
    def load_setuptools_entrypoints(self, group: str, name: Optional[str] = None) -> int:
        """Load modules from querying the specified setuptools entrypoint name.
        Return the number of loaded plugins."""
        logger.info(f"Loading plugins under entrypoint {group}")
        eps = entry_points()
        # Python 3.9 stdlib `importlib.metadata.entry_points()` returns a dict.
        # Python 3.10+ returns an object with `.select(...)`.
        if hasattr(eps, "select"):
            candidates = eps.select(group=group)
        else:
            candidates = eps.get(group, [])

        if name is not None:
            candidates = [ep for ep in candidates if ep.name == name]

        for ep in candidates:
            if self.get_plugin(ep.name) or self.is_blocked(ep.name):
                continue

            plugin = ep.load()
            self.register(plugin, name=ep.name)
            self.external_plugins.add(ep.name)
            self._plugin_distinfo.append((plugin, ep.dist))
            self.plugin_metadata[ep.name] = metadata(ep.dist._normalized_name).json
            logger.info(f"Loaded plugin: {ep.name}")
        logger.info(
            f"Loaded {len(self._plugin_distinfo)} plugins for entrypoint {group}"
        )
        return len(self._plugin_distinfo)

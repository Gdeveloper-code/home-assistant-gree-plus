"""Diagnostics support for the gree_plus integration."""

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.core import HomeAssistant

from . import GreePlusConfigEntry

# Redact credentials and account identifiers, including entry metadata.
TO_REDACT = frozenset(
    {
        "access_token",
        "refresh_token",
        "open_id",
        "name",
        "title",
        "unique_id",
    }
)


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant,
    entry: GreePlusConfigEntry,
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    return {"entry": async_redact_data(entry.as_dict(), TO_REDACT)}

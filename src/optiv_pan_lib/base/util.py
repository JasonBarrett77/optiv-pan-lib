# src/optiv_lib/providers/pan/util.py
from __future__ import annotations

from typing import Any, Callable, Iterable

import xmltodict

DEFAULT_FORCE_LIST: Iterable[str | Callable[..., bool]] = ("entry", "member", "line")
SENSITIVE_KEYS = {"pre-shared-key", "private-key", "public-key", "key", "bind-password", "password", "secret", "auth-password", "priv-password", "phash"}

def sanitize(branch: dict) -> None:
    """Recursively remove sensitive fields from nested PAN-OS config dicts."""
    for k, v in list(branch.items()):
        key_lower = k.lower()
        if isinstance(v, str) and (any(token in key_lower for token in SENSITIVE_KEYS) or key_lower in SENSITIVE_KEYS):
            branch[k] = "<redacted>"
        elif isinstance(v, dict):
            sanitize(v)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    sanitize(item)



def parse_xml(text: str, *, force_list: Iterable | None = None) -> dict:
    return xmltodict.parse(text, force_list=force_list or DEFAULT_FORCE_LIST)


def node_text(node: Any) -> str | None:
    if node is None:
        return None
    if isinstance(node, dict):
        node = node.get("#text")
    s = ("" if node is None else str(node)).strip()
    return s or None


def as_list(x: Any) -> list[Any]:
    return x if isinstance(x, list) else ([] if x is None else [x])


def yn_bool(s: str | None) -> bool:
    return s is not None and s.strip().lower() in {"y", "yes", "true", "1"}


def collect_members(tag_node: Any) -> list[str]:
    if not isinstance(tag_node, dict):
        return []
    return [v for v in (node_text(m) for m in as_list(tag_node.get("member"))) if v]


def xpath_dg_address(device_group: str) -> str:
    return f"/config/devices/entry/device-group/entry[@name='{device_group}']/address"

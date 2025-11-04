# src/optiv_lib/providers/pan/panorama/managed_devices/api.py
from __future__ import annotations

from optiv_pan_lib.base import ops
from optiv_pan_lib.base.session import PanoramaSession


def list_connected_devices(*, session: PanoramaSession) -> dict:
    """
    Panorama → show devices connected
    Returns inner 'result'.
    """
    cmd = "<show><devices><connected/></devices></show>"
    return ops.op(session=session, cmd=cmd)


def list_all_devices(*, session: PanoramaSession) -> dict:
    """
    Panorama → show devices all
    Returns inner 'result'.
    """
    cmd = "<show><devices><all/></devices></show>"
    return ops.op(session=session, cmd=cmd)


def list_connected(*, session: PanoramaSession) -> dict:
    """
    Panorama → show devices connected
    Returns inner 'result'.
    """
    cmd = "<show><devices><connected/></devices></show>"
    return ops.op(session=session, cmd=cmd)


def list_all(*, session: PanoramaSession) -> dict:
    """
    Panorama → show devices all
    Returns inner 'result'.
    """
    cmd = "<show><devices><all/></devices></show>"
    return ops.op(session=session, cmd=cmd)

#!/usr/bin/env python

#  This file and its contents are licensed under the Apache License 2.0.
#  Please see the included NOTICE for copyright information and
#  LICENSE-APACHE for a copy of the license.

# Common settings for our CI jobs
#
# EARLIEST is the minimum postgres version required when building from source
# LATEST is the maximum postgres version that is supported
# ABI_MIN is the minimum postgres version required when the extension was build against LATEST
#
# TODO: Enable tests uploading in linux-build-and-test.yaml for macos once we
# move to a new minor version below

PG13_EARLIEST = "13.2"
PG13_LATEST = "13.13"
PG13_ABI_MIN = "13.5"

PG14_EARLIEST = "14.0"
PG14_LATEST = "14.10"
PG14_ABI_MIN = "14.0"

PG15_EARLIEST = "15.0"
PG15_LATEST = "15.5"
PG15_ABI_MIN = "15.0"

PG16_EARLIEST = "16.0"
PG16_LATEST = "16.1"
PG16_ABI_MIN = "16.0"

PG_LATEST = [PG13_LATEST, PG14_LATEST, PG15_LATEST, PG16_LATEST]

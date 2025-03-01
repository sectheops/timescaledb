/*
 * This file and its contents are licensed under the Timescale License.
 * Please see the included NOTICE for copyright information and
 * LICENSE-TIMESCALE for a copy of the license.
 */
#pragma once

#include <postgres.h>

extern Datum job_add(PG_FUNCTION_ARGS);
extern Datum job_alter(PG_FUNCTION_ARGS);
extern Datum job_delete(PG_FUNCTION_ARGS);
extern Datum job_run(PG_FUNCTION_ARGS);
extern Datum job_alter_set_hypertable_id(PG_FUNCTION_ARGS);

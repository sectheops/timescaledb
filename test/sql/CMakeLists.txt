include(GenerateTestSchedule)

set(TEST_FILES
    agg_bookends.sql
    alter.sql
    alternate_users.sql
    baserel_cache.sql
    broken_tables.sql
    chunks.sql
    chunk_adaptive.sql
    chunk_utils.sql
    create_chunks.sql
    create_hypertable.sql
    create_table.sql
    constraint.sql
    copy.sql
    copy_where.sql
    ddl_errors.sql
    debug_utils.sql
    drop_extension.sql
    drop_hypertable.sql
    drop_owned.sql
    drop_rename_hypertable.sql
    drop_schema.sql
    dump_meta.sql
    extension_scripts.sql
    generated_as_identity.sql
    grant_hypertable.sql
    hash.sql
    index.sql
    information_views.sql
    insert_many.sql
    insert_single.sql
    insert_returning.sql
    lateral.sql
    null_exclusion.sql
    partition.sql
    partitioning.sql
    pg_dump_unprivileged.sql
    pg_join.sql
    plain.sql
    plan_hypertable_inline.sql
    relocate_extension.sql
    reloptions.sql
    repair.sql
    size_utils.sql
    sort_optimization.sql
    sql_query.sql
    tableam.sql
    tablespace.sql
    triggers.sql
    truncate.sql
    upsert.sql
    util.sql
    vacuum.sql
    version.sql
    license.sql)

set(TEST_TEMPLATES
    append.sql.in
    cluster.sql.in
    cursor.sql.in
    ddl.sql.in
    delete.sql.in
    histogram_test.sql.in
    insert.sql.in
    plan_hashagg.sql.in
    rowsecurity.sql.in
    update.sql.in
    parallel.sql.in
    partitionwise.sql.in
    plan_expand_hypertable.sql.in
    plan_ordered_append.sql.in
    query.sql.in
    timestamp.sql.in)

# Loader test must distinguish between Apache and TSL builds so we parametrize
# this here
set(LOADER_TEST_FILE loader-${TEST_LICENSE_SUFFIX})
configure_file(loader.sql.in
               ${CMAKE_CURRENT_SOURCE_DIR}/${LOADER_TEST_FILE}.sql)

# tests that fail or are unreliable when run in parallel bgw tests need to run
# first otherwise they are flaky
set(SOLO_TESTS
    alter
    alternate_users
    bgw_launcher
    chunk_utils
    index
    net
    pg_dump_unprivileged
    tablespace
    telemetry)

list(APPEND SOLO_TESTS ${LOADER_TEST_FILE})

if(CMAKE_BUILD_TYPE MATCHES Debug)
  list(
    APPEND
    TEST_FILES
    bgw_launcher.sql
    c_unit_tests.sql
    copy_memory_usage.sql
    guc_options.sql
    metadata.sql
    multi_transaction_index.sql
    net.sql
    pg_dump.sql
    symbol_conflict.sql
    test_utils.sql
    ${LOADER_TEST_FILE}.sql)
  if(USE_TELEMETRY)
    list(APPEND TEST_FILES telemetry.sql)
  endif()
endif(CMAKE_BUILD_TYPE MATCHES Debug)

if((${PG_VERSION_MAJOR} GREATER_EQUAL "13"))
  list(APPEND TEST_FILES trusted_extension.sql vacuum_parallel.sql)
endif()

if((${PG_VERSION_MAJOR} GREATER_EQUAL "14"))
  list(APPEND TEST_FILES ddl_extra.sql)
endif()

if((${PG_VERSION_MAJOR} GREATER_EQUAL "15"))
  list(APPEND TEST_FILES merge.sql)
  list(APPEND TEST_TEMPLATES ts_merge.sql.in)
endif()

# only test custom type if we are in 64-bit architecture
if("${CMAKE_SIZEOF_VOID_P}" STREQUAL "8")
  list(APPEND TEST_FILES custom_type.sql)
endif()

# Regression tests that vary with PostgreSQL version. Generated test files are
# put in the original source directory since all tests must be in the same
# directory. These files are updated when the template is edited, but not when
# the output file is deleted. If the output is deleted either recreate it
# manually, or rerun cmake on the root dir.
foreach(TEMPLATE_FILE ${TEST_TEMPLATES})
  string(LENGTH ${TEMPLATE_FILE} TEMPLATE_NAME_LEN)
  math(EXPR TEMPLATE_NAME_LEN ${TEMPLATE_NAME_LEN}-7)
  string(SUBSTRING ${TEMPLATE_FILE} 0 ${TEMPLATE_NAME_LEN} TEMPLATE)
  set(TEST_FILE ${TEMPLATE}-${TEST_VERSION_SUFFIX}.sql)
  configure_file(${TEMPLATE_FILE} ${CMAKE_CURRENT_SOURCE_DIR}/${TEST_FILE}
                 @ONLY)
  list(APPEND TEST_FILES ${TEST_FILE})
endforeach(TEMPLATE_FILE)

if(NOT TEST_GROUP_SIZE)
  set(PARALLEL_GROUP_SIZE 20)
else()
  set(PARALLEL_GROUP_SIZE ${TEST_GROUP_SIZE})
endif()

# Generate a test schedule for each configuration.
generate_test_schedule(
  ${TEST_SCHEDULE}
  TEST_FILES
  ${TEST_FILES}
  SOLO
  ${SOLO_TESTS}
  GROUP_SIZE
  ${PARALLEL_GROUP_SIZE})

add_subdirectory(loader)
